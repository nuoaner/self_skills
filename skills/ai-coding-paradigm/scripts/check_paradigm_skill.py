#!/usr/bin/env python3
"""Read-only quality checks for the ai-coding-paradigm skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/paradigm-checklist.md",
    "references/prompt-templates.md",
]

REQUIRED_SECTIONS = [
    "## Overview",
    "## Review Modes",
    "## Core Workflow",
    "## Ten Engineering Dimensions",
    "## Output Contract",
    "## When to Read References",
    "## Quality Gate",
    "## Common Failure Modes",
]

REQUIRED_MODES = [
    "maturity-review",
    "boundary-review",
    "delivery-review",
    "prompt-hardening",
    "risk-review",
]

REQUIRED_DIMENSIONS = [
    "Requirement and Boundary Clarity",
    "Single Responsibility and Module Cohesion",
    "Dependency Direction and Layering",
    "Interface and Data Contracts",
    "Validation and Error Handling",
    "Testability and Regression Protection",
    "Observability and Diagnosability",
    "Security, Permission, and Data Safety",
    "Delivery, Rollback, and Environment Readiness",
    "AI Executability and Handoff Clarity",
]

BAD_PATTERNS = [
    ("replacement character", re.compile(r"\ufffd")),
    ("mojibake marker", re.compile(r"�|����|锟")),
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
        if "name: ai-coding-paradigm" not in text:
            failures.append("SKILL.md has unexpected skill name")
        if "description: Use when" not in text:
            failures.append("description should start with Use when")
        for section in REQUIRED_SECTIONS:
            if section not in text:
                failures.append(f"SKILL.md missing section: {section}")
        for mode in REQUIRED_MODES:
            if f"`{mode}`" not in text:
                failures.append(f"SKILL.md missing review mode: {mode}")
        if "references/paradigm-checklist.md" not in text:
            failures.append("SKILL.md does not route to paradigm checklist")
        if "references/prompt-templates.md" not in text:
            failures.append("SKILL.md does not route to prompt templates")

    checklist_path = root / "references" / "paradigm-checklist.md"
    if checklist_path.exists():
        text = checklist_path.read_text(encoding="utf-8")
        for dimension in REQUIRED_DIMENSIONS:
            if dimension not in text:
                failures.append(f"paradigm-checklist.md missing dimension: {dimension}")

    for path in root.rglob("*"):
        if path.is_file():
            rel_path = path.relative_to(root)
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                failures.append(f"not valid UTF-8: {rel_path}")
                continue
            for label, pattern in BAD_PATTERNS:
                if rel_path.as_posix() == "scripts/check_paradigm_skill.py" and label in {"replacement character", "mojibake marker"}:
                    continue
                if pattern.search(text):
                    failures.append(f"{rel_path} contains {label}")

    return failures


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    failures = collect_failures(root)
    if failures:
        print("ai-coding-paradigm quality check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("ai-coding-paradigm quality check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
