#!/usr/bin/env python3
"""Read-only contract regression tests. Run with python -m unittest discover -s tests."""
from __future__ import annotations
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC_AUDIT = ROOT / "skills/internal-project-doc-standardizer/scripts/audit_docs.py"
STRUCTURE = ROOT / "skills/project-structure-review/scripts/review_project.py"
SCOOP = ROOT / "skills/app-to-scoop/scripts/test-manifest.ps1"

class RegressionTests(unittest.TestCase):
    def run_script(self, script: Path, directory: Path):
        return subprocess.run([sys.executable, str(script), str(directory)], capture_output=True, text=True, timeout=12)

    def test_doc_audit_failure_exit_code(self):
        with tempfile.TemporaryDirectory() as d:
            result = self.run_script(DOC_AUDIT, Path(d))
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertFalse(json.loads(result.stdout)["ok"])

    def test_project_review_allows_nested_directories(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "README.md").write_text("A documented repository", encoding="utf-8")
            nested = root / "src" / "domain" / "features" / "deep"
            nested.mkdir(parents=True)
            (nested / "index.ts").write_text("export const x = 1;", encoding="utf-8")
            result = self.run_script(STRUCTURE, root)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertNotIn("nesting", result.stdout.lower())

    def test_project_review_missing_readme_fails(self):
        with tempfile.TemporaryDirectory() as d:
            result = self.run_script(STRUCTURE, Path(d))
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)

    def test_scoop_helper_has_no_implicit_uninstall(self):
        content = SCOOP.read_text(encoding="utf-8")
        self.assertIn("AllowInstall", content)
        self.assertNotIn("$scoop.Source uninstall", content)
        self.assertIn("Read-only", content)

if __name__ == "__main__":
    unittest.main()
