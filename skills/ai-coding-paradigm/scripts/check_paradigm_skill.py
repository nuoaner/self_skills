#!/usr/bin/env python3
"""Read-only package integrity check; does not measure agent outcomes."""
from __future__ import annotations
import re
import sys
from pathlib import Path
NAME = "ai-coding-paradigm"
RESOURCES = ["references/paradigm-checklist.md"]
def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    errors = []
    skill = root / "SKILL.md"
    if not skill.is_file():
        errors.append("missing SKILL.md")
    else:
        body = skill.read_text(encoding="utf-8-sig")
        header = re.match(r"\A---\s*\n(.*?)\n---(?:\s*\n|\Z)", body, re.S)
        if not header:
            errors.append("invalid YAML frontmatter")
        else:
            if not re.search(r"(?m)^name:\s*['\"]?" + re.escape(NAME) + r"['\"]?\s*$", header.group(1)):
                errors.append("incorrect skill name")
            if not re.search(r"(?m)^description:\s*\S", header.group(1)):
                errors.append("missing description")
        if "\ufffd" in body:
            errors.append("Unicode replacement character detected")
    for item in RESOURCES:
        if not (root / item).is_file():
            errors.append("missing resource: " + item)
    for issue in errors:
        print("FAIL:", issue)
    if not errors:
        print(NAME + " integrity PASS (not a behavior test)")
    return int(bool(errors))
if __name__ == "__main__":
    raise SystemExit(main())
