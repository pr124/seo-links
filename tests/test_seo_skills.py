import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'seo_skills.py'
spec = importlib.util.spec_from_file_location('seo_skills', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class SkillWorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent)
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        source = self.root / 'vendor/demo/SKILL.md'
        source.parent.mkdir(parents=True)
        source.write_text('upstream workflow\n', encoding='utf-8')
        content = '---\nname: demo-audit\ndescription: "Audit"\n---\nRead vendor/demo/SKILL.md\n'
        for folder in ['.agents/skills', '.claude/skills']:
            path = self.root / folder / 'demo-audit/SKILL.md'
            path.parent.mkdir(parents=True)
            path.write_text(content, encoding='utf-8')
        self.manifest = {
            'agents': {'generic': '.agents/skills', 'claude': '.claude/skills'},
            'skills': [{'id': 'demo-audit', 'local_path': 'vendor/demo/SKILL.md'}],
            'files': [{'path': 'vendor/demo/SKILL.md', 'git_blob_sha': module.git_hash(source.read_bytes())}],
            'optional_assets': [],
        }

    def test_valid_workspace(self):
        self.assertEqual(module.check(self.root, self.manifest), [])

    def test_changed_vendor_file_is_detected(self):
        (self.root / 'vendor/demo/SKILL.md').write_text('changed', encoding='utf-8')
        self.assertTrue(any('hash' in error for error in module.check(self.root, self.manifest)))

    def test_missing_adapter_is_detected(self):
        (self.root / '.claude/skills/demo-audit/SKILL.md').unlink()
        self.assertTrue(any('missing' in error for error in module.check(self.root, self.manifest)))

    def test_sync_repairs_adapter_without_touching_source(self):
        target = self.root / '.claude/skills/demo-audit/SKILL.md'
        target.unlink()
        module.sync(self.root, self.manifest, ['claude'])
        self.assertEqual(module.check(self.root, self.manifest), [])

    def test_path_escape_is_rejected(self):
        with self.assertRaises(ValueError):
            module.within(self.root, '../outside')


if __name__ == '__main__':
    unittest.main()
