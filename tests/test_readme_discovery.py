"""Visitor-facing README checks: accurate navigation, honest evidence, no dead paths."""
from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = ("README.md", "README_EN.md", "skills/CHOOSING.md")


def local_targets(markdown_path: Path):
    text = markdown_path.read_text(encoding="utf-8")
    # All authored navigation links use simple Markdown paths; URL and anchors are external.
    for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text):
        path = target.split("#", 1)[0]
        if not path or path.startswith(("https://", "http://", "mailto:")):
            continue
        yield (markdown_path.parent / path).resolve(), target


class VisitorReadmeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((ROOT / "skills/catalog.json").read_text(encoding="utf-8"))
        cls.entries = cls.catalog["entries"]

    def test_all_relative_navigation_links_resolve(self):
        missing = []
        for relative in FILES:
            for target, raw in local_targets(ROOT / relative):
                if not target.is_relative_to(ROOT) or not target.exists():
                    missing.append(f"{relative}: {raw}")
        self.assertEqual(missing, [])

    def test_readme_pages_make_every_core_discoverable(self):
        core = [x["name"] for x in self.entries if x["tier"] == "core"]
        self.assertEqual(len(core), 5)
        for relative in ("README.md", "README_EN.md"):
            text = (ROOT / relative).read_text(encoding="utf-8")
            for name in core:
                with self.subTest(readme=relative, skill=name):
                    self.assertIn(f"skills/{name}/SKILL.md", text)

    def test_directory_covers_all_known_entries(self):
        guide = (ROOT / "skills/CHOOSING.md").read_text(encoding="utf-8")
        for entry in self.entries:
            with self.subTest(skill=entry["name"]):
                self.assertIn(f"({entry['name']}/SKILL.md)", guide)

    def test_quality_claims_distinguish_static_from_live(self):
        zh = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        self.assertIn("尚未取得可信的模型对照结果", zh)
        self.assertIn("Not measured yet", en)
        self.assertIn("GitHub Actions", zh)
        self.assertIn("GitHub Actions", en)
        count = sum(1 for line in (ROOT / "evals/cases.jsonl").read_text(encoding="utf-8").splitlines()
                    if line.strip() and not line.lstrip().startswith("#"))
        self.assertIn(f"{count} 条", zh)
        self.assertIn(f"{count} labeled", en)

    def test_no_lab_is_presented_as_ready_core(self):
        directory = (ROOT / "skills/CHOOSING.md").read_text(encoding="utf-8")
        self.assertIn("Lab 不代表", directory)
        for relative in ("README.md", "README_EN.md"):
            text = (ROOT / relative).read_text(encoding="utf-8")
            self.assertIn("catalog.json", text)
            self.assertIn("skill.zip", text)


if __name__ == "__main__":
    unittest.main()
