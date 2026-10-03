import tempfile
import unittest
from pathlib import Path

from tools.project_issues import ROOT, bullets, generate, load, node_markdown


class IssueProjectionTests(unittest.TestCase):
    def test_checked_in_projections_are_current(self):
        self.assertEqual([], generate(ROOT, check=True))

    def test_bullets_rejects_scalar_evidence_produced_values(self):
        with self.assertRaises(TypeError):
            bullets("evidence/github/ECO-001-2026-08-31.md")

    def test_node_markdown_rejects_scalar_depends_on(self):
        node = self._node(dependsOn="ECO-000")
        with self.assertRaises(TypeError):
            node_markdown(node, self._epics())

    def test_node_markdown_rejects_falsy_malformed_evidence_produced(self):
        for value in ("", {}, 0):
            with self.subTest(value=value):
                node = self._node(evidenceProduced=value)
                with self.assertRaises(TypeError):
                    node_markdown(node, self._epics())

    def test_node_markdown_rejects_falsy_malformed_human_gates(self):
        for value in ("", {}, 0):
            with self.subTest(value=value):
                node = self._node(humanGates=value)
                with self.assertRaises(TypeError):
                    node_markdown(node, self._epics())

    def test_projection_renders_every_parsed_acceptance_criterion_in_full(self):
        graph = load(ROOT / "planning/graph.yaml")
        epics = {epic["id"]: epic for epic in graph["epics"]}
        node = next(node for node in graph["nodes"] if node["id"] == "ECO-060")
        rendered = node_markdown(node, epics).splitlines()
        for criterion in node["acceptance"]:
            self.assertIn(f"- [ ] {criterion}", rendered)
        self.assertIn("- upstream-contact", rendered)
        self.assertIn("- repo-creation", rendered)

    def _node(self, **overrides):
        node = {
            "id": "ECO-999",
            "title": "Example",
            "epic": "EPIC-1",
            "milestone": "M0",
            "targetRepo": "ecosystem",
            "githubProjection": "issue",
            "status": "ready",
            "priority": "P1",
            "ownerRole": "agent",
            "dependsOn": [],
            "outcome": "Example outcome.",
            "subtasks": ["do the thing"],
            "acceptance": ["thing is done"],
            "evidenceExpected": ["a command transcript"],
            "humanGates": [],
        }
        node.update(overrides)
        return node

    def _epics(self):
        return {"EPIC-1": {"title": "Example epic"}}

    def test_checked_in_projection_names_graph_schema_version(self):
        readme = (ROOT / "planning/issues/README.md").read_text(encoding="utf-8")
        self.assertIn("- Graph schema version: 2", readme)

    def test_generator_rejects_unsupported_graph_schema_version(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "planning").mkdir()
            graph = (ROOT / "planning/graph.yaml").read_text(encoding="utf-8")
            (root / "planning/graph.yaml").write_text(
                graph.replace("schemaVersion: 2", "schemaVersion: 1", 1),
                encoding="utf-8",
            )
            self.assertEqual(
                ["planning/graph.yaml: schemaVersion must be 2"], generate(root)
            )

    def test_generation_is_deterministic(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "planning").mkdir()
            (root / "planning/graph.yaml").write_text(
                (ROOT / "planning/graph.yaml").read_text(encoding="utf-8"),
                encoding="utf-8",
            )
            generate(root)
            first = {
                path.relative_to(root): path.read_text(encoding="utf-8")
                for path in (root / "planning/issues").rglob("*.md")
            }
            generate(root)
            second = {
                path.relative_to(root): path.read_text(encoding="utf-8")
                for path in (root / "planning/issues").rglob("*.md")
            }
            self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
