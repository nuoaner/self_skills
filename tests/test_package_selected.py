"""Core packaging tests never upload or install skills."""
from __future__ import annotations
import json
import tempfile
import unittest
import zipfile
from pathlib import Path
from scripts import package_selected


def fake_repo(root: Path, tier: str='core') -> None:
    skill = root/'skills'/'demo-skill'
    (skill/'agents').mkdir(parents=True)
    (skill/'references').mkdir()
    (skill/'SKILL.md').write_text('---\nname: demo-skill\ndescription: Test demo\n---\nBody',encoding='utf-8')
    (skill/'VERSION').write_text('1.0.0',encoding='utf-8')
    (skill/'agents/openai.yaml').write_text('interface:\n  display_name: Demo\n',encoding='utf-8')
    (skill/'references/detail.md').write_text('Background',encoding='utf-8')
    (root/'skills/catalog.json').write_text(json.dumps({'schema_version':1,'entries':[
        {'name':'demo-skill','tier':tier,'action':'retain','rationale':'For controlled testing','agent_evidence':'not_measured'}
    ]}),encoding='utf-8')


class PackagingTests(unittest.TestCase):
    def test_core_zip_contains_one_top_level_skill(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            fake_repo(root)
            zip_path=root/'exports'/'skill.zip'
            count,size=package_selected.package(root,'demo-skill',zip_path)
            self.assertEqual(count,4)
            self.assertGreater(size,0)
            with zipfile.ZipFile(zip_path) as z:
                paths=z.namelist()
                self.assertTrue(all(x.startswith('demo-skill/') for x in paths))
                self.assertIn('demo-skill/SKILL.md',paths)
                self.assertIn('demo-skill/references/detail.md',paths)

    def test_lab_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            fake_repo(root,tier='lab')
            with self.assertRaises(ValueError):
                package_selected.package(root,'demo-skill',root/'skill.zip')

    def test_refuses_existing_output(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            fake_repo(root)
            out=root/'skill.zip'
            out.write_text('important existing file',encoding='utf-8')
            with self.assertRaises(FileExistsError):
                package_selected.package(root,'demo-skill',out)
            self.assertEqual(out.read_text(), 'important existing file')

    def test_symlink_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            fake_repo(root)
            target=root/'README.md'
            target.write_text('private',encoding='utf-8')
            (root/'skills/demo-skill/assets').mkdir()
            (root/'skills/demo-skill/assets/secret').symlink_to(target)
            with self.assertRaises(ValueError):
                package_selected.package(root,'demo-skill',root/'skill.zip')

if __name__ == '__main__':
    unittest.main()
