import json
import re
import unittest
from pathlib import Path
from urllib.parse import urlparse


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
CONTRACT_PATH = REPOSITORY_ROOT / "packages/contracts/asyncapi/common.asyncapi.json"


class CommonAsyncApiContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.document = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
        cls.components = cls.document["components"]
        cls.schemas = cls.components["schemas"]

    def test_document_is_asyncapi_30_component_library_at_version_010(self) -> None:
        self.assertEqual("3.0.0", self.document["asyncapi"])
        self.assertEqual("0.1.0", self.document["info"]["version"])
        self.assertEqual({}, self.document["channels"])
        self.assertEqual({}, self.document["operations"])
        self.assertIn("no business channels", self.document["info"]["description"])

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

    def test_event_envelope_requires_governed_identity_and_version_fields(self) -> None:
        envelope = self.schemas["EventEnvelope"]
        self.assertFalse(envelope["additionalProperties"])
        self.assertEqual(
            {
                "event_id",
                "event_type",
                "schema_version",
                "aggregate_id",
                "aggregate_version",
                "occurred_at",
                "received_at",
                "source",
                "trace_id",
                "data",
            },
            set(envelope["required"]),
        )
        self.assertEqual(1, envelope["properties"]["aggregate_version"]["minimum"])
        self.assertEqual("date-time", envelope["properties"]["occurred_at"]["format"])
        self.assertEqual("date-time", envelope["properties"]["received_at"]["format"])

    def test_schema_version_is_strict_semver(self) -> None:
        pattern = self.schemas["SemanticVersion"]["pattern"]
        for valid in ("0.1.0", "1.0.0", "12.34.56"):
            self.assertIsNotNone(re.fullmatch(pattern, valid), valid)
        for invalid in ("v1", "1.0", "01.0.0", "1.0.0-beta"):
            self.assertIsNone(re.fullmatch(pattern, invalid), invalid)
        self.assertIn("new major version", self.schemas["SemanticVersion"]["description"])

    def test_delivery_policy_is_at_least_once_and_bounded(self) -> None:
        policy = self.schemas["DeliveryPolicy"]
        properties = policy["properties"]
        self.assertEqual("at_least_once", properties["delivery_guarantee"]["const"])
        self.assertEqual("event_id", properties["deduplication_key"]["const"])
        self.assertEqual("aggregate_id", properties["ordering_key"]["const"])
        self.assertGreaterEqual(properties["max_attempts"]["minimum"], 2)
        self.assertLessEqual(properties["max_attempts"]["maximum"], 20)
        self.assertEqual(True, properties["dead_letter_on_exhaustion"]["const"])
        self.assertIn("outbox", policy["description"])
        self.assertIn("inbox", policy["description"])

    def test_consumer_checkpoint_handles_duplicate_reorder_and_gap(self) -> None:
        checkpoint = self.schemas["ConsumerCheckpoint"]
        outcomes = set(checkpoint["properties"]["outcome"]["enum"])
        self.assertTrue(
            {
                "applied",
                "duplicate_ignored",
                "reorder_deferred",
                "gap_detected",
                "dead_lettered",
            }.issubset(outcomes)
        )
        self.assertIn("stops application", checkpoint["description"])
        self.assertIn("never infer missing state", checkpoint["description"])

    def test_dead_letter_metadata_excludes_raw_payload_and_exception_detail(self) -> None:
        dead_letter = self.schemas["DeadLetterMetadata"]
        properties = dead_letter["properties"]
        for forbidden in (
            "data",
            "payload",
            "raw_payload",
            "exception",
            "stack_trace",
            "token",
            "gps",
            "health_detail",
        ):
            self.assertNotIn(forbidden, properties)
        self.assertIn("never an exception stack or raw payload", properties["reason_code"]["description"])
        self.assertIn("payload bytes are not copied", dead_letter["description"])

    def test_retry_and_replay_rules_preserve_event_identity(self) -> None:
        rules = self.document["x-safezone-contract-rules"]
        self.assertEqual("deduplicate_by_event_id", rules["duplicate_handling"])
        self.assertEqual("defer_by_aggregate_version", rules["reorder_handling"])
        self.assertEqual(
            "stop_aggregate_and_reconcile_with_owner", rules["gap_handling"]
        )
        self.assertEqual(
            "preserve_event_id_and_suppress_duplicate_side_effects",
            rules["replay_handling"],
        )

    def test_ai_authoritative_event_semantics_are_explicitly_forbidden(self) -> None:
        forbidden = set(
            self.document["x-safezone-contract-rules"]["forbidden_event_semantics"]
        )
        self.assertEqual(
            {
                "ai.evacuation_ordered",
                "ai.road_closed",
                "ai.report_verified",
                "ai.team_dispatched",
                "ai.risk_rule_activated",
            },
            forbidden,
        )

    def test_contract_contains_no_business_event_or_sensitive_fixture(self) -> None:
        serialized = json.dumps(self.document, ensure_ascii=False).lower()
        self.assertEqual({"CommonEvent"}, set(self.components["messages"]))
        for field in (
            '"phone"',
            '"address"',
            '"latitude"',
            '"longitude"',
            '"health"',
            '"access_token"',
            '"raw_media"',
        ):
            self.assertNotIn(field, serialized)

    @staticmethod
    def _walk_references(value: object):
        if isinstance(value, dict):
            for key, child in value.items():
                if key == "$ref":
                    parsed = urlparse(child)
                    if not parsed.scheme and not parsed.path:
                        yield child
                yield from CommonAsyncApiContractTests._walk_references(child)
        elif isinstance(value, list):
            for child in value:
                yield from CommonAsyncApiContractTests._walk_references(child)


if __name__ == "__main__":
    unittest.main()
