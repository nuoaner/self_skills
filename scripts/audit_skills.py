#!/usr/bin/env python3
"""Read-only audit for this personal skills repository."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
TRIGGER_TESTS = SKILLS_DIR / "TRIGGER_TESTS.md"
CHANGELOG = SKILLS_DIR / "CHANGELOG.md"
ROOT_README = ROOT / "README.md"

NAME_RE = re.compile(r"^[a-z0-9-]+$")
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")
REPLACEMENT_CHAR_RE = re.compile(r"\ufffd")
COMMON_MOJIBAKE_RE = re.compile(r"(?:Ã.|Â.|â€|â€™|â€œ|â€\x9d|ï»¿)")
SECRET_RE = re.compile(
    r"sk-[A-Za-z0-9]{20,}|api[_-]?key\s*[:=]|password\s*[:=]|secret\s*[:=]|token\s*[:=]",
    re.I,
)
PLACEHOLDER_RE = re.compile(r"\bTODO\b|FIXME", re.I)
TEXT_SUFFIXES = {".md", ".py", ".yaml", ".yml", ".ps1", ".json", ".txt"}


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


def check_version(skill_dir: Path) -> tuple[str | None, list[str]]:
    path = skill_dir / "VERSION"
    if not path.exists():
        return None, [f"{skill_dir.name}: missing VERSION"]

    version = path.read_text(encoding="utf-8").strip()
    if not VERSION_RE.fullmatch(version):
        return version or None, [f"{skill_dir.name}: invalid VERSION '{version}'"]
    return version, []


def check_resource_usage(skill_dir: Path, skill_text: str, root_readme_text: str) -> list[str]:
    warnings: list[str] = []

    references_dir = skill_dir / "references"
    if references_dir.exists():
        for path in sorted(p for p in references_dir.rglob("*") if p.is_file()):
            rel = path.relative_to(skill_dir).as_posix()
            if rel not in skill_text:
                warnings.append(f"{skill_dir.name}: reference is not linked from SKILL.md: {rel}")

    scripts_dir = skill_dir / "scripts"
    if scripts_dir.exists():
        for path in sorted(p for p in scripts_dir.rglob("*") if p.is_file()):
            rel = path.relative_to(skill_dir).as_posix()
            is_maintenance_check = path.suffix.lower() == ".py" and path.name.startswith("check_")
            if is_maintenance_check and "scripts/check_*.py" in root_readme_text:
                continue
            if rel not in skill_text:
                warnings.append(f"{skill_dir.name}: script is not documented in SKILL.md: {rel}")

    return warnings


def audit_skill(
    skill_dir: Path,
    trigger_text: str,
    root_readme_text: str,
) -> tuple[str | None, list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    name = skill_dir.name

    if not NAME_RE.match(name):
        errors.append(f"{name}: folder name must use lowercase letters, digits, and hyphens")

    version, version_errors = check_version(skill_dir)
    errors.extend(version_errors)

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        errors.append(f"{name}: missing SKILL.md")
        return version, errors, warnings

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

    warnings.extend(check_resource_usage(skill_dir, text, root_readme_text))

    for path in skill_dir.rglob("*"):
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            errors.extend(f"{name}: {error}" for error in check_text_file(path, skill_dir))

    return version, errors, warnings


def print_version_summary(versions: dict[str, str]) -> None:
    counts = Counter(versions.values())
    if len(counts) == 1:
        version, count = next(iter(counts.items()))
        print(f"Version baseline: {version} ({count} skills)")
        return

    print("Versions:")
    for name, version in sorted(versions.items()):
        print(f"- {name}: {version}")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    versions: dict[str, str] = {}

    if not SKILLS_DIR.exists():
        print(f"missing skills directory: {SKILLS_DIR}")
        return 1

    if not CHANGELOG.exists():
        errors.append("skills/CHANGELOG.md is missing")

    root_readme_text = ROOT_README.read_text(encoding="utf-8") if ROOT_README.exists() else ""

    trigger_text = ""
    if TRIGGER_TESTS.exists():
        trigger_text = TRIGGER_TESTS.read_text(encoding="utf-8")
        errors.extend(check_text_file(TRIGGER_TESTS, ROOT))
    else:
        errors.append("skills/TRIGGER_TESTS.md is missing")

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    print(f"Skills discovered: {len(skill_dirs)}")

    for skill_dir in skill_dirs:
        version, skill_errors, skill_warnings = audit_skill(skill_dir, trigger_text, root_readme_text)
        if version is not None:
            versions[skill_dir.name] = version
        errors.extend(skill_errors)
        warnings.extend(skill_warnings)

    if versions:
        print_version_summary(versions)

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
