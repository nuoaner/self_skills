#!/usr/bin/env python3
"""Read-only quality check for the wechat-article-image-planner skill."""

from __future__ import annotations

from pathlib import Path
import re
import sys


REQUIRED_SKILL_TERMS = [
    "imagegen2",
    "Article first, images second",
    "Output Contract",
    "IMAGEGEN2_API_KEY",
    "WeChat article image planning",
]

REQUIRED_PLAYBOOK_TERMS = [
    "Article Diagnosis",
    "Visual Anchor Extraction",
    "Prompt Structure",
    "QA Checklist",
]

BAD_TEXT_RE = re.compile(r"\ufffd|[\u3400-\u9fff\uf900-\ufaff]")


def fail(message: str) -> int:
    print(f"FAIL: {message}")
    return 1


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    skill = root / "SKILL.md"
    playbook = root / "references" / "visual-planning-playbook.md"
    agent = root / "agents" / "openai.yaml"

    for path in [skill, playbook, agent]:
        if not path.exists():
            return fail(f"missing {path.relative_to(root)}")

    skill_text = skill.read_text(encoding="utf-8")
    playbook_text = playbook.read_text(encoding="utf-8")
    agent_text = agent.read_text(encoding="utf-8")

    if BAD_TEXT_RE.search(skill_text + playbook_text + agent_text):
        return fail("replacement characters, CJK text, or mojibake remain")
    if "[TODO" in skill_text + playbook_text + agent_text:
        return fail("TODO placeholder remains")
    if not re.search(r"^name: wechat-article-image-planner$", skill_text, re.M):
        return fail("skill name frontmatter is wrong")
    for term in REQUIRED_SKILL_TERMS:
        if term not in skill_text:
            return fail(f"SKILL.md missing required term: {term}")
    for term in REQUIRED_PLAYBOOK_TERMS:
        if term not in playbook_text:
            return fail(f"playbook missing required term: {term}")
    if "Use $wechat-article-image-planner" not in agent_text:
        return fail("openai.yaml default_prompt does not name the skill")

    print("OK: wechat-article-image-planner skill check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
