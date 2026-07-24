import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SDK = ROOT / "packages" / "sdk-typescript"
OPENAPI = ROOT / "packages" / "contracts" / "openapi"

class SdkHandoffTests(unittest.TestCase):
    def test_handoff_covers_exactly_five_contract_sources_at_010(self):
        metadata = json.loads((SDK / "COMPATIBILITY.json").read_text(encoding="utf-8"))
        expected = sorted(path.name for path in OPENAPI.glob("*.openapi.json"))
        self.assertEqual(expected, sorted(metadata["sourceDocuments"]))
        self.assertEqual("0.1.0", metadata["sdkVersion"])
        for name in expected:
            document = json.loads((OPENAPI / name).read_text(encoding="utf-8"))
            self.assertEqual(metadata["contractVersion"], document["info"]["version"])

    def test_generated_client_covers_every_operation_id(self):
        source = (SDK / "src" / "index.ts").read_text(encoding="utf-8")
        operation_ids = []
        for path in OPENAPI.glob("*.openapi.json"):
            document = json.loads(path.read_text(encoding="utf-8"))
            for path_item in document["paths"].values():
                for operation in path_item.values():
                    operation_ids.append(operation["operationId"])
        self.assertEqual(5, len(operation_ids))
        for operation_id in operation_ids:
            self.assertIn(f"  {operation_id}(", source)

if __name__ == "__main__":
    unittest.main()
