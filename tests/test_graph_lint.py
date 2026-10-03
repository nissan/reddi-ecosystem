import copy
import tempfile
import unittest
from pathlib import Path

import yaml

from tools.graph_lint import ROOT, find_cycle, lint, lint_obligation_sequence, load_yaml


class GraphLintTests(unittest.TestCase):
    def test_repository_graph_is_valid(self):
        self.assertEqual([], lint(ROOT))

    def test_graph_schema_version_is_required(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        graph["schemaVersion"] = 1
        errors = self._lint_with_graph(graph)
        self.assertIn("planning/graph.yaml: schemaVersion must be 2", errors)

    def test_stale_planning_registry_schema_version_is_rejected(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        milestones = copy.deepcopy(load_yaml(ROOT / "planning/milestones.yaml"))
        milestones["schemaVersion"] = 1
        errors = self._lint_with_graph(graph, milestones=milestones)
        self.assertIn("planning/milestones.yaml: schemaVersion must be 2", errors)

    def test_stale_repositories_schema_version_is_rejected(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        repositories = copy.deepcopy(load_yaml(ROOT / "planning/repositories.yaml"))
        repositories["schemaVersion"] = 1
        errors = self._lint_with_graph(graph, repositories=repositories)
        self.assertIn("planning/repositories.yaml: schemaVersion must be 2", errors)

    def test_cycle_is_found(self):
        nodes = {
            "A": {"dependsOn": ["B"]},
            "B": {"dependsOn": ["C"]},
            "C": {"dependsOn": ["A"]},
        }
        self.assertEqual(["A", "B", "C", "A"], find_cycle(nodes))

    def test_unknown_dependency_is_rejected(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        graph["nodes"][0]["dependsOn"] = ["DOES-NOT-EXIST"]
        errors = self._lint_with_graph(graph)
        self.assertTrue(any("unknown dependency" in error for error in errors))

    def test_earlier_milestone_cannot_depend_on_later_milestone(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        nodes = {node["id"]: node for node in graph["nodes"]}
        nodes["ECO-071"]["dependsOn"].append("ECO-112")
        errors = self._lint_with_graph(graph)
        self.assertIn(
            "ECO-071: milestone M4 cannot depend on later ECO-112 in M8", errors
        )

    def test_unknown_gate_is_rejected(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        graph["nodes"][0]["humanGates"] = ["agent-decides"]
        errors = self._lint_with_graph(graph)
        self.assertTrue(any("unknown human gate" in error for error in errors))

    def test_dependency_non_string_elements_are_rejected(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        graph["nodes"][0]["dependsOn"] = [[]]
        errors = self._lint_with_graph(graph)
        self.assertTrue(
            any("dependsOn must contain only strings" in error for error in errors)
        )

    def test_human_gate_non_string_elements_are_rejected(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        graph["nodes"][0]["humanGates"] = [{}]
        errors = self._lint_with_graph(graph)
        self.assertTrue(
            any("humanGates must contain only strings" in error for error in errors)
        )

    def test_solana_audd_technical_evidence_is_required_before_cross_standard_fixture(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        nodes = {node["id"]: node for node in graph["nodes"]}
        nodes["ECO-043"]["dependsOn"] = ["ECO-041"]
        errors = lint_obligation_sequence(nodes)
        self.assertIn("ECO-043: missing required dependency ECO-046", errors)

    def test_public_buzz_sidecar_still_requires_external_acceptance_gate(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        nodes = {node["id"]: node for node in graph["nodes"]}
        nodes["ECO-062"]["dependsOn"].remove("ECO-047")
        errors = lint_obligation_sequence(nodes)
        self.assertIn("ECO-062: missing required dependency ECO-047", errors)

    def test_technical_split_nodes_keep_their_human_gates(self):
        for node_id, gate in (
            ("ECO-043", "live-payment"),
            ("ECO-046", "signing-or-custody"),
            ("ECO-060", "upstream-contact"),
            ("ECO-060", "repo-creation"),
        ):
            with self.subTest(node_id=node_id, gate=gate):
                graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
                nodes = {node["id"]: node for node in graph["nodes"]}
                nodes[node_id]["humanGates"].remove(gate)
                errors = lint_obligation_sequence(nodes)
                self.assertIn(
                    f"{node_id}: missing required human gate {gate}", errors
                )

    def test_comment_truncated_criterion_is_rejected(self):
        graph_text = (ROOT / "planning/graph.yaml").read_text(encoding="utf-8")
        graph = load_yaml(ROOT / "planning/graph.yaml")
        criterion = next(
            node for node in graph["nodes"] if node["id"] == "ECO-060"
        )["acceptance"][1]
        unquoted = criterion.replace("lab issues 424-427", "lab #424-#427")
        self.assertIn(f"- {criterion}\n", graph_text)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "planning").mkdir()
            for name in ("milestones.yaml", "repositories.yaml"):
                (root / "planning" / name).write_text(
                    (ROOT / "planning" / name).read_text(encoding="utf-8"),
                    encoding="utf-8",
                )
            (root / "planning/graph.yaml").write_text(
                graph_text.replace(f"- {criterion}\n", f"- {unquoted}\n"),
                encoding="utf-8",
            )
            errors = lint(root)
        self.assertIn(
            "ECO-060: acceptance entries must be complete sentences ending with a period",
            errors,
        )

    def test_buzz_reuse_criterion_keeps_its_scope_and_never_live_guard(self):
        graph = load_yaml(ROOT / "planning/graph.yaml")
        node = next(node for node in graph["nodes"] if node["id"] == "ECO-060")
        reuse = [item for item in node["acceptance"] if "424-427" in item]
        self.assertEqual(1, len(reuse))
        scope, _, guard = reuse[0].partition(";")
        self.assertIn("reused only at its evidenced plan/spec or implementation scope", scope)
        self.assertIn("never represented as a live integration", guard)

    def test_early_baselines_precede_consuming_milestones(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        nodes = {node["id"]: node for node in graph["nodes"]}
        nodes["ECO-071"]["dependsOn"].remove("ECO-018")
        nodes["ECO-092"]["dependsOn"].remove("ECO-017")
        errors = lint_obligation_sequence(nodes)
        self.assertIn("ECO-071: missing required dependency ECO-018", errors)
        self.assertIn("ECO-092: missing required dependency ECO-017", errors)

    def test_solana_audd_implementation_requires_m0_obligation_reconciliation(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        nodes = {node["id"]: node for node in graph["nodes"]}
        nodes["ECO-042"]["dependsOn"].remove("ECO-004")
        errors = lint_obligation_sequence(nodes)
        self.assertIn("ECO-042: missing required dependency ECO-004", errors)

    def test_payment_adapter_contract_methods_are_required(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        nodes = {node["id"]: node for node in graph["nodes"]}
        nodes["ECO-041"]["adapterMethods"].remove("refund_or_reverse")
        errors = lint_obligation_sequence(nodes)
        self.assertIn("ECO-041: adapter contract must cover refund_or_reverse", errors)

    def test_adapter_contract_method_is_not_inferred_from_prose(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        nodes = {node["id"]: node for node in graph["nodes"]}
        nodes["ECO-041"]["acceptance"] = [
            "Contract excludes redact; redact is unsupported."
        ]
        nodes["ECO-041"]["adapterMethods"].remove("redact")
        errors = lint_obligation_sequence(nodes)
        self.assertIn("ECO-041: adapter contract must cover redact", errors)

    def test_unknown_adapter_method_is_rejected_on_any_node(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        nodes = {node["id"]: node for node in graph["nodes"]}
        nodes["ECO-044"]["adapterMethods"] = ["pay"]
        errors = self._lint_with_graph(graph)
        self.assertIn("ECO-044: unknown adapter method pay", errors)

    def test_duplicate_adapter_method_is_rejected_on_any_node(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        nodes = {node["id"]: node for node in graph["nodes"]}
        nodes["ECO-041"]["adapterMethods"].append("quote")
        nodes["ECO-044"]["adapterMethods"] = ["quote", "quote"]
        errors = self._lint_with_graph(graph)
        self.assertIn("ECO-041: duplicate adapter method quote", errors)
        self.assertIn("ECO-044: duplicate adapter method quote", errors)

    def test_invalid_dependency_shape_returns_diagnostics(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        nodes = {node["id"]: node for node in graph["nodes"]}
        nodes["ECO-042"]["dependsOn"] = None
        errors = self._lint_with_graph(graph)
        self.assertIn("ECO-042: dependsOn must be a list", errors)

    def test_first_implementation_role_must_stay_on_eco042(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        nodes = {node["id"]: node for node in graph["nodes"]}
        nodes["ECO-042"]["railRole"] = "comparison-fixture"
        nodes["ECO-043"]["railRole"] = "first-implementation"
        errors = lint_obligation_sequence(nodes)
        self.assertIn("ECO-042: railRole must be first-implementation", errors)
        self.assertIn(
            "exactly one node may declare railRole first-implementation, found ECO-043",
            errors,
        )

    def test_first_implementation_must_declare_the_solana_audd_rail(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        nodes = {node["id"]: node for node in graph["nodes"]}
        nodes["ECO-042"]["railProfile"] = "mpp"
        errors = lint_obligation_sequence(nodes)
        self.assertIn(
            "ECO-042: first-implementation railProfile must be solana-audd", errors
        )

    def test_first_implementation_without_rail_profile_is_rejected(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        nodes = {node["id"]: node for node in graph["nodes"]}
        del nodes["ECO-042"]["railProfile"]
        errors = lint_obligation_sequence(nodes)
        self.assertIn(
            "ECO-042: first-implementation railProfile must be solana-audd", errors
        )

    def test_comparison_standards_must_cover_required_standards(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        nodes = {node["id"]: node for node in graph["nodes"]}
        nodes["ECO-043"]["comparisonStandards"] = [
            item for item in nodes["ECO-043"]["comparisonStandards"] if item != "x402"
        ]
        self.assertIn("x402", nodes["ECO-043"]["outcome"])
        errors = lint_obligation_sequence(nodes)
        self.assertIn("ECO-043: comparisonStandards must include x402", errors)

    def test_any_comparison_fixture_must_follow_the_technical_evidence_pack(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        nodes = {node["id"]: node for node in graph["nodes"]}
        self.assertNotIn("ECO-999", nodes)
        nodes["ECO-999"] = {
            "id": "ECO-999",
            "railRole": "comparison-fixture",
            "comparisonStandards": ["mpp"],
            "dependsOn": ["ECO-041"],
        }
        errors = lint_obligation_sequence(nodes)
        self.assertIn("ECO-999: missing required dependency ECO-046", errors)

    def test_first_rail_profile_requires_the_first_implementation_role(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        for node in graph["nodes"]:
            if node["id"] == "ECO-043":
                node["railProfile"] = "solana-audd"
        errors = self._lint_with_graph(graph)
        self.assertTrue(
            any(
                "ECO-043: railProfile solana-audd requires railRole"
                " first-implementation" in error
                for error in errors
            )
        )

    def test_rail_profile_without_a_rail_role_is_rejected(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        for node in graph["nodes"]:
            if node["id"] == "ECO-044":
                self.assertIsNone(node.get("railRole"))
                node["railProfile"] = "mpp"
        errors = self._lint_with_graph(graph)
        self.assertIn("ECO-044: railProfile requires an explicit railRole", errors)

    def test_comparison_standards_without_a_rail_role_are_rejected(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        for node in graph["nodes"]:
            if node["id"] == "ECO-044":
                self.assertIsNone(node.get("railRole"))
                node["comparisonStandards"] = ["mpp", "ap2"]
        errors = self._lint_with_graph(graph)
        self.assertIn("ECO-044: comparisonStandards requires an explicit railRole", errors)

    def test_unknown_comparison_standard_is_rejected(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        for node in graph["nodes"]:
            if node["id"] == "ECO-043":
                node["comparisonStandards"] = node["comparisonStandards"] + ["x4o2"]
        errors = self._lint_with_graph(graph)
        self.assertTrue(
            any("unknown comparisonStandards entry x4o2" in error for error in errors)
        )

    def test_first_rail_profile_cannot_be_listed_as_a_comparison_standard(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        for node in graph["nodes"]:
            if node["id"] == "ECO-060":
                node["comparisonStandards"] = ["solana-audd"]
        errors = self._lint_with_graph(graph)
        self.assertTrue(
            any(
                "solana-audd is the first implementation profile, not a comparison"
                " standard" in error
                for error in errors
            )
        )

    def test_unknown_rail_role_is_rejected(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        for node in graph["nodes"]:
            if node["id"] == "ECO-041":
                node["railRole"] = "solana-only"
        errors = self._lint_with_graph(graph)
        self.assertTrue(any("unknown railRole solana-only" in error for error in errors))

    def test_malformed_rail_field_types_return_diagnostics(self):
        cases = (
            ("railRole", [], "ECO-041: unknown railRole []"),
            ("railProfile", [], "ECO-042: unknown railProfile []"),
            (
                "comparisonStandards",
                [[]],
                "ECO-043: unknown comparisonStandards entry []",
            ),
        )
        for field, value, expected in cases:
            with self.subTest(field=field):
                graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
                nodes = {node["id"]: node for node in graph["nodes"]}
                node_id = {
                    "railRole": "ECO-041",
                    "railProfile": "ECO-042",
                    "comparisonStandards": "ECO-043",
                }[field]
                nodes[node_id][field] = value
                errors = self._lint_with_graph(graph)
                self.assertIn(expected, errors)

    def test_missing_acceptance_is_rejected(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        graph["nodes"][0]["acceptance"] = []
        errors = self._lint_with_graph(graph)
        self.assertTrue(any("acceptance must contain" in error for error in errors))

    def test_evidence_produced_malformed_values_are_rejected(self):
        for value in ("", {}, 0):
            with self.subTest(value=value):
                graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
                graph["nodes"][0]["evidenceProduced"] = value
                errors = self._lint_with_graph(graph)
                self.assertTrue(
                    any("evidenceProduced must be a list" in error for error in errors)
                )

    def test_evidence_produced_non_string_elements_are_rejected(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        graph["nodes"][0]["evidenceProduced"] = ["valid", 42]
        errors = self._lint_with_graph(graph)
        self.assertTrue(
            any("evidenceProduced must contain only strings" in error for error in errors)
        )

    def test_projected_list_field_with_non_string_element_is_rejected(self):
        for field in ("acceptance", "subtasks", "evidenceExpected"):
            with self.subTest(field=field):
                graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
                graph["nodes"][0][field] = graph["nodes"][0][field] + [42]
                errors = self._lint_with_graph(graph)
                self.assertTrue(
                    any(f"{field} must contain only strings" in error for error in errors)
                )

    def _lint_with_graph(self, graph, milestones=None, repositories=None):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "planning").mkdir()
            for name, replacement in (
                ("milestones.yaml", milestones),
                ("repositories.yaml", repositories),
            ):
                if replacement is None:
                    (root / "planning" / name).write_text(
                        (ROOT / "planning" / name).read_text(encoding="utf-8"),
                        encoding="utf-8",
                    )
                else:
                    (root / "planning" / name).write_text(
                        yaml.safe_dump(replacement, sort_keys=False), encoding="utf-8"
                    )
            (root / "planning/graph.yaml").write_text(
                yaml.safe_dump(graph, sort_keys=False), encoding="utf-8"
            )
            return lint(root)


if __name__ == "__main__":
    unittest.main()
