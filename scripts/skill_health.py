#!/usr/bin/env python3
"""Read-only portfolio health checks for self_skills."""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

from catalog import validate as validate_catalog

ROOT = Path(__file__).resolve().parents[1]
FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
FIELD = re.compile(r"(?m)^([a-z][a-z0-9_-]*):\s*(.*?)\s*$")
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
VERSION = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")


def parse_frontmatter(path: Path) -> dict[str, str] | None:
    try:
        text = path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError):
        return None
    match = FRONTMATTER.match(text)
    if not match:
        return None
    return {key: value.strip().strip("\"'") for key, value in FIELD.findall(match.group(1))}


def local_links(markdown: str) -> list[str]:
    result = []
    for raw in LINK.findall(markdown):
        target = raw.strip().split()[0].strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or target.startswith("#"):
            continue
        path = unquote(parsed.path)
        if path:
            result.append(path)
    return result


def eval_coverage(path: Path) -> tuple[dict[str, Counter], list[str]]:
    counts: dict[str, Counter] = {}
    errors: list[str] = []
    if not path.is_file():
        return counts, ["evals/cases.jsonl missing"]
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        try:
            case = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"evals/cases.jsonl:{line_no}: invalid JSON ({exc.msg})")
            continue
        if not isinstance(case, dict):
            errors.append(f"evals/cases.jsonl:{line_no}: expected object")
            continue
        name, kind = case.get("skill"), case.get("kind")
        if not isinstance(name, str) or kind not in {"positive", "negative", "task"}:
            errors.append(f"evals/cases.jsonl:{line_no}: invalid skill or kind")
            continue
        counts.setdefault(name, Counter())[kind] += 1
    return counts, errors


def audit(root: Path) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    catalog, catalog_errors = validate_catalog(root)
    errors.extend(catalog_errors)
    if catalog_errors:
        return {"status": "fail", "errors": errors, "warnings": warnings, "skills": []}

    entries = catalog["entries"]
    tiers = Counter(item["tier"] for item in entries)
    coverage, eval_errors = eval_coverage(root / "evals" / "cases.jsonl")
    errors.extend(eval_errors)
    skill_rows = []

    for item in entries:
        name, tier = item["name"], item["tier"]
        skill_dir = root / "skills" / name
        skill_file = skill_dir / "SKILL.md"
        metadata = parse_frontmatter(skill_file)
        row = {"name": name, "tier": tier, "checks": [], "warnings": []}

        if tier == "reference":
            row["checks"].append("reference_only")
            skill_rows.append(row)
            continue

        if metadata is None:
            message = f"{name}: SKILL.md has no readable YAML frontmatter"
            if tier == "core":
                errors.append(message)
            else:
                warnings.append(message)
                row["warnings"].append(message)
        else:
            if metadata.get("name") != name:
                errors.append(f"{name}: frontmatter name mismatch")
            if tier == "core" and not metadata.get("description"):
                errors.append(f"{name}: description missing")
            row["checks"].append("frontmatter")

        if tier == "core":
            version_file = skill_dir / "VERSION"
            if not version_file.is_file() or not VERSION.fullmatch(version_file.read_text(encoding="utf-8").strip()):
                errors.append(f"{name}: VERSION missing or invalid")
            else:
                row["checks"].append("version")

            agent_file = skill_dir / "agents" / "openai.yaml"
            if not agent_file.is_file():
                errors.append(f"{name}: agents/openai.yaml missing")
            else:
                agent_text = agent_file.read_text(encoding="utf-8-sig")
                if not re.search(r"(?m)^\s*display_name:\s*\S", agent_text):
                    errors.append(f"{name}: agents/openai.yaml display_name missing")
                else:
                    row["checks"].append("agent_metadata")

            actual = coverage.get(name, Counter())
            for kind, minimum in (("positive", 2), ("negative", 2), ("task", 1)):
                if actual[kind] < minimum:
                    errors.append(f"{name}: {kind} eval cases {actual[kind]}/{minimum}")
            row["eval_cases"] = dict(actual)
            row["checks"].append("eval_coverage")

        try:
            body = skill_file.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{name}: cannot read SKILL.md ({exc})")
            skill_rows.append(row)
            continue

        for target in local_links(body):
            candidate = (skill_dir / target).resolve()
            try:
                candidate.relative_to(skill_dir.resolve())
            except ValueError:
                errors.append(f"{name}: local link escapes skill directory: {target}")
                continue
            if not candidate.is_file():
                errors.append(f"{name}: broken local link {target}")
        row["checks"].append("local_links")
        skill_rows.append(row)

    known = {item["name"] for item in entries}
    for name in sorted(set(coverage) - known):
        warnings.append(f"evaluation cases refer to uncataloged skill: {name}")

    return {
        "status": "fail" if errors else "pass",
        "summary": {
            "total": len(entries), "core": tiers["core"], "lab": tiers["lab"],
            "reference": tiers["reference"],
            "eval_cases": sum(sum(c.values()) for c in coverage.values()),
            "errors": len(errors), "warnings": len(warnings),
        },
        "errors": errors, "warnings": warnings, "skills": skill_rows,
        "scope_note": "Structural and declared-evaluation checks only; no model behavior or output quality was measured.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only self_skills health audit")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    parser.add_argument("--strict", action="store_true", help="return nonzero when warnings exist")
    args = parser.parse_args()
    result = audit(args.root.resolve())
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        summary = result.get("summary", {})
        print(f"Skill health: {result['status'].upper()}")
        if summary:
            print("Inventory: " + ", ".join(f"{k}={summary[k]}" for k in ("total", "core", "lab", "reference", "eval_cases")))
        for message in result["warnings"]:
            print("WARN:", message)
        for message in result["errors"]:
            print("ERROR:", message)
        print(result.get("scope_note", ""))
    return 1 if result["status"] == "fail" or (args.strict and result["warnings"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
