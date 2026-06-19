#!/usr/bin/env python3
"""Strict read-only audit for this personal skills repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
TRIGGER_TESTS = SKILLS_DIR / "TRIGGER_TESTS.md"

NAME_RE = re.compile(r"^[a-z0-9-]+$")
BAD_TEXT_RE = re.compile(r"\ufffd|[\u3400-\u9fff\uf900-\ufaff]")
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
    if BAD_TEXT_RE.search(text):
        errors.append(f"{rel}: contains replacement characters, CJK text, or mojibake")
    if SECRET_RE.search(text):
        errors.append(f"{rel}: may contain a real secret")
    return errors


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
    elif not description.startswith("Use when"):
        errors.append(f"{name}: description should start with 'Use when'")

    openai_yaml = skill_dir / "agents" / "openai.yaml"
    if not openai_yaml.exists():
        errors.append(f"{name}: missing agents/openai.yaml")
    else:
        yaml_text = openai_yaml.read_text(encoding="utf-8")
        for field in ["display_name:", "short_description:", "default_prompt:"]:
            if field not in yaml_text:
                errors.append(f"{name}: agents/openai.yaml missing {field}")

    if PLACEHOLDER_RE.search(text):
        warnings.append(f"{name}: SKILL.md may contain placeholder text")

    word_count = len(re.findall(r"\S+", text))
    if word_count > 900:
        warnings.append(f"{name}: SKILL.md is long ({word_count} words); consider moving detail to references")

    trigger_section = re.search(rf"## {re.escape(name)}\n(?P<body>.*?)(?:\n## |\Z)", trigger_text, re.S)
    if not trigger_section:
        errors.append(f"{name}: missing trigger test section")
    else:
        body = trigger_section.group("body")
        if "Should trigger:" not in body:
            errors.append(f"{name}: trigger tests missing Should trigger")
        if "Should not trigger:" not in body:
            errors.append(f"{name}: trigger tests missing Should not trigger")

    for path in skill_dir.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".md", ".py", ".yaml", ".yml"}:
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
