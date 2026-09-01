import copy
import tempfile
import unittest
from pathlib import Path

import yaml

from tools.graph_lint import ROOT, find_cycle, lint, lint_obligation_sequence, load_yaml


class GraphLintTests(unittest.TestCase):
    def test_repository_graph_is_valid(self):
        self.assertEqual([], lint(ROOT))

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

    def test_solana_audd_sequence_is_required_before_cross_standard_proof(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        nodes = {node["id"]: node for node in graph["nodes"]}
        nodes["ECO-043"]["dependsOn"] = ["ECO-041"]
        errors = lint_obligation_sequence(nodes)
        self.assertIn("ECO-043: missing required dependency ECO-047", errors)

    def test_payment_adapter_contract_methods_are_required(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        nodes = {node["id"]: node for node in graph["nodes"]}
        nodes["ECO-041"]["acceptance"] = [
            item.replace("refund_or_reverse", "remedy")
            for item in nodes["ECO-041"]["acceptance"]
        ]
        nodes["ECO-041"]["outcome"] = nodes["ECO-041"]["outcome"].replace(
            "refund/reverse", "remedy"
        )
        errors = lint_obligation_sequence(nodes)
        self.assertIn("ECO-041: adapter contract must cover refund_or_reverse", errors)

    def test_adapter_contract_method_is_not_satisfied_by_a_longer_word(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        nodes = {node["id"]: node for node in graph["nodes"]}
        nodes["ECO-041"]["acceptance"] = [
            item.replace("redact", "remove") for item in nodes["ECO-041"]["acceptance"]
        ]
        nodes["ECO-041"]["outcome"] = nodes["ECO-041"]["outcome"].replace(
            "redact", "remove"
        )
        self.assertTrue(
            any("redaction" in subtask for subtask in nodes["ECO-041"]["subtasks"])
        )
        errors = lint_obligation_sequence(nodes)
        self.assertIn("ECO-041: adapter contract must cover redact", errors)

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

    def _lint_with_graph(self, graph):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "planning").mkdir()
            for name in ("milestones.yaml", "repositories.yaml"):
                (root / "planning" / name).write_text(
                    (ROOT / "planning" / name).read_text(encoding="utf-8"),
                    encoding="utf-8",
                )
            (root / "planning/graph.yaml").write_text(
                yaml.safe_dump(graph, sort_keys=False), encoding="utf-8"
            )
            return lint(root)


if __name__ == "__main__":
    unittest.main()
