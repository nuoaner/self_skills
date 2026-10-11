#!/usr/bin/env python3
"""Context-aware, read-only repository handoff review."""
from __future__ import annotations
import argparse
from pathlib import Path

def review(root: Path) -> list[tuple[str,str]]:
    findings = []
    readmes = [p for p in root.iterdir() if p.is_file() and p.name.lower().startswith("readme")]
    if not readmes:
        findings.append(("HIGH","Root README is missing"))
    elif not any(p.read_text(encoding="utf-8-sig", errors="replace").strip() for p in readmes):
        findings.append(("HIGH","Root README is empty"))
    return findings

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_root")
    args = parser.parse_args()
    root = Path(args.project_root).expanduser().resolve()
    if not root.is_dir():
        parser.error(f"project root not found: {root}")
    issues = review(root)
    print("# Project Structure Review")
    print(f"Project: {root}")
    for severity, issue in issues:
        print(f"- [{severity}] {issue}")
    if not issues:
        print("No basic handoff issues found; this is not a full architecture audit.")
    return int(any(level == "HIGH" for level, _ in issues))

if __name__ == "__main__":
    raise SystemExit(main())
