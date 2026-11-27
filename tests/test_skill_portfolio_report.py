import csv
import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import skill_portfolio_report as portfolio


class PortfolioReportTests(unittest.TestCase):
    def test_tokenizer_handles_english_and_chinese(self):
        tokens = portfolio.tokenize("机器人 PowerPoint 演示文稿")
        self.assertIn("zh:机器", tokens)
        self.assertIn("en:powerpoint", tokens)

    def test_identical_documents_have_full_cosine_similarity(self):
        document = portfolio.tokenize("PowerPoint presentation engineering quality")
        scores, _ = portfolio.cosine_tfidf({"one": document, "two": document.copy()})
        self.assertAlmostEqual(scores[("one", "two")], 1.0, places=6)

    def test_usage_recommendation_does_not_overreact_to_small_sample(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "usage.csv"
            fields = ["date", "skill", "task_completed", "benefit_over_no_skill", "quality_score", "friction_category", "safety_violations"]
            with path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                for day in ("2026-11-01", "2026-11-02"):
                    writer.writerow({
                        "date": day, "skill": "demo", "task_completed": "yes",
                        "benefit_over_no_skill": "better", "quality_score": "5",
                        "friction_category": "none", "safety_violations": "0",
                    })
            summaries, warnings = portfolio.load_usage(path, {"demo"})
            self.assertFalse(warnings)
            self.assertEqual(summaries["demo"]["records"], 2)
            self.assertIn("Sample too small", summaries["demo"]["recommendation"])

    def test_missing_usage_is_unknown_not_zero(self):
        with tempfile.TemporaryDirectory() as tmp:
            summaries, warnings = portfolio.load_usage(Path(tmp) / "missing.csv", {"demo"})
            self.assertEqual(summaries, {})
            self.assertTrue(any("unavailable" in item for item in warnings))

    def test_explicit_review_date_controls_freshness(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill_dir = root / "skills" / "demo"
            skill_dir.mkdir(parents=True)
            (skill_dir / "manifest.json").write_text(
                json.dumps({"last_reviewed": "2026-01-01", "review_cadence": "monthly"}),
                encoding="utf-8",
            )
            result = portfolio.review_status(
                root, {"name": "demo", "tier": "lab"}, date(2026, 11, 27)
            )
            self.assertEqual(result["status"], "overdue")
            self.assertEqual(result["date_source"], "last_reviewed")

    def test_declared_complement_is_not_reported_as_duplicate(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "skills").mkdir()
            (root / "docs").mkdir()
            (root / "evals").mkdir()
            entries = []
            for name in ("course-deck", "pptx-engine"):
                folder = root / "skills" / name
                folder.mkdir()
                (folder / "SKILL.md").write_text(
                    f"---\nname: {name}\ndescription: PowerPoint presentation engineering and delivery QA.\n---\n# PowerPoint presentation engineering\nReview PPTX structure and presentation delivery.\n",
                    encoding="utf-8",
                )
                entries.append({"name": name, "tier": "lab", "action": "strengthen", "rationale": "test", "agent_evidence": "not_measured"})
            (root / "skills" / "catalog.json").write_text(json.dumps({"entries": entries}), encoding="utf-8")
            (root / "docs" / "skill-relations.json").write_text(json.dumps({
                "schema_version": 1,
                "relations": [{
                    "skills": ["course-deck", "pptx-engine"],
                    "type": "complements",
                    "reason": "authoring and QA are separate responsibilities",
                }],
            }), encoding="utf-8")
            report = portfolio.build_report(
                root, date(2026, 11, 27), root / "evals" / "usage-log.csv",
                root / "docs" / "skill-relations.json", threshold=0.99,
            )
            self.assertEqual(report["overlap_candidates"], [])
            self.assertEqual(len(report["declared_relationships"]), 1)
            self.assertEqual(report["declared_relationships"][0]["relation"], "complements")


if __name__ == "__main__":
    unittest.main()
