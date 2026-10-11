"""Audit profile and status-column regression tests (no project writes)."""
from __future__ import annotations
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/internal-project-doc-standardizer/scripts/audit_docs.py'

class DocumentationProfileTests(unittest.TestCase):
    def run_audit(self, root: Path, profile: str):
        proc = subprocess.run([sys.executable, str(SCRIPT), str(root), '--profile', profile],
                              capture_output=True, text=True, timeout=10)
        return proc.returncode, json.loads(proc.stdout)

    def test_lean_accepts_small_readme_full_requires_template(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d)
            (path/'README.md').write_text('# Small project\n\nQuick start\n',encoding='utf-8')
            rc, result = self.run_audit(path,'lean')
            self.assertEqual(rc,0)
            self.assertTrue(result['ok'])
            rc, result = self.run_audit(path,'full')
            self.assertEqual(rc,1)
            self.assertIn('docs/api.md', result['missing_files'])

    def test_unrelated_table_value_done_is_not_a_status(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d)
            (path/'README.md').write_text('# Example\n\n| Phase | Description |\n| --- | --- |\n| done | important |\n',encoding='utf-8')
            rc, result = self.run_audit(path,'lean')
            self.assertEqual(rc,0)
            self.assertFalse(result['status_notes'])

    def test_status_column_done_is_flagged(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d)
            (path/'README.md').write_text('# Example\n\n| Feature | Status |\n| --- | --- |\n| Login | done |\n',encoding='utf-8')
            rc, result = self.run_audit(path,'lean')
            self.assertEqual(rc,1)
            self.assertIn('done',result['status_notes'][0]['values'])

    def test_obvious_secret_is_reported(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d)
            (path/'README.md').write_text('# Example\npassword=actual-demo-secret\n',encoding='utf-8')
            rc, result = self.run_audit(path,'lean')
            self.assertEqual(rc,1)
            self.assertIn('README.md',result['secret_risks'])

if __name__ == '__main__':
    unittest.main()
