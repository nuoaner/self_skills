#!/usr/bin/env python3
"""Read-only quality checks for the internal-project-doc-standardizer skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "scripts/audit_docs.py",
    "references/readme-template.md",
    "references/agent-template.md",
    "references/standard.md",
    "references/requirements-template.md",
    "references/architecture-template.md",
    "references/api-template.md",
    "references/database-template.md",
    "references/deploy-template.md",
    "references/test-template.md",
    "references/changelog-template.md",
]

REQUIRED_SECTIONS = [
    "## Overview",
    "## Operation Modes",
    "## Required Workflow",
    "## Standard File Set",
    "## README Entry Rules",
    "## Required Status Enums",
    "## Delivery Template",
    "## Safety Rules",
    "## Quality Gate",
    "## Common Mistakes",
]

REQUIRED_MODES = ["audit", "generate", "split", "sync", "repair"]

REQUIRED_ENUMS = [
    "planned",
    "in-development",
    "joint-debugging",
    "testing",
    "online",
    "maintenance",
    "paused",
    "archived",
    "pending-planning",
    "pending-implementation",
    "pending-joint-debugging",
    "pending-testing",
    "completed",
    "deprecated",
    "pending-design",
    "implemented",
    "designed",
    "migrated",
    "untested",
    "passed",
    "failed",
    "blocked",
    "not-applicable",
    "pending",
    "in-progress",
    "resolved",
    "deferred",
    "closed",
]

BAD_PATTERNS = [
    ("replacement character, CJK text, or mojibake", re.compile(r"\ufffd|[\u3400-\u9fff\uf900-\ufaff]")),
    ("possible secret", re.compile(r"sk-[A-Za-z0-9]{20,}|api[_-]?key\s*[:=]|password\s*[:=]|secret\s*[:=]|token\s*[:=]", re.I)),
]


def collect_failures(root: Path) -> list[str]:
    failures: list[str] = []

    for rel_path in REQUIRED_FILES:
        if not (root / rel_path).exists():
            failures.append(f"missing required file: {rel_path}")

    skill_path = root / "SKILL.md"
    if skill_path.exists():
        text = skill_path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            failures.append("SKILL.md missing YAML frontmatter")
        if "name: internal-project-doc-standardizer" not in text:
            failures.append("SKILL.md has unexpected skill name")
        if "description: Use when" not in text:
            failures.append("description should start with Use when")
        for section in REQUIRED_SECTIONS:
            if section not in text:
                failures.append(f"SKILL.md missing section: {section}")
        for mode in REQUIRED_MODES:
            if f"`{mode}`" not in text:
                failures.append(f"SKILL.md missing operation mode: {mode}")
        for enum in REQUIRED_ENUMS:
            if enum not in text:
                failures.append(f"SKILL.md missing required enum: {enum}")

    for path in root.rglob("*"):
        if path.is_file():
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                failures.append(f"not valid UTF-8: {path.relative_to(root)}")
                continue
            for label, pattern in BAD_PATTERNS:
                if pattern.search(text):
                    failures.append(f"{path.relative_to(root)} contains {label}")

    return failures


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    failures = collect_failures(root)
    if failures:
        print("internal-project-doc-standardizer quality check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("internal-project-doc-standardizer quality check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
