import tempfile
import unittest
from pathlib import Path

from tools.project_issues import ROOT, bullets, generate, node_markdown


class IssueProjectionTests(unittest.TestCase):
    def test_checked_in_projections_are_current(self):
        self.assertEqual([], generate(ROOT, check=True))

    def test_bullets_rejects_scalar_evidence_produced_values(self):
        with self.assertRaises(TypeError):
            bullets("evidence/github/ECO-001-2026-08-31.md")

    def test_node_markdown_rejects_scalar_depends_on(self):
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
            "dependsOn": "ECO-000",
            "outcome": "Example outcome.",
            "subtasks": ["do the thing"],
            "acceptance": ["thing is done"],
            "evidenceExpected": ["a command transcript"],
            "humanGates": [],
        }
        epics = {"EPIC-1": {"title": "Example epic"}}
        with self.assertRaises(TypeError):
            node_markdown(node, epics)

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

