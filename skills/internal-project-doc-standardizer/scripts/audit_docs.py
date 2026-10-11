#!/usr/bin/env python3
"""Read-only documentation audit with proportionate lean and full profiles."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

FULL_FILES = [
    'README.md', 'agent.md', 'docs/standard.md', 'docs/requirements.md',
    'docs/architecture.md', 'docs/api.md', 'docs/database.md',
    'docs/deploy.md', 'docs/test.md', 'docs/changelog.md',
]
FULL_SECTIONS = {
    'Project Basic Information': ('project basic information', '\u57fa\u672c\u4fe1\u606f'),
    'Project Overview': ('project overview', '\u9879\u76ee\u6982\u8ff0', '\u9879\u76ee\u4ecb\u7ecd'),
    'Quick Start': ('quick start', 'getting started', '\u5feb\u901f\u5f00\u59cb', '\u8fd0\u884c\u6307\u5357'),
    'Project Structure': ('project structure', '\u9879\u76ee\u7ed3\u6784', '\u76ee\u5f55\u7ed3\u6784'),
    'Current Progress': ('current progress', '\u5f53\u524d\u8fdb\u5ea6', '\u5f00\u53d1\u8fdb\u5ea6'),
    'Documentation Index': ('documentation index', '\u6587\u6863\u7d22\u5f15', '\u6587\u6863\u76ee\u5f55'),
    'Known Issues': ('known issues', '\u5df2\u77e5\u95ee\u9898'),
    'Next Steps': ('next steps', '\u540e\u7eed\u8ba1\u5212', '\u4e0b\u4e00\u6b65'),
    'AI / Agent Usage Prompt': ('ai / agent usage prompt', 'agent usage', '\u667a\u80fd\u4f53\u4f7f\u7528\u8bf4\u660e'),
}
BAD_GENERIC = {'done', 'doing', 'not-started', 'finished', 'todo'}
SECRET = re.compile(r'(?i)(api[_-]?key|secret|token|password|passwd|private[_-]?key)\s*[:=]\s*[\'\"]?[^\s\'\"<>]+')
PRIVATE_KEY = re.compile(r'-----BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY-----')


def read_text(path: Path) -> str:
    return path.read_text(encoding='utf-8-sig')


def status_values(text: str) -> list[str]:
    """Read only cells under a recognizable status header, not arbitrary text."""
    values = []
    lines = text.splitlines()
    for i, line in enumerate(lines[:-2]):
        if '|' not in line or '|' not in lines[i + 1] or not re.search(r'[-]{3,}', lines[i + 1]):
            continue
        headers = [x.strip().lower() for x in line.strip('|').split('|')]
        index = [n for n, h in enumerate(headers) if h.endswith('status') or '\u72b6\u6001' in h]
        if not index:
            continue
        for data in lines[i + 2:]:
            if '|' not in data:
                break
            cells = [x.strip(' `').lower() for x in data.strip('|').split('|')]
            values.extend(cells[n] for n in index if n < len(cells) and cells[n])
    return values


def audit(root: Path, profile: str = 'full') -> dict:
    if profile not in {'full', 'lean'}:
        raise ValueError('profile must be full or lean')
    required = FULL_FILES if profile == 'full' else ['README.md']
    result = {'root': str(root), 'profile': profile, 'missing_files': [],
              'readme_missing_sections': [], 'placeholder_counts': {},
              'secret_risks': [], 'encoding_risks': [], 'status_notes': []}
    for name in required:
        if not (root / name).is_file():
            result['missing_files'].append(name)
    readme = root / 'README.md'
    if readme.is_file() and profile == 'full':
        try:
            text = read_text(readme).lower()
            for section, aliases in FULL_SECTIONS.items():
                if not any(alias.lower() in text for alias in aliases):
                    result['readme_missing_sections'].append(section)
        except UnicodeError:
            result['encoding_risks'].append('README.md')
    for name in FULL_FILES:
        file = root / name
        if not file.is_file():
            continue
        try:
            text = read_text(file)
        except UnicodeError:
            result['encoding_risks'].append(name)
            continue
        if 'TBD' in text:
            result['placeholder_counts'][name] = text.count('TBD')
        if SECRET.search(text) or PRIVATE_KEY.search(text):
            result['secret_risks'].append(name)
        suspicious = sorted(set(value for value in status_values(text) if value in BAD_GENERIC))
        if suspicious:
            result['status_notes'].append({'file': name, 'values': suspicious})
    result['ok'] = not any(result[k] for k in
                           ('missing_files', 'readme_missing_sections', 'secret_risks',
                            'encoding_risks', 'status_notes'))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description='Read-only documentation audit')
    parser.add_argument('project_root', type=Path)
    parser.add_argument('--profile', choices=['lean','full'], default='full')
    args = parser.parse_args()
    root = args.project_root.expanduser().resolve()
    if not root.is_dir():
        parser.error(f'project root not found: {root}')
    result = audit(root, profile=args.profile)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['ok'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
