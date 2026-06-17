#!/usr/bin/env python3
"""Read-only quality checks for the market-commercialization-strategist skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_FILES = [
    "SKILL.md",
    "references/market-manager-playbook.md",
    "agents/openai.yaml",
]

REQUIRED_SECTIONS = [
    "## Overview",
    "## Workflow",
    "## Output Modes",
    "## Decision Rules",
    "## Common Mistakes",
]

REQUIRED_PLAYBOOK_SECTIONS = [
    "## Core Principle",
    "## 1. Fast Diagnosis",
    "## 4. Ethical Retention and Dependency",
    "## 7. Commercialization Design",
    "## 10. Commercial Readiness Checklist",
    "## 11. Output Templates",
]

BAD_PATTERNS = [
    ("replacement character", re.compile(r"\ufffd")),
    ("absolute Windows path", re.compile(r"[A-Za-z]:[\\/]|C:/|C:\\\\")),
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
        if "name: market-commercialization-strategist" not in text:
            failures.append("SKILL.md has unexpected skill name")
        if "description: Use when" not in text:
            failures.append("description should start with Use when")
        for section in REQUIRED_SECTIONS:
            if section not in text:
                failures.append(f"SKILL.md missing section: {section}")
        if "references/market-manager-playbook.md" not in text:
            failures.append("SKILL.md does not reference the playbook")

    playbook_path = root / "references" / "market-manager-playbook.md"
    if playbook_path.exists():
        text = playbook_path.read_text(encoding="utf-8")
        for section in REQUIRED_PLAYBOOK_SECTIONS:
            if section not in text:
                failures.append(f"playbook missing section: {section}")

    for rel_path in ["SKILL.md", "references/market-manager-playbook.md", "agents/openai.yaml"]:
        path = root / rel_path
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for label, pattern in BAD_PATTERNS:
            if pattern.search(text):
                failures.append(f"{rel_path} contains {label}")

    return failures


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    failures = collect_failures(root)
    if failures:
        print("market-commercialization-strategist quality check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("market-commercialization-strategist quality check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
