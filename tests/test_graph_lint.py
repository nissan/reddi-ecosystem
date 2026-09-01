import copy
import tempfile
import unittest
from pathlib import Path

import yaml

from tools.graph_lint import ROOT, find_cycle, lint, load_yaml


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

    def test_missing_acceptance_is_rejected(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        graph["nodes"][0]["acceptance"] = []
        errors = self._lint_with_graph(graph)
        self.assertTrue(any("acceptance must contain" in error for error in errors))

    def test_evidence_produced_scalar_is_rejected(self):
        graph = copy.deepcopy(load_yaml(ROOT / "planning/graph.yaml"))
        graph["nodes"][0]["evidenceProduced"] = "evidence/github/ECO-001-2026-08-31.md"
        errors = self._lint_with_graph(graph)
        self.assertTrue(any("evidenceProduced must be a list" in error for error in errors))

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

