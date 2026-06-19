#!/usr/bin/env python3
"""Read-only quality checks for the project-prompt-polisher skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/prompt-patterns.md",
]

REQUIRED_SECTIONS = [
    "## Overview",
    "## Fast Workflow",
    "## Output Contract",
    "## When to Read References",
    "## Quality Bar",
    "## Common Failure Modes",
]

REQUIRED_REFERENCE_SECTIONS = [
    "## Universal Prompt Skeleton",
    "## UI / Frontend Prompt",
    "## Backend / API Prompt",
    "## Documentation Prompt",
    "## Testing / Debugging Prompt",
    "## Refactor Prompt",
    "## Automation / Script Prompt",
    "## Handoff Prompt",
    "## Pressure Examples",
]

REQUIRED_PHRASES = [
    "Do not expand functionality unrelated to this goal",
    "Acceptance criteria",
    "Needs confirmation",
    "Do not explain the rewrite unless the user asks",
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
        if "name: project-prompt-polisher" not in text:
            failures.append("SKILL.md has unexpected skill name")
        if "description: Use when" not in text:
            failures.append("description should start with Use when")
        if "references/prompt-patterns.md" not in text:
            failures.append("SKILL.md does not route to prompt-patterns reference")
        for section in REQUIRED_SECTIONS:
            if section not in text:
                failures.append(f"SKILL.md missing section: {section}")
        for phrase in REQUIRED_PHRASES:
            if phrase not in text:
                failures.append(f"SKILL.md missing required phrase: {phrase}")

    reference_path = root / "references" / "prompt-patterns.md"
    if reference_path.exists():
        text = reference_path.read_text(encoding="utf-8")
        for section in REQUIRED_REFERENCE_SECTIONS:
            if section not in text:
                failures.append(f"prompt-patterns.md missing section: {section}")

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
        print("project-prompt-polisher quality check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("project-prompt-polisher quality check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
