import importlib.util
import tempfile
import unittest
from unittest import mock
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("installer", ROOT / "scripts/install.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)

class InstallTests(unittest.TestCase):
    def test_copy_failure_removes_only_this_runs_folders(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp) / ".agents/skills"
            existing = base / "unrelated-user-skill"
            existing.mkdir(parents=True)
            (existing / "keep.txt").write_text("USER DATA", encoding="utf-8")
            real_copy = installer.shutil.copytree
            count = 0
            def fail_second(source, destination, *args, **kwargs):
                nonlocal count
                if Path(source).parent == ROOT / "skills":
                    count += 1
                    if count == 2:
                        raise OSError("Synthetic copy failure")
                return real_copy(source, destination, *args, **kwargs)
            with mock.patch.object(installer.shutil, "copytree", side_effect=fail_second):
                with self.assertRaisesRegex(OSError, "newly created skill folders were removed"):
                    installer.install(ROOT, temp, "codex", apply=True)
            self.assertEqual([p.name for p in base.iterdir()], ["unrelated-user-skill"])
            self.assertEqual((existing / "keep.txt").read_text(), "USER DATA")
            installer.install(ROOT, temp, "codex", apply=True)
            self.assertEqual(len(list(base.iterdir())), 8)

    def test_cleanup_failure_reports_remaining_folder(self):
        with tempfile.TemporaryDirectory() as temp:
            with mock.patch.object(installer.shutil, "copytree", side_effect=OSError("Synthetic failure")), mock.patch.object(installer.shutil, "rmtree", side_effect=OSError("Synthetic locked folder")):
                with self.assertRaisesRegex(OSError, "cleanup incomplete.*xhs-content-ops"):
                    installer.install(ROOT, temp, "codex", apply=True)

    def test_preview_does_not_write(self):
        with tempfile.TemporaryDirectory() as temp:
            result = installer.install(ROOT, temp, "codex")
            self.assertEqual(len(result["destinations"]), 7)
            self.assertEqual(list(Path(temp).iterdir()), [])

    def test_all_targets_copy_complete_skills(self):
        for agent, subdir in installer.TARGETS.items():
            with self.subTest(agent=agent), tempfile.TemporaryDirectory() as temp:
                installer.install(ROOT, temp, agent, apply=True)
                for source in (ROOT / "skills").rglob("*"):
                    if source.is_file():
                        copied = Path(temp) / subdir / source.relative_to(ROOT / "skills")
                        self.assertEqual(source.read_bytes(), copied.read_bytes())

    def test_existing_content_not_overwritten(self):
        with tempfile.TemporaryDirectory() as temp:
            selected = ["xhs-post-writing"]
            installer.install(ROOT, temp, "codex", selected, True)
            target = Path(temp) / ".agents/skills/xhs-post-writing/SKILL.md"
            target.write_text("USER EDIT", encoding="utf-8")
            with self.assertRaises(ValueError):
                installer.install(ROOT, temp, "codex", apply=True)
            self.assertEqual(target.read_text(encoding="utf-8"), "USER EDIT")
            self.assertFalse((target.parent.parent / "xhs-content-ops").exists())

    def test_unknown_skill_no_write(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaises(ValueError):
                installer.install(ROOT, temp, "codex", ["../../escape"], True)
            self.assertEqual(list(Path(temp).iterdir()), [])

    def test_missing_project_is_not_created(self):
        with tempfile.TemporaryDirectory() as temp:
            missing = Path(temp) / "misspelled-project"
            with self.assertRaises(ValueError):
                installer.install(ROOT, missing, "codex", apply=True)
            self.assertFalse(missing.exists())

    def test_selected_skill_is_self_contained(self):
        with tempfile.TemporaryDirectory() as temp:
            installer.install(ROOT, temp, "cursor", ["xhs-preference-learning"], True)
            folder = Path(temp) / ".cursor/skills/xhs-preference-learning"
            self.assertTrue((folder / "references/preferences.md").is_file())
            self.assertTrue((folder / "assets/preferences.json").is_file())
            self.assertEqual(len(list(folder.parent.iterdir())), 1)

if __name__ == "__main__":
    unittest.main()
