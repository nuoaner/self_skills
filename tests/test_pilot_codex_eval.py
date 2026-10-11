"""Safety and no-cost preflight checks for the opt-in Codex pilot."""
from __future__ import annotations

import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import pilot_codex_eval


class PilotRunnerTests(unittest.TestCase):
    def test_plan_has_three_arms_without_running_a_model(self):
        case = pilot_codex_eval.find_case("project-prompt-polisher-05")
        plan = pilot_codex_eval.preview(case, "model-for-test", 2)
        self.assertEqual(plan["arms"], ["A", "B", "C"])
        self.assertEqual(plan["billable_runs_if_executed"], 6)
        self.assertIn("DISABLED", plan["execution"])

    def test_default_plan_does_not_touch_private_output(self):
        with tempfile.TemporaryDirectory() as d:
            requested = Path(d) / "not-created"
            out = io.StringIO()
            with patch.object(sys, "argv", [
                "pilot_codex_eval.py", "plan", "--case", "internal-project-doc-standardizer-05"
            ]), contextlib.redirect_stdout(out):
                self.assertEqual(pilot_codex_eval.main(), 0)
            self.assertFalse(requested.exists())
            self.assertIn("billable_runs_if_executed", out.getvalue())

    def test_running_without_explicit_cost_confirmation_is_rejected(self):
        with patch.object(sys, "argv", [
            "pilot_codex_eval.py", "run", "--model", "test-model"
        ]), contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as raised:
                pilot_codex_eval.main()
        self.assertEqual(raised.exception.code, 2)

    def test_env_does_not_forward_arbitrary_project_secrets(self):
        with patch.dict(os.environ, {
            "OPENAI_API_KEY": "unit-test-placeholder",
            "PROJECT_PRIVATE_PASSWORD": "do-not-forward",
            "PATH": os.environ.get("PATH", ""),
        }):
            env = pilot_codex_eval.model_env(Path("/tmp/fake-codex-home"))
        self.assertNotIn("PROJECT_PRIVATE_PASSWORD", env)
        self.assertEqual(env["CODEX_HOME"], "/tmp/fake-codex-home")
        self.assertIn("OPENAI_API_KEY", env)

    def test_read_only_policy_is_explicit(self):
        source = Path(pilot_codex_eval.__file__).read_text(encoding="utf-8")
        self.assertIn('"--sandbox", "read-only"', source)
        self.assertIn('"--skip-git-repo-check"', source)
        self.assertNotIn("--dangerously-bypass-approvals-and-sandbox", source)


if __name__ == "__main__":
    unittest.main()
