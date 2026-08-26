import tempfile
import unittest
from pathlib import Path

from tools.project_issues import ROOT, generate


class IssueProjectionTests(unittest.TestCase):
    def test_checked_in_projections_are_current(self):
        self.assertEqual([], generate(ROOT, check=True))

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

