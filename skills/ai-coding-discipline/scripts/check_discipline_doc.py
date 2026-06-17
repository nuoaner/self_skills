#!/usr/bin/env python3
"""Read-only quality checks for the ai-coding-discipline skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_FILES = [
    "SKILL.md",
    "references/discipline-checklist.md",
    "references/prompt-template.md",
    "references/pressure-scenarios.md",
]

REQUIRED_SECTIONS = [
    "## Core Contract",
    "## When To Use",
    "## Execution Gate",
    "## Stop Conditions",
    "## Anti-Patterns",
    "## Pressure Rules",
    "## Quick Reference",
    "## Resource Use",
    "## Common Mistakes",
]

BAD_PATTERNS = [
    ("replacement character", re.compile(r"\ufffd")),
    ("absolute Windows path", re.compile(r"[A-Za-z]:[\\/]|C:/|C:\\\\")),
    ("missing reference typo", re.compile(r"workflow-checklist\.md")),
]


def check(root: Path) -> int:
    failures: list[str] = []

    for rel_path in REQUIRED_FILES:
        path = root / rel_path
        if not path.exists():
            failures.append(f"missing required file: {rel_path}")

    skill_path = root / "SKILL.md"
    if skill_path.exists():
        text = skill_path.read_text(encoding="utf-8")

        if not text.startswith("---\n"):
            failures.append("SKILL.md missing YAML frontmatter")

        for section in REQUIRED_SECTIONS:
            if section not in text:
                failures.append(f"SKILL.md missing section: {section}")

        for label, pattern in BAD_PATTERNS:
            if pattern.search(text):
                failures.append(f"SKILL.md contains {label}")

        for match in re.findall(r"\]\((references/[^)]+)\)", text):
            if not (root / match).exists():
                failures.append(f"broken reference link: {match}")

    for rel_path in REQUIRED_FILES[1:]:
        path = root / rel_path
        if path.exists():
            text = path.read_text(encoding="utf-8")
            for label, pattern in BAD_PATTERNS[:2]:
                if pattern.search(text):
                    failures.append(f"{rel_path} contains {label}")

    if failures:
        print("ai-coding-discipline quality check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("ai-coding-discipline quality check passed")
    return 0


if __name__ == "__main__":
    skill_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    raise SystemExit(check(skill_root))
