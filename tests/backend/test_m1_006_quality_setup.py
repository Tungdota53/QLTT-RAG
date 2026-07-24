import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import quality_check


class QualitySetupTests(unittest.TestCase):
    def test_owned_artifacts_pass_dependency_free_checks(self) -> None:
        quality_check.check_python()
        quality_check.check_json_and_refs()
        quality_check.check_safety_and_hygiene()

    def test_unresolved_local_reference_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            document = root / "broken.json"
            document.write_text(json.dumps({"$ref": "missing.json#/value"}), encoding="utf-8")
            with patch.object(quality_check, "OWNED_PATHS", (root,)):
                with self.assertRaisesRegex(ValueError, "missing local JSON reference target"):
                    quality_check.check_json_and_refs()

    def test_hard_coded_secret_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            sensitive_name = "access" + "_token"
            (root / "unsafe.py").write_text(f'{sensitive_name} = "synthetic-value"\n', encoding="utf-8")
            with patch.object(quality_check, "OWNED_PATHS", (root,)):
                with self.assertRaisesRegex(ValueError, "possible hard-coded secret"):
                    quality_check.check_safety_and_hygiene()

    def test_missing_typescript_compiler_has_deterministic_guidance(self) -> None:
        with patch.dict("os.environ", {}, clear=True), patch.object(Path, "is_file", return_value=False), patch.object(quality_check.shutil, "which", return_value=None):
            with self.assertRaisesRegex(RuntimeError, "never downloads packages"):
                quality_check.typescript_compiler()


if __name__ == "__main__":
    unittest.main()