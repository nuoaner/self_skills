import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import dependency_watch as watcher


class DependencyWatchTests(unittest.TestCase):
    def test_registry_rejects_non_https_and_unallowlisted_hosts(self):
        registry = {
            "schema_version": 1,
            "watch_items": [{
                "id": "bad", "url": "http://example.com/spec",
                "allowed_hosts": ["example.com"], "checks": [],
            }],
        }
        self.assertTrue(watcher.validate_registry(registry))

    def test_public_url_rejects_loopback_ip(self):
        with self.assertRaises(ValueError):
            watcher.safe_public_url("https://127.0.0.1/spec", {"127.0.0.1"})

    def test_inventory_finds_python_package_imports(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill = root / "skills" / "pptx-check"
            (skill / "scripts").mkdir(parents=True)
            (skill / "SKILL.md").write_text("---\nname: pptx-check\ndescription: Check PPTX files.\n---\n", encoding="utf-8")
            (skill / "scripts" / "check.py").write_text("import json\nimport pptx\n", encoding="utf-8")
            (root / "skills" / "catalog.json").write_text(json.dumps({
                "entries": [{
                    "name": "pptx-check", "tier": "lab", "action": "retain",
                    "rationale": "test", "agent_evidence": "not_measured",
                }]
            }), encoding="utf-8")
            inventory = watcher.scan_inventory(root)
            self.assertIn("python-pptx", inventory["skills"][0]["runtime_packages"])
            self.assertNotIn("json", inventory["skills"][0]["runtime_packages"])

    def test_command_dependency_scan_detects_pip_and_npm(self):
        found = watcher.command_dependencies("pip install pillow\nnpm i -D playwright-core")
        self.assertIn("pillow", found)
        self.assertIn("playwright-core", found)

    def test_missing_contract_pattern_requires_review(self):
        registry = {
            "schema_version": 1,
            "watch_items": [{
                "id": "spec", "url": "https://docs.example.org/spec",
                "allowed_hosts": ["docs.example.org"], "kind": "tool_interface",
                "checks": [{"label": "required field", "pattern": "required-field-that-is-absent"}],
            }],
        }
        with mock.patch.object(watcher, "fetch_source", return_value=("This is the spec.", "abc123", 200)):
            result = watcher.check_sources(registry)
        self.assertEqual(result["status"], "review_required")
        self.assertEqual(result["results"][0]["missing_checks"], ["required field"])

    def test_repository_watch_registry_is_valid(self):
        registry_path = Path(__file__).resolve().parents[1] / "docs" / "dependency-watch.json"
        if registry_path.is_file():
            registry = json.loads(registry_path.read_text(encoding="utf-8"))
            self.assertEqual(watcher.validate_registry(registry), [])


if __name__ == "__main__":
    unittest.main()
