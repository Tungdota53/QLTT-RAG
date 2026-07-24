import json
import re
import unittest
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
OPENAPI_DIR = REPOSITORY_ROOT / "packages/contracts/openapi"
DOMAIN_FILES = (
    "identity.openapi.json",
    "alerts.openapi.json",
    "gis.openapi.json",
    "shelters.openapi.json",
)
HTTP_METHODS = {"get", "put", "post", "delete", "options", "head", "patch", "trace"}


class DomainOpenApiContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.paths = [OPENAPI_DIR / name for name in DOMAIN_FILES]
        cls.documents = {
            path.name: json.loads(path.read_text(encoding="utf-8")) for path in cls.paths
        }

    def test_documents_are_openapi_31_at_milestone_010(self) -> None:
        for name, document in self.documents.items():
            with self.subTest(document=name):
                self.assertEqual("3.1.0", document["openapi"])
                self.assertEqual("0.1.0", document["info"]["version"])
                self.assertEqual(
                    "https://json-schema.org/draft/2020-12/schema",
                    document["jsonSchemaDialect"],
                )
                self.assertTrue(document["paths"])

    def test_every_local_relative_reference_resolves_without_escaping_contract_dir(self) -> None:
        references = []
        for source_path, document in zip(self.paths, self.documents.values()):
            for reference in self._walk_refs(document):
                references.append(reference)
                file_part, separator, fragment = reference.partition("#")
                target = (source_path.parent / unquote(file_part)).resolve() if file_part else source_path
                self.assertEqual(OPENAPI_DIR.resolve(), target.parent, reference)
                self.assertTrue(target.is_file(), reference)
                target_document = json.loads(target.read_text(encoding="utf-8"))
                if separator and fragment:
                    current = target_document
                    self.assertTrue(fragment.startswith("/"), reference)
                    for token in fragment[1:].split("/"):
                        token = unquote(token).replace("~1", "/").replace("~0", "~")
                        self.assertIsInstance(current, dict, reference)
                        self.assertIn(token, current, reference)
                        current = current[token]
        self.assertTrue(any(ref.startswith("common.openapi.json#") for ref in references))

    def test_operation_and_schema_identifiers_are_unique_across_domain_contracts(self) -> None:
        operation_ids = []
        schema_ids = []
        for name, document in self.documents.items():
            schema_ids.extend(document.get("components", {}).get("schemas", {}).keys())
            for path_item in document["paths"].values():
                for method, operation in path_item.items():
                    if method in HTTP_METHODS:
                        self.assertIn("operationId", operation, (name, method))
                        operation_ids.append(operation["operationId"])
        self.assertEqual([], self._duplicates(operation_ids))
        self.assertEqual([], self._duplicates(schema_ids))

    def test_operations_are_read_only_and_do_not_define_later_epic_behaviors(self) -> None:
        for name, document in self.documents.items():
            for route, path_item in document["paths"].items():
                with self.subTest(document=name, route=route):
                    self.assertEqual({"get"}, set(path_item) & HTTP_METHODS)
        serialized = json.dumps(self.documents, ensure_ascii=False).lower()
        for prohibited in ("community-reports", "verify-report", "relief", "notification", "rag", "risk-score", "dispatch", "evacuation-order", "road-closure"):
            self.assertNotIn(prohibited, serialized)

    def test_alert_kinds_are_distinct_and_official_projection_is_immutable_and_provenanced(self) -> None:
        schemas = self.documents["alerts.openapi.json"]["components"]["schemas"]
        self.assertEqual(
            ["official_alert", "system_analysis", "community_report"],
            schemas["InformationKind"]["enum"],
        )
        alert = schemas["OfficialAlert"]
        required = set(alert["required"])
        self.assertTrue({"information_kind", "version_id", "version_number", "source", "content", "content_hash"} <= required)
        self.assertEqual("official_alert", alert["properties"]["information_kind"]["const"])
        self.assertEqual("^[a-f0-9]{64}$", alert["properties"]["content_hash"]["pattern"])
        self.assertIn("immutable", alert["properties"]["content"]["description"].lower())
        self.assertIn("previous_version_id", alert["properties"])
        self.assertIn("supersedes_version_id", alert["properties"])
        source_required = set(schemas["OfficialAlertSource"]["required"])
        self.assertTrue({"source_id", "authority_name", "source_uri", "retrieved_at", "signature_status"} <= source_required)

    def test_shelter_requires_official_freshness_evidence_and_represents_stale(self) -> None:
        schemas = self.documents["shelters.openapi.json"]["components"]["schemas"]
        shelter = schemas["PublicShelter"]
        verification = schemas["ShelterVerification"]
        self.assertTrue({"official_status", "freshness_status", "verification"} <= set(shelter["required"]))
        self.assertEqual(["current", "stale"], shelter["properties"]["freshness_status"]["enum"])
        self.assertEqual(
            {"authority_name", "source_uri", "verified_at", "fresh_until"},
            set(verification["required"]),
        )
        self.assertIn("cannot be shown as current official", verification["properties"]["fresh_until"]["description"])

    def test_locality_is_explicitly_not_authorization(self) -> None:
        identity = self.documents["identity.openapi.json"]["components"]["schemas"]["IdentityProjection"]
        description = identity["properties"]["locality_scopes"]["description"].lower()
        self.assertIn("does not grant access", description)
        gis_parameter = self.documents["gis.openapi.json"]["paths"]["/v1/localities/{locality_id}"]["get"]["parameters"][1]
        self.assertIn("not proof of authorization", gis_parameter["description"].lower())

    def test_ids_are_opaque_and_all_timestamp_fields_use_date_time(self) -> None:
        for name, document in self.documents.items():
            for key, value in self._walk_items(document):
                if key.endswith("_id") and isinstance(value, dict):
                    references = [value["$ref"]] if "$ref" in value else [
                        branch["$ref"]
                        for branch in value.get("oneOf", [])
                        if "$ref" in branch
                    ]
                    self.assertTrue(references, (name, key))
                    self.assertTrue(
                        all(ref.endswith("/OpaqueIdentifier") for ref in references),
                        (name, key),
                    )
                if key.endswith("_at") or key in {"fresh_until"}:
                    self.assertEqual("date-time", value.get("format"), (name, key))

    def test_public_projections_exclude_sensitive_or_operational_fields(self) -> None:
        serialized = json.dumps(self.documents, ensure_ascii=False).lower()
        forbidden_fields = ("password", "access_token", "refresh_token", "resident_list", "resident_name", "phone_number", "email_address", "household_members", "precise_user_location", "private_contact")
        for field in forbidden_fields:
            self.assertNotRegex(serialized, rf'"{re.escape(field)}"\s*:')
        gis = self.documents["gis.openapi.json"]["components"]["schemas"]["PublicLocality"]
        self.assertIn("excludes household points", gis["description"])

    @staticmethod
    def _walk_refs(value):
        if isinstance(value, dict):
            for key, child in value.items():
                if key == "$ref":
                    yield child
                yield from DomainOpenApiContractTests._walk_refs(child)
        elif isinstance(value, list):
            for child in value:
                yield from DomainOpenApiContractTests._walk_refs(child)

    @staticmethod
    def _walk_items(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key, child
                yield from DomainOpenApiContractTests._walk_items(child)
        elif isinstance(value, list):
            for child in value:
                yield from DomainOpenApiContractTests._walk_items(child)

    @staticmethod
    def _duplicates(values):
        return sorted(value for value, count in Counter(values).items() if count > 1)


if __name__ == "__main__":
    unittest.main()
