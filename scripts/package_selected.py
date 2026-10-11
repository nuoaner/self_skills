#!/usr/bin/env python3
"""Package exactly one validated Core skill for explicit ChatGPT upload.

This does not install or upload anything. Lab and Reference are excluded.
"""
from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path

try:
    from .catalog import validate
except ImportError:  # direct execution as scripts/package_selected.py
    from catalog import validate

ROOT = Path(__file__).resolve().parents[1]
MAX_ZIP_SIZE = 25 * 1024 * 1024  # conservative ChatGPT skill-creator limit
EXCLUDE = {'__pycache__', '.DS_Store', '.git', '.pytest_cache', 'Thumbs.db'}


def package(root: Path, name: str, output: Path) -> tuple[int, int]:
    catalog, errors = validate(root)
    if errors:
        raise ValueError('Portfolio integrity failed: ' + '; '.join(errors))
    matches = [row for row in catalog['entries'] if row['name'] == name]
    if len(matches) != 1 or matches[0]['tier'] != 'core':
        raise ValueError('Only an explicitly cataloged Core skill may be packaged')
    source = root / 'skills' / name
    if output.exists():
        raise FileExistsError(f'Refusing to overwrite existing output: {output}')
    files = sorted(p for p in source.rglob('*') if p.is_file())
    for path in source.rglob('*'):
        if path.is_symlink():
            raise ValueError(f'Symlink not allowed in published skill: {path}')
    files = [p for p in files if not any(part in EXCLUDE or part.startswith('.env') for part in p.relative_to(source).parts)]
    if not files or not (source / 'SKILL.md') in files:
        raise ValueError('No valid skill manifest to package')
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for path in files:
                relative = path.relative_to(source).as_posix()
                archive.write(path, arcname=f'{name}/{relative}')
        size = output.stat().st_size
        if size > MAX_ZIP_SIZE:
            raise ValueError(f'ZIP exceeds conservative 25 MB limit: {size} bytes')
        with zipfile.ZipFile(output) as archive:
            if archive.testzip() is not None:
                raise ValueError('ZIP CRC integrity check failed')
        return len(files), size
    except Exception:
        output.unlink(missing_ok=True)
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description='Build one Core skill ZIP, without installing it')
    parser.add_argument('skill_name')
    parser.add_argument('--output', type=Path, default=Path('skill.zip'))
    args = parser.parse_args()
    try:
        count, size = package(ROOT, args.skill_name, args.output.expanduser().resolve())
    except (OSError, ValueError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1
    print(f'Created {args.output}: {count} files, {size} bytes; upload and install are separate user actions.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
