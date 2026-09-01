import copy
import shutil
import tempfile
import unittest
from pathlib import Path

import yaml

from tools.research_lint import ROOT, lint, load


class ResearchLintTests(unittest.TestCase):
    def test_registries_are_valid(self):
        self.assertEqual([], lint(ROOT))

    def test_commitment_without_acceptance_artifacts_is_rejected(self):
        grants = copy.deepcopy(load(ROOT / "docs/grants/commitments.yaml"))
        del grants["commitments"][0]["acceptanceArtifacts"]
        errors = self._lint_with_grants(grants)
        self.assertIn(
            "GRANT-2026-01: missing commitment field acceptanceArtifacts", errors
        )

    def test_empty_acceptance_artifacts_are_rejected(self):
        grants = copy.deepcopy(load(ROOT / "docs/grants/commitments.yaml"))
        grants["commitments"][0]["acceptanceArtifacts"] = []
        errors = self._lint_with_grants(grants)
        self.assertIn(
            "GRANT-2026-01: acceptanceArtifacts must be a non-empty list", errors
        )

    def _lint_with_grants(self, grants):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "prompts", root / "prompts")
            (root / "research").mkdir()
            shutil.copy(ROOT / "research/SOURCES.yaml", root / "research/SOURCES.yaml")
            (root / "docs/grants").mkdir(parents=True)
            (root / "docs/grants/commitments.yaml").write_text(
                yaml.safe_dump(grants, sort_keys=False), encoding="utf-8"
            )
            return lint(root)


if __name__ == "__main__":
    unittest.main()
