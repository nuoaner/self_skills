#!/usr/bin/env python3
"""Read-only quality checks for the client-technical-reporting skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
]

REQUIRED_SECTIONS = [
    "## Overview",
    "## Required Structure",
    "## Writing Rules",
    "## Section Guidance",
    "## Output Template",
    "## Quality Checklist",
]

REQUIRED_REPORT_HEADINGS = [
    "1. 本次做了什么",
    "2. 迁移方式",
    "3. 主要改动位置",
    "4. 真实接口后续在哪改",
    "5. 模块问题定位",
    "6. 后续联调需确认的事项",
    "7. 总结",
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
        if "name: client-technical-reporting" not in text:
            failures.append("SKILL.md has unexpected skill name")
        if "description: Use when" not in text:
            failures.append("description should start with Use when")
        for section in REQUIRED_SECTIONS:
            if section not in text:
                failures.append(f"SKILL.md missing section: {section}")
        for heading in REQUIRED_REPORT_HEADINGS:
            if heading not in text:
                failures.append(f"SKILL.md missing required report heading: {heading}")

    for path in root.rglob("*"):
        if path.is_file():
            rel_path = path.relative_to(root)
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                failures.append(f"not valid UTF-8: {rel_path}")
                continue
            for label, pattern in BAD_PATTERNS:
                if label == "absolute Windows path" and rel_path.as_posix() == "scripts/check_client_report_skill.py":
                    continue
                if pattern.search(text):
                    failures.append(f"{rel_path} contains {label}")

    return failures


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    failures = collect_failures(root)
    if failures:
        print("client-technical-reporting quality check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("client-technical-reporting quality check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
