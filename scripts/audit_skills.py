#!/usr/bin/env python3
"""Read-only audit of core packages and optional lab sketches.

This reports repository structural health, not AI task quality or routing.
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

from catalog import read_frontmatter, validate

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {'.md', '.yaml', '.yml', '.py', '.ps1', '.json', '.txt'}
RESOURCE_LINK = re.compile(r'\]\(((?:references|scripts|assets|examples)/[^)#]+)(?:#[^)]+)?\)')


def audit(root: Path) -> tuple[list[str], list[str]]:
    catalog, errors = validate(root)
    warnings: list[str] = []
    if errors:
        return errors, warnings
    trigger_file = root / 'skills' / 'TRIGGER_TESTS.md'
    trigger_text = trigger_file.read_text(encoding='utf-8') if trigger_file.is_file() else ''
    for entry in catalog['entries']:
        skill_dir = root / 'skills' / entry['name']
        file = skill_dir / 'SKILL.md'
        if entry['tier'] == 'lab' and read_frontmatter(file) is None:
            warnings.append(f"{entry['name']}: prototype lacks frontmatter; do not install as an active skill")
        if entry['tier'] == 'reference':
            continue
        if entry['tier'] == 'core':
            section = re.search(r'^## ' + re.escape(entry['name']) + r'\s*\n(.*?)(?=^## |\Z)', trigger_text, re.M | re.S)
            if not section or 'Should trigger:' not in section.group(1) or 'Should not trigger:' not in section.group(1):
                errors.append(f"{entry['name']}: missing positive or negative trigger specification")
            content = file.read_text(encoding='utf-8')
            for relative in RESOURCE_LINK.findall(content):
                if not (skill_dir / relative).is_file():
                    errors.append(f"{entry['name']}: broken resource link {relative}")
        for path in skill_dir.rglob('*'):
            if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            try:
                content = path.read_text(encoding='utf-8')
            except UnicodeDecodeError:
                errors.append(f"{path.relative_to(root)}: invalid UTF-8")
                continue
            if '\ufffd' in content:
                errors.append(f"{path.relative_to(root)}: Unicode replacement character detected")
    return errors, warnings


def main() -> int:
    root = ROOT
    errors, warnings = audit(root)
    for item in warnings:
        print('INFO:', item)
    for item in errors:
        print('FAIL:', item, file=sys.stderr)
    if errors:
        print(f"Audit failed: {len(errors)} structural issues", file=sys.stderr)
        return 1
    import json
    data = json.loads((root / 'skills' / 'catalog.json').read_text(encoding='utf-8'))
    counts = Counter(x['tier'] for x in data['entries'])
    print(f"PASS: core={counts['core']}, lab={counts['lab']}, reference={counts['reference']}; model behavior not measured")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
