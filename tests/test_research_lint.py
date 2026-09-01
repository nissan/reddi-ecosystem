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

    def test_non_https_non_repo_source_location_is_rejected(self):
        research = copy.deepcopy(load(ROOT / "research/SOURCES.yaml"))
        research["sources"][0]["url"] = "ftp://example.invalid/paper.pdf"
        errors = self._lint_with_research(research)
        self.assertTrue(
            any("source URL must use https or repo:" in error for error in errors)
        )

    def test_absolute_local_path_source_location_is_rejected(self):
        research = copy.deepcopy(load(ROOT / "research/SOURCES.yaml"))
        research["sources"][0]["url"] = "file:///srv/reports/report.md"
        errors = self._lint_with_research(research)
        self.assertTrue(
            any("source URL must use https or repo:" in error for error in errors)
        )

    def test_repo_source_location_must_resolve_inside_the_repository(self):
        research = copy.deepcopy(load(ROOT / "research/SOURCES.yaml"))
        research["sources"][0]["url"] = "repo:../outside/report.md"
        errors = self._lint_with_research(research)
        self.assertTrue(
            any("must name a file inside the repository" in error for error in errors)
        )

    def test_repo_source_location_must_exist(self):
        research = copy.deepcopy(load(ROOT / "research/SOURCES.yaml"))
        research["sources"][0]["url"] = "repo:research/does-not-exist.md"
        errors = self._lint_with_research(research)
        self.assertTrue(
            any("must name a file inside the repository" in error for error in errors)
        )

    def _lint_with_research(self, research):
        return self._lint_with(research=research)

    def _lint_with_grants(self, grants):
        return self._lint_with(grants=grants)

    def _lint_with(self, research=None, grants=None):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "prompts", root / "prompts")
            shutil.copytree(ROOT / "research", root / "research")
            (root / "docs/grants").mkdir(parents=True)
            for relative, replacement in (
                ("research/SOURCES.yaml", research),
                ("docs/grants/commitments.yaml", grants),
            ):
                if replacement is None:
                    shutil.copy(ROOT / relative, root / relative)
                else:
                    (root / relative).write_text(
                        yaml.safe_dump(replacement, sort_keys=False), encoding="utf-8"
                    )
            return lint(root)


if __name__ == "__main__":
    unittest.main()
