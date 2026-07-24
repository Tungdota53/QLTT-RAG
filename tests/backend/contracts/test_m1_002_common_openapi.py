import json
import re
import unittest
from pathlib import Path
from urllib.parse import urlparse


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
CONTRACT_PATH = REPOSITORY_ROOT / "packages/contracts/openapi/common.openapi.json"


class CommonOpenApiContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.document = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
        cls.components = cls.document["components"]

    def test_document_is_openapi_31_component_library_at_version_010(self) -> None:
        self.assertEqual("3.1.0", self.document["openapi"])
        self.assertEqual("0.1.0", self.document["info"]["version"])
        self.assertEqual(
            "https://json-schema.org/draft/2020-12/schema",
            self.document["jsonSchemaDialect"],
        )
        self.assertEqual({}, self.document["paths"])

    def test_all_local_references_resolve(self) -> None:
        references = list(self._walk_references(self.document))
        self.assertGreater(len(references), 0)

        for reference in references:
            self.assertTrue(reference.startswith("#/"), reference)
            current = self.document
            for token in reference[2:].split("/"):
                token = token.replace("~1", "/").replace("~0", "~")
                self.assertIn(token, current, reference)
                current = current[token]

    def test_problem_details_has_stable_safe_error_shape(self) -> None:
        schema = self.components["schemas"]["ProblemDetails"]
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(
            {"type", "title", "status", "code", "correlation_id"},
            set(schema["required"]),
        )
        self.assertEqual(400, schema["properties"]["status"]["minimum"])
        self.assertEqual(599, schema["properties"]["status"]["maximum"])
        self.assertNotIn("stack_trace", schema["properties"])
        self.assertNotIn("raw_payload", schema["properties"])

        for response_name in ("BadRequest", "Forbidden", "IdempotencyConflict"):
            response = self.components["responses"][response_name]
            media = response["content"]["application/problem+json"]
            self.assertEqual(
                "#/components/schemas/ProblemDetails", media["schema"]["$ref"]
            )
            self.assertIn("X-Correlation-ID", response["headers"])

    def test_cursor_pagination_is_bounded_and_opaque(self) -> None:
        cursor = self.components["parameters"]["PageCursor"]
        limit = self.components["parameters"]["PageLimit"]
        metadata = self.components["schemas"]["PageMetadata"]

        self.assertEqual("page_cursor", cursor["name"])
        self.assertNotIn("pattern", cursor["schema"])
        self.assertEqual(1, limit["schema"]["minimum"])
        self.assertEqual(100, limit["schema"]["maximum"])
        self.assertEqual(20, limit["schema"]["default"])
        self.assertEqual({"page_size", "has_more"}, set(metadata["required"]))
        self.assertIn("next_cursor", metadata["properties"])
        self.assertNotIn("total_count", metadata["required"])

    def test_idempotency_contract_defines_replay_and_conflict_semantics(self) -> None:
        parameter = self.components["parameters"]["IdempotencyKey"]
        replay_header = self.components["headers"]["IdempotencyReplayed"]
        record = self.components["schemas"]["IdempotencyRecord"]

        self.assertTrue(parameter["required"])
        self.assertEqual("Idempotency-Key", parameter["name"])
        self.assertIn("materially different request", parameter["description"])
        self.assertEqual("boolean", replay_header["schema"]["type"])
        self.assertIn("request_fingerprint", record["required"])
        self.assertIn("expires_at", record["required"])
        self.assertNotIn("raw_key", record["properties"])
        self.assertIn("IdempotencyConflict", self.components["responses"])

    def test_locality_scope_is_explicit_but_not_an_authorization_grant(self) -> None:
        locality = self.components["schemas"]["LocalityScope"]
        self.assertEqual({"locality_id", "level"}, set(locality["required"]))
        self.assertEqual(
            ["province", "district", "commune"],
            locality["properties"]["level"]["enum"],
        )
        self.assertIn("does not itself grant access", locality["description"])
        self.assertIn("Forbidden", self.components["responses"])

    def test_examples_and_descriptions_do_not_contain_forbidden_sensitive_data(self) -> None:
        serialized = json.dumps(self.document, ensure_ascii=False).lower()
        forbidden = (
            "password",
            "access_token",
            "refresh_token",
            "private_key",
            "raw gps",
            "health detail",
        )
        for term in forbidden:
            self.assertNotIn(term, serialized)

    def test_uri_and_timestamp_formats_are_contractual(self) -> None:
        problem = self.components["schemas"]["ProblemDetails"]
        record = self.components["schemas"]["IdempotencyRecord"]
        self.assertEqual("uri-reference", problem["properties"]["type"]["format"])
        self.assertEqual("date-time", record["properties"]["created_at"]["format"])
        self.assertEqual("date-time", record["properties"]["expires_at"]["format"])

    def test_machine_codes_and_identifiers_are_constrained(self) -> None:
        code_pattern = self.components["schemas"]["ProblemDetails"]["properties"][
            "code"
        ]["pattern"]
        identifier_pattern = self.components["schemas"]["OpaqueIdentifier"]["pattern"]

        self.assertIsNotNone(re.fullmatch(code_pattern, "LOCALITY_FORBIDDEN"))
        self.assertIsNone(re.fullmatch(code_pattern, "free text"))
        self.assertIsNotNone(re.fullmatch(identifier_pattern, "loc_syn_district_001"))
        self.assertIsNone(re.fullmatch(identifier_pattern, "contains space"))

    @staticmethod
    def _walk_references(value: object):
        if isinstance(value, dict):
            for key, child in value.items():
                if key == "$ref":
                    parsed = urlparse(child)
                    if not parsed.scheme and not parsed.path:
                        yield child
                yield from CommonOpenApiContractTests._walk_references(child)
        elif isinstance(value, list):
            for child in value:
                yield from CommonOpenApiContractTests._walk_references(child)


if __name__ == "__main__":
    unittest.main()
