#!/usr/bin/env python3
"""Read-only audit for the internal project documentation standard."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REQUIRED_FILES = [
    "README.md",
    "agent.md",
    "docs/standard.md",
    "docs/requirements.md",
    "docs/architecture.md",
    "docs/api.md",
    "docs/database.md",
    "docs/deploy.md",
    "docs/test.md",
    "docs/changelog.md",
]

README_SECTIONS = [
    "Project Basic Information",
    "Project Overview",
    "Quick Start",
    "Project Structure",
    "Current Progress",
    "Documentation Index",
    "Known Issues",
    "Next Steps",
    "AI / Agent Usage Prompt",
]

ENUMS = {
    "project_status": ["planned", "in-development", "joint-debugging", "testing", "online", "maintenance", "paused", "archived"],
    "feature_status": ["pending-planning", "pending-implementation", "in-development", "pending-joint-debugging", "pending-testing", "completed", "deprecated"],
    "api_status": ["pending-design", "pending-implementation", "implemented", "pending-joint-debugging", "online", "deprecated"],
    "database_status": ["pending-design", "designed", "migrated", "online", "deprecated"],
    "test_status": ["untested", "testing", "passed", "failed", "blocked", "not-applicable"],
    "issue_status": ["pending", "in-progress", "resolved", "deferred", "closed"],
}

SECRET_PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|secret|token|password|passwd|private[_-]?key)\s*[:=]\s*['\"]?[^\s'\"<>]+"),
    re.compile(r"-----BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY-----"),
]


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8-sig", errors="replace")


def find_status_values(text: str) -> list[str]:
    values: list[str] = []
    for line in text.splitlines():
        if "|" not in line or "---" in line:
            continue
        for cell in [part.strip(" `") for part in line.strip().strip("|").split("|")]:
            if cell:
                values.append(cell)
    return values


def audit(root: Path) -> dict:
    result: dict = {
        "root": str(root),
        "missing_files": [],
        "readme_missing_sections": [],
        "placeholder_counts": {},
        "secret_risks": [],
        "status_notes": [],
    }

    for rel in REQUIRED_FILES:
        if not (root / rel).exists():
            result["missing_files"].append(rel)

    readme = root / "README.md"
    if readme.exists():
        text = read_text(readme)
        for section in README_SECTIONS:
            if section not in text:
                result["readme_missing_sections"].append(section)

    for rel in REQUIRED_FILES:
        path = root / rel
        if not path.exists() or path.is_dir():
            continue
        text = read_text(path)
        count = text.count("TBD")
        if count:
            result["placeholder_counts"][rel] = count
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                result["secret_risks"].append(rel)
                break

    allowed = set().union(*ENUMS.values())
    header_values = {"status", "current status", "test status", "database status", "api status"}
    bad_generic_values = {"done", "doing", "not-started", "finished", "todo"}
    for rel in ["README.md", "docs/requirements.md", "docs/api.md", "docs/database.md", "docs/test.md"]:
        path = root / rel
        if not path.exists():
            continue
        suspicious = []
        for value in find_status_values(read_text(path)):
            normalized = value.strip().lower()
            if normalized in header_values:
                continue
            if normalized in bad_generic_values:
                suspicious.append(value)
            elif "status" in normalized and value not in allowed:
                suspicious.append(value)
        if suspicious:
            result["status_notes"].append({"file": rel, "values": sorted(set(suspicious))})

    result["ok"] = not any(
        result[key]
        for key in ["missing_files", "readme_missing_sections", "secret_risks", "status_notes"]
    )
    return result


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: audit_docs.py <project-root>", file=sys.stderr)
        return 2
    root = Path(sys.argv[1]).resolve()
    if not root.exists() or not root.is_dir():
        print(f"Project root not found: {root}", file=sys.stderr)
        return 2
    print(json.dumps(audit(root), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
