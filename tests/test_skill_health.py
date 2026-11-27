import tempfile
import unittest
from pathlib import Path

from skill_health import eval_coverage, local_links, parse_frontmatter


class SkillHealthTests(unittest.TestCase):
    def test_frontmatter_reads_name_and_description(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "SKILL.md"
            path.write_text("---\\nname: demo-skill\\ndescription: A demo skill\\n---\\n# Demo\\n", encoding="utf-8")
            self.assertEqual(parse_frontmatter(path), {"name": "demo-skill", "description": "A demo skill"})

    def test_local_links_ignores_external_and_anchors(self):
        markdown = "[ref](references/guide.md) [web](https://example.com) [section](#top)"
        self.assertEqual(local_links(markdown), ["references/guide.md"])

    def test_eval_coverage_counts_case_kinds(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "cases.jsonl"
            path.write_text(
                '{"skill":"demo","kind":"positive"}\\n'
                '{"skill":"demo","kind":"negative"}\\n'
                '{"skill":"demo","kind":"task"}\\n',
                encoding="utf-8",
            )
            counts, errors = eval_coverage(path)
            self.assertFalse(errors)
            self.assertEqual(counts["demo"]["positive"], 1)
            self.assertEqual(counts["demo"]["negative"], 1)
            self.assertEqual(counts["demo"]["task"], 1)


if __name__ == "__main__":
    unittest.main()
