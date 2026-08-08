#!/usr/bin/env python3
"""Read-only audit for this personal skills repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
TRIGGER_TESTS = SKILLS_DIR / "TRIGGER_TESTS.md"

NAME_RE = re.compile(r"^[a-z0-9-]+$")
REPLACEMENT_CHAR_RE = re.compile(r"\ufffd")
COMMON_MOJIBAKE_RE = re.compile(r"(?:Ã.|Â.|â€|â€™|â€œ|â€\x9d|ï»¿)")
SECRET_RE = re.compile(
    r"sk-[A-Za-z0-9]{20,}|api[_-]?key\s*[:=]|password\s*[:=]|secret\s*[:=]|token\s*[:=]",
    re.I,
)
PLACEHOLDER_RE = re.compile(r"\bTODO\b|FIXME", re.I)


def parse_frontmatter(text: str) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, ["missing YAML frontmatter"]
    end = text.find("\n---", 4)
    if end == -1:
        return {}, ["unterminated YAML frontmatter"]

    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data, errors


def check_text_file(path: Path, root: Path) -> list[str]:
    rel = path.relative_to(root)
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return [f"{rel}: not valid UTF-8"]

    errors: list[str] = []
    if REPLACEMENT_CHAR_RE.search(text):
        errors.append(f"{rel}: contains Unicode replacement characters")
    if COMMON_MOJIBAKE_RE.search(text):
        errors.append(f"{rel}: contains likely mojibake")
    if SECRET_RE.search(text):
        errors.append(f"{rel}: may contain a real secret")
    return errors


def check_openai_yaml(path: Path, skill_name: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if not path.exists():
        return [f"{skill_name}: missing agents/openai.yaml"], warnings

    text = path.read_text(encoding="utf-8")
    has_interface = bool(re.search(r"(?m)^interface:\s*$", text))
    has_nested_display_name = bool(re.search(r"(?m)^[ \t]+display_name:\s*.+$", text))
    has_flat_display_name = bool(re.search(r"(?m)^display_name:\s*.+$", text))

    if has_interface:
        if not has_nested_display_name:
            errors.append(f"{skill_name}: agents/openai.yaml interface is missing display_name")
    elif has_flat_display_name:
        warnings.append(
            f"{skill_name}: agents/openai.yaml uses legacy top-level metadata; "
            "keep it for Codex compatibility or migrate deliberately to interface.*"
        )
    else:
        errors.append(f"{skill_name}: agents/openai.yaml missing display_name")

    return errors, warnings


def audit_skill(skill_dir: Path, trigger_text: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    name = skill_dir.name

    if not NAME_RE.match(name):
        errors.append(f"{name}: folder name must use lowercase letters, digits, and hyphens")

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        errors.append(f"{name}: missing SKILL.md")
        return errors, warnings

    text = skill_md.read_text(encoding="utf-8")
    frontmatter, fm_errors = parse_frontmatter(text)
    errors.extend(f"{name}: {error}" for error in fm_errors)

    if frontmatter.get("name") != name:
        errors.append(f"{name}: frontmatter name does not match folder")
    description = frontmatter.get("description", "")
    if not description:
        errors.append(f"{name}: missing description")
    elif len(description) > 1024:
        errors.append(f"{name}: description exceeds 1024 characters")
    elif "use when" not in description.lower():
        warnings.append(f"{name}: description should clearly explain when the skill triggers")

    yaml_errors, yaml_warnings = check_openai_yaml(skill_dir / "agents" / "openai.yaml", name)
    errors.extend(yaml_errors)
    warnings.extend(yaml_warnings)

    if PLACEHOLDER_RE.search(text):
        warnings.append(f"{name}: SKILL.md may contain placeholder text")

    line_count = len(text.splitlines())
    if line_count > 500:
        warnings.append(f"{name}: SKILL.md is long ({line_count} lines); move detail to references")

    trigger_section = re.search(rf"## {re.escape(name)}\n(?P<body>.*?)(?:\n## |\Z)", trigger_text, re.S)
    if not trigger_section:
        errors.append(f"{name}: missing trigger test section")
    else:
        body = trigger_section.group("body")
        if "Should trigger:" not in body:
            errors.append(f"{name}: trigger tests missing Should trigger")
        if "Should not trigger:" not in body:
            errors.append(f"{name}: trigger tests missing Should not trigger")

    text_suffixes = {".md", ".py", ".yaml", ".yml", ".ps1", ".json", ".txt"}
    for path in skill_dir.rglob("*"):
        if path.is_file() and path.suffix.lower() in text_suffixes:
            errors.extend(f"{name}: {error}" for error in check_text_file(path, skill_dir))

    return errors, warnings


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if not SKILLS_DIR.exists():
        print(f"missing skills directory: {SKILLS_DIR}")
        return 1

    trigger_text = ""
    if TRIGGER_TESTS.exists():
        trigger_text = TRIGGER_TESTS.read_text(encoding="utf-8")
        errors.extend(check_text_file(TRIGGER_TESTS, ROOT))
    else:
        errors.append("skills/TRIGGER_TESTS.md is missing")

    for skill_dir in sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir()):
        skill_errors, skill_warnings = audit_skill(skill_dir, trigger_text)
        errors.extend(skill_errors)
        warnings.extend(skill_warnings)

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")

    if errors:
        print("Skill audit failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Skill audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
