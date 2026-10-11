"""Deterministic unit tests for the catalog and reporting tools."""
from __future__ import annotations
import json
import tempfile
import unittest
from pathlib import Path
from scripts import catalog, eval_cases


def fixture(root: Path, tier: str = 'core') -> None:
    name = 'test-core'
    dir = root / 'skills' / name
    dir.mkdir(parents=True)
    (dir / 'SKILL.md').write_text('---\nname: test-core\ndescription: Verify a tiny workflow.\n---\n\nDetails.\n', encoding='utf-8')
    (dir / 'agents').mkdir()
    (dir / 'agents' / 'openai.yaml').write_text('interface:\n  display_name: Test Core\n', encoding='utf-8')
    (dir / 'VERSION').write_text('1.0.0\n', encoding='utf-8')
    items = [{'name':name,'tier':tier,'action':'retain','rationale':'A reusable test case','agent_evidence':'not_measured'}]
    (root / 'skills' / 'catalog.json').write_text(json.dumps({'schema_version':1,'entries':items})+'\n',encoding='utf-8')


class CatalogTests(unittest.TestCase):
    def test_core_valid(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            fixture(root)
            data, issues = catalog.validate(root)
            self.assertFalse(issues)
            self.assertIn('Core: **1**', catalog.render(data))

    def test_missing_frontmatter_rejected_for_core(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            fixture(root)
            (root / 'skills/test-core/SKILL.md').write_text('Only a sketch',encoding='utf-8')
            _, issues = catalog.validate(root)
            self.assertTrue(any('frontmatter' in x for x in issues))

    def test_missing_frontmatter_allowed_for_lab(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            fixture(root, tier='lab')
            (root / 'skills/test-core/SKILL.md').write_text('Only a sketch',encoding='utf-8')
            _, issues = catalog.validate(root)
            self.assertFalse(issues)

    def test_duplicate_catalog_entry_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            fixture(root)
            path = root / 'skills/catalog.json'
            obj = json.loads(path.read_text())
            obj['entries'].append(obj['entries'][0].copy())
            path.write_text(json.dumps(obj),encoding='utf-8')
            _, issues = catalog.validate(root)
            self.assertTrue(any('duplicate' in x for x in issues))

    def test_catalog_missing_directory_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            fixture(root)
            path = root / 'skills/catalog.json'
            obj = json.loads(path.read_text())
            obj['entries'][0]['name'] = 'missing-other'
            path.write_text(json.dumps(obj),encoding='utf-8')
            _, issues = catalog.validate(root)
            self.assertTrue(any('no directory' in x or 'SKILL.md missing' in x for x in issues))


class EvaluationCasesTests(unittest.TestCase):
    def create_case_root(self, root: Path):
        fixture(root)
        folder = root / 'evals'
        folder.mkdir()
        rows = []
        for i,kind in enumerate(('positive','positive','negative','negative','task'),1):
            rows.append({'id':f'case-{i}','skill':'test-core','kind':kind,'prompt':'User task',
                         'acceptance':'Concrete outcome','should_trigger':kind!='negative'})
        (folder/'cases.jsonl').write_text('\n'.join(json.dumps(row) for row in rows)+'\n',encoding='utf-8')
        return rows

    def test_valid_cases(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.create_case_root(root)
            cases, issues = eval_cases.validate_cases(root)
            self.assertFalse(issues)
            self.assertEqual(len(cases), 5)

    def test_reject_mislabeled_trigger(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            rows=self.create_case_root(root)
            rows[2]['should_trigger']=True
            (root/'evals/cases.jsonl').write_text('\n'.join(json.dumps(row) for row in rows)+'\n',encoding='utf-8')
            _,issues=eval_cases.validate_cases(root)
            self.assertTrue(any('should_trigger mismatch' in x for x in issues))

    def test_report_requires_trace_and_shows_incomplete_coverage(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.create_case_root(root)
            cases,_=eval_cases.validate_cases(root)
            base = {'case_id':'case-1','arm':'A','run_id':'one','triggered':False,'success':True,
                    'tool_calls':1,'duration_s':1.0,'confirmations':0,'safety_violations':0}
            _,issues=eval_cases.summarize_results(cases,[base])
            self.assertTrue(any('evidence' in x for x in issues))
            base['evidence']='sanitized/test-trace'
            result,issues=eval_cases.summarize_results(cases,[base])
            self.assertFalse(issues)
            self.assertIn('Incomplete A/B/C coverage',result)
            self.assertIn('not_applicable_no_skill',result)

if __name__ == '__main__':
    unittest.main()
