#!/usr/bin/env python3
"""Validate and render this repository's skill portfolio catalog.

Catalog tiers are repository policy, not claims about platform certification or
measured model benefit. No external dependencies or network calls.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TIERS = {"core", "lab", "reference"}
ACTIONS = {"retain", "strengthen", "merge_candidate", "retire_candidate", "index_only"}
FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
FIELD_RE = re.compile(r"(?m)^([a-z][a-z0-9_-]*):\s*(.+?)\s*$")
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def read_frontmatter(skill_file: Path) -> dict[str, str] | None:
    text = skill_file.read_text(encoding="utf-8-sig")
    match = FM_RE.match(text)
    if not match:
        return None
    return {key: value.strip(' "\'') for key, value in FIELD_RE.findall(match.group(1))}


def validate(root: Path) -> tuple[dict, list[str]]:
    errors: list[str] = []
    file = root / "skills" / "catalog.json"
    try:
        catalog = json.loads(file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {}, [f"cannot read catalog: {exc}"]
    entries = catalog.get("entries")
    if not isinstance(entries, list):
        return {}, ["entries must be an array"]
    if catalog.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    found: set[str] = set()
    for index, item in enumerate(entries):
        if not isinstance(item, dict):
            errors.append(f"entry {index} must be an object")
            continue
        name, tier, action = (item.get(k) for k in ("name", "tier", "action"))
        if not isinstance(name, str) or not NAME_RE.fullmatch(name):
            errors.append(f"entry {index} has invalid name: {name}")
            continue
        if name in found:
            errors.append(f"duplicate entry: {name}")
        found.add(name)
        if tier not in TIERS:
            errors.append(f"{name}: unknown tier: {tier}")
        if action not in ACTIONS:
            errors.append(f"{name}: unknown action: {action}")
        if tier == "reference" and action != "index_only":
            errors.append(f"{name}: reference entries must use index_only")
        if tier == "core" and action in {"merge_candidate", "retire_candidate", "index_only"}:
            errors.append(f"{name}: core cannot be marked for merge or retirement")
        if not isinstance(item.get("rationale"), str) or not item["rationale"].strip():
            errors.append(f"{name}: missing rationale")
        if item.get("agent_evidence") not in {"not_measured", "measured"}:
            errors.append(f"{name}: invalid agent_evidence")
        if item.get("agent_evidence") == "measured" and not item.get("evidence_path"):
            errors.append(f"{name}: measured claims require a traceable evidence_path")
        if action == "merge_candidate" and not item.get("successor"):
            errors.append(f"{name}: merge_candidate needs a successor")
        skill = root / "skills" / name / "SKILL.md"
        if not skill.is_file():
            errors.append(f"{name}: SKILL.md missing")
            continue
        try:
            metadata = read_frontmatter(skill)
        except UnicodeError:
            errors.append(f"{name}: SKILL.md not UTF-8")
            continue
        if tier == "core":
            if not metadata:
                errors.append(f"{name}: core skill has no frontmatter")
            else:
                if metadata.get("name") != name:
                    errors.append(f"{name}: frontmatter name mismatch")
                description = metadata.get("description", "")
                if not description or len(description) > 1024:
                    errors.append(f"{name}: description length invalid")
            # Repository release convention. The portable Skill standard does
            # not mandate this UI file or an independent VERSION file.
            agent_file = root / "skills" / name / "agents" / "openai.yaml"
            if not agent_file.is_file():
                errors.append(f"{name}: core is missing ChatGPT UI metadata")
            else:
                content = agent_file.read_text(encoding="utf-8-sig")
                if not re.search(r"(?m)^interface:\s*$", content) or not re.search(r"(?m)^\s+display_name:\s*\S", content):
                    errors.append(f"{name}: interface.display_name missing")
            version = root / "skills" / name / "VERSION"
            if not version.is_file() or not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", version.read_text(encoding="utf-8").strip()):
                errors.append(f"{name}: missing or invalid repository VERSION")
        elif metadata and metadata.get("name") != name:
            errors.append(f"{name}: experimental frontmatter name mismatch")
    physical = {p.name for p in (root / "skills").iterdir() if p.is_dir()}
    errors.extend(f"uncataloged directory: {name}" for name in sorted(physical - found))
    errors.extend(f"catalog entry has no directory: {name}" for name in sorted(found - physical))
    return catalog, errors


def render(data: dict) -> str:
    entries = sorted(data["entries"], key=lambda e: (list(("core", "lab", "reference")).index(e["tier"]), e["name"]))
    counts = Counter(x["tier"] for x in entries)
    lines = ["# Skill Portfolio / Skill 能力清单", "",
             "Generated from `skills/catalog.json`. Edit the catalog, not this file.", "",
             f"- Core: **{counts['core']}** (priority-maintained candidates, not benchmark-certified)",
             f"- Lab: **{counts['lab']}** (opt-in evaluation, including compatibility candidates)",
             f"- Reference: **{counts['reference']}** (not installable as skills)", "",
             "| Tier | Skill | Decision | Evidence | Reason |", "|---|---|---|---|---|"]
    for item in entries:
        name = item["name"]
        rationale = item["rationale"].replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {item['tier']} | [{name}]({name}/SKILL.md) | {item['action']} | {item['agent_evidence']} | {rationale} |")
    lines += ["", "**Reading this catalog:** Tier and action are local maintainers' provisional decisions.",
              "No `agent_evidence: not_measured` entry is claimed to improve model performance.",
              "Lab packages without valid frontmatter are source sketches, not installable skills.",
              "Only release individual, validated skill folders. Never upload this multi-skill tree as one ChatGPT skill.", ""]
    return "\n".join(lines)


def main() -> int:
    p = argparse.ArgumentParser(description="Read-only skill portfolio policy check")
    p.add_argument("command", choices=["check", "list", "sync", "check-docs"])
    p.add_argument("--root", type=Path, default=ROOT)
    args = p.parse_args()
    root = args.root.resolve()
    data, errors = validate(root)
    if errors:
        for error in errors:
            print("ERROR:", error, file=sys.stderr)
        return 1
    if args.command == "list":
        print(render(data))
    elif args.command == "sync":
        (root / "skills" / "CATALOG.md").write_text(render(data), encoding="utf-8")
        print("Updated skills/CATALOG.md from catalog.json")
    elif args.command == "check-docs":
        output = root / "skills" / "CATALOG.md"
        if not output.is_file() or output.read_text(encoding="utf-8") != render(data):
            print("ERROR: skills/CATALOG.md is out of date. Run: python scripts/catalog.py sync", file=sys.stderr)
            return 1
        print("Skill catalog documentation in sync")
    else:
        counts = Counter(entry["tier"] for entry in data["entries"])
        print(f"Catalog valid: {len(data['entries'])} entries (core={counts['core']}, lab={counts['lab']}, reference={counts['reference']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
