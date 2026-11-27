#!/usr/bin/env python3
"""Inventory declared Skill dependencies and watch curated public contracts.

Inventory is offline. Remote checks are opt-in and read-only. A detected
change is a review signal, not an automatic compatibility or breakage verdict.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import html
import ipaddress
import json
import re
import shlex
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
URL_RE = re.compile(r"https?://[^\s)\]<>\"']+")
PIP_RE = re.compile(r"(?:python\s+-m\s+)?pip\s+install\s+([^\n]+)", re.I)
NPM_RE = re.compile(r"npm\s+(?:i|install)\s+([^\n]+)", re.I)
PACKAGE_MAP = {
    "pptx": "python-pptx",
    "PIL": "Pillow",
    "yaml": "PyYAML",
    "cv2": "opencv-python",
    "bs4": "beautifulsoup4",
}
PLACEHOLDER_HOSTS = {"example.com", "example.org", "example.net"}
MAX_RESPONSE_BYTES = 1_500_000


class VisibleTextParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.hidden_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag.lower() in {"script", "style", "noscript", "svg"}:
            self.hidden_depth += 1

    def handle_endtag(self, tag):
        if tag.lower() in {"script", "style", "noscript", "svg"} and self.hidden_depth:
            self.hidden_depth -= 1

    def handle_data(self, data):
        if not self.hidden_depth:
            self.parts.append(data)

    def text(self):
        return re.sub(r"\s+", " ", " ".join(self.parts)).strip()


def module_dependencies(path: Path) -> set[str]:
    try:
        source = path.read_text(encoding="utf-8-sig")
        tree = ast.parse(source, filename=str(path))
    except (OSError, UnicodeError, SyntaxError):
        return set()
    stdlib = getattr(sys, "stdlib_module_names", set())
    found = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names = [alias.name for alias in node.names]
        elif isinstance(node, ast.ImportFrom) and node.module:
            names = [node.module]
        else:
            continue
        for name in names:
            top = name.split(".", 1)[0]
            if top not in stdlib and not top.startswith("_"):
                found.add(PACKAGE_MAP.get(top, top))
    return found


def command_dependencies(text: str) -> set[str]:
    found = set()
    for pattern, kind in ((PIP_RE, "pip"), (NPM_RE, "npm")):
        for match in pattern.finditer(text):
            raw = match.group(1).strip()
            raw = raw.split(chr(96), 1)[0].split("#", 1)[0]
            try:
                args = shlex.split(raw)
            except ValueError:
                continue
            for arg in args:
                if arg.startswith("-"):
                    continue
                if kind == "npm" and arg in {"-D", "--save-dev", "-g", "--global"}:
                    continue
                found.add(arg)
                break
    return found


def scan_inventory(root: Path) -> dict:
    catalog = json.loads((root / "skills" / "catalog.json").read_text(encoding="utf-8"))
    results = []
    for item in catalog["entries"]:
        if item["tier"] == "reference":
            continue
        name = item["name"]
        directory = root / "skills" / name
        urls, packages, sources = set(), set(), []
        for path in directory.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in {".md", ".py", ".yaml", ".yml", ".toml", ".txt"}:
                continue
            try:
                text = path.read_text(encoding="utf-8-sig")
            except (OSError, UnicodeError):
                continue
            relative = path.relative_to(directory).as_posix()
            for url in URL_RE.findall(text):
                url = url.rstrip(".,;:")
                host = urllib.parse.urlsplit(url).hostname or ""
                if host not in PLACEHOLDER_HOSTS and "owner/repo" not in url:
                    urls.add(url)
            packages.update(command_dependencies(text))
            if path.suffix.lower() == ".py":
                packages.update(module_dependencies(path))
            if urls or packages:
                sources.append(relative)
        results.append({
            "skill": name,
            "tier": item["tier"],
            "external_urls": sorted(urls),
            "runtime_packages": sorted(packages),
            "scanned_files": sorted(set(sources)),
        })
    return {
        "schema_version": 1,
        "scope": "Static scan of repository Skill files; inferred imports and URLs require human confirmation.",
        "skills": results,
        "summary": {
            "skills_scanned": len(results),
            "unique_urls": len({u for row in results for u in row["external_urls"]}),
            "unique_packages": len({p for row in results for p in row["runtime_packages"]}),
        },
    }


def validate_registry(data: dict) -> list[str]:
    errors = []
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        return ["dependency-watch schema_version must be 1"]
    items = data.get("watch_items")
    if not isinstance(items, list):
        return ["watch_items must be an array"]
    seen = set()
    for item in items:
        if not isinstance(item, dict):
            errors.append("each watch item must be an object")
            continue
        identifier = item.get("id")
        if not isinstance(identifier, str) or not identifier or identifier in seen:
            errors.append(f"invalid or duplicate watch id: {identifier}")
            continue
        seen.add(identifier)
        parsed = urllib.parse.urlsplit(item.get("url", ""))
        if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
            errors.append(f"{identifier}: watch URL must be an HTTPS URL without credentials")
        allowed = item.get("allowed_hosts", [])
        if not isinstance(allowed, list) or parsed.hostname not in allowed:
            errors.append(f"{identifier}: source hostname must appear in allowed_hosts")
        if not isinstance(item.get("checks", []), list):
            errors.append(f"{identifier}: checks must be an array")
        for check in item.get("checks", []):
            try:
                re.compile(check.get("pattern", ""))
            except (re.error, AttributeError):
                errors.append(f"{identifier}: invalid check pattern")
    return errors


def safe_public_url(url: str, allowed_hosts: set[str]) -> None:
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "https" or not parsed.hostname or parsed.hostname not in allowed_hosts:
        raise ValueError("URL is not HTTPS or its host is not allowlisted")
    if parsed.username or parsed.password:
        raise ValueError("URL credentials are not allowed")
    try:
        address = ipaddress.ip_address(parsed.hostname)
        if not address.is_global:
            raise ValueError("non-public IP addresses are not allowed")
    except ValueError as exc:
        if "does not appear to be an IPv4 or IPv6 address" not in str(exc):
            raise


class AllowlistRedirectHandler(urllib.request.HTTPRedirectHandler):
    def __init__(self, allowed_hosts: set[str]):
        super().__init__()
        self.allowed_hosts = allowed_hosts

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        safe_public_url(newurl, self.allowed_hosts)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def fetch_source(url: str, allowed_hosts: set[str], timeout: int = 12) -> tuple[str, str, int]:
    safe_public_url(url, allowed_hosts)
    opener = urllib.request.build_opener(AllowlistRedirectHandler(allowed_hosts))
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "self-skills-dependency-watch/1.0", "Accept": "text/html,text/plain;q=0.9"},
        method="GET",
    )
    with opener.open(request, timeout=timeout) as response:
        status = getattr(response, "status", 200)
        final_url = response.geturl()
        safe_public_url(final_url, allowed_hosts)
        payload = response.read(MAX_RESPONSE_BYTES + 1)
    if len(payload) > MAX_RESPONSE_BYTES:
        raise ValueError(f"response exceeds {MAX_RESPONSE_BYTES} bytes")
    decoded = payload.decode("utf-8", errors="replace")
    parser = VisibleTextParser()
    parser.feed(decoded)
    text = html.unescape(parser.text())
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return text, digest, status


def check_sources(registry: dict) -> dict:
    errors = validate_registry(registry)
    if errors:
        return {"status": "invalid_registry", "errors": errors, "results": []}
    results = []
    for item in registry["watch_items"]:
        allowed = set(item.get("allowed_hosts", []))
        row = {
            "id": item["id"], "skill": item.get("skill"),
            "kind": item.get("kind", "external_dependency"),
            "url": item["url"], "status": "unknown",
            "expected_version": item.get("expected_version"),
            "observed_version": None, "missing_checks": [],
            "sha256": None, "error": None,
        }
        try:
            text, digest, http_status = fetch_source(item["url"], allowed)
            row["sha256"] = digest
            row["http_status"] = http_status
            version_pattern = item.get("version_pattern")
            if version_pattern:
                match = re.search(version_pattern, text, re.I)
                row["observed_version"] = match.group(1) if match else None
            for check in item.get("checks", []):
                if not re.search(check["pattern"], text, re.I):
                    row["missing_checks"].append(check.get("label", check["pattern"]))
            version_changed = (
                row["expected_version"] is not None
                and row["observed_version"] != row["expected_version"]
            )
            if row["missing_checks"] or version_changed:
                row["status"] = "review_required"
            else:
                row["status"] = "ok"
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError, ValueError) as exc:
            row["status"] = "unreachable"
            row["error"] = str(exc)
        results.append(row)
    statuses = {row["status"] for row in results}
    overall = "review_required" if "review_required" in statuses else (
        "unreachable" if "unreachable" in statuses else "ok"
    )
    return {
        "generated_at": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(),
        "status": overall,
        "results": results,
        "limitations": [
            "A changed documentation page is a review signal, not proof of a breaking change.",
            "Only explicitly registered sources and checks are monitored; static inventory does not imply active monitoring.",
            "Remote checks are unauthenticated, read-only, bounded to allowlisted HTTPS hosts, and may fail transiently.",
        ],
    }


def render_markdown(data: dict) -> str:
    lines = ["# External Dependency and Interface Watch", "", f"Status: **{data.get('status', 'inventory')}**", ""]
    if "skills" in data:
        lines += [f"Scanned {data['summary']['skills_scanned']} Skills · {data['summary']['unique_urls']} unique URLs · {data['summary']['unique_packages']} unique packages", ""]
        for row in data["skills"]:
            lines.append(f"## {row['skill']} ({row['tier']})")
            lines.append("- Runtime packages: " + (", ".join(row["runtime_packages"]) if row["runtime_packages"] else "none detected"))
            lines.append("- External URLs:")
            lines.extend(f"  - {url}" for url in row["external_urls"])
            if not row["external_urls"]:
                lines.append("  - none detected")
            lines.append("")
    else:
        lines += ["| Source | Type | Status | Observed version | Missing checks / error |", "|---|---|---|---|---|"]
        for row in data.get("results", []):
            detail = ", ".join(row["missing_checks"]) or row.get("error") or "—"
            lines.append(f"| {row['id']} | {row['kind']} | {row['status']} | {row.get('observed_version') or '—'} | {detail} |")
        lines += ["", "## Limitations", ""]
        lines.extend(f"- {item}" for item in data.get("limitations", []))
    return "\n".join(lines) + "\n"


def emit(data: dict, fmt: str, output: Path | None) -> None:
    rendered = json.dumps(data, ensure_ascii=False, indent=2) + "\n" if fmt == "json" else render_markdown(data)
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only dependency inventory and interface watcher")
    parser.add_argument("command", choices=("validate", "inventory", "check"))
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--registry", type=Path, default=None)
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--strict", action="store_true", help="return nonzero for remote drift or unreachable sources")
    args = parser.parse_args()
    root = args.root.resolve()
    registry_path = args.registry or (root / "docs" / "dependency-watch.json")
    if args.command == "inventory":
        emit(scan_inventory(root), args.format, args.output)
        return 0
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    errors = validate_registry(registry)
    if args.command == "validate":
        if errors:
            for error in errors:
                print("ERROR:", error, file=sys.stderr)
            return 1
        print(f"PASS: {len(registry['watch_items'])} external sources registered.")
        return 0
    result = check_sources(registry)
    emit(result, args.format, args.output)
    return 1 if args.strict and result["status"] != "ok" else 0


if __name__ == "__main__":
    raise SystemExit(main())
