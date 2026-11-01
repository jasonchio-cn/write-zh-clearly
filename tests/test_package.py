import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    @unittest.skipUnless(shutil.which("npm"), "npm is required to inspect the package")
    def test_package_contains_the_skill_for_both_clients(self):
        with tempfile.TemporaryDirectory() as cache:
            env = os.environ.copy()
            env["npm_config_cache"] = cache
            result = subprocess.run(
                [shutil.which("npm"), "pack", "--dry-run", "--ignore-scripts", "--json"],
                cwd=ROOT, env=env, text=True, encoding="utf-8", capture_output=True, check=True,
                shell=os.name == "nt",
            )
        packed = json.loads(result.stdout)
        package = packed[0] if isinstance(packed, list) else next(iter(packed.values()))
        files = {item["path"] for item in package["files"]}
        required = {
            ".codex-plugin/plugin.json",
            ".qoder-plugin/plugin.json",
            "skills/write-zh-clearly/SKILL.md",
            "skills/write-zh-clearly/agents/openai.yaml",
            "skills/write-zh-clearly/LICENSE",
            "README.md",
            "LICENSE",
        }
        self.assertTrue(required <= files, f"missing from package: {required - files}")
        package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
        for client in ("codex", "qoder"):
            manifest = json.loads((ROOT / f".{client}-plugin/plugin.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["name"], package["name"])
            self.assertEqual(manifest["version"], package["version"])
            self.assertEqual(manifest["license"], package["license"])
            self.assertEqual(manifest["skills"], "./skills/")
        self.assertEqual(
            (ROOT / "LICENSE").read_bytes(),
            (ROOT / "skills/write-zh-clearly/LICENSE").read_bytes(),
        )
        interface = json.loads((ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))["interface"]
        for field in ("logo", "composerIcon"):
            self.assertTrue(interface[field].startswith("./"))
            self.assertIn(interface[field][2:], files)


if __name__ == "__main__":
    unittest.main()
