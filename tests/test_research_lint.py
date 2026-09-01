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

    def test_stale_registry_schema_version_is_rejected(self):
        grants = copy.deepcopy(load(ROOT / "docs/grants/commitments.yaml"))
        grants["schemaVersion"] = 1
        errors = self._lint_with_grants(grants)
        self.assertIn("docs/grants/commitments.yaml: schemaVersion must be 2", errors)

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

    def test_existing_file_beside_the_repository_is_rejected(self):
        research = copy.deepcopy(load(ROOT / "research/SOURCES.yaml"))
        research["sources"][0]["url"] = f"repo:../{self.SIBLING_NAME}"
        errors = self._lint_with_research(research)
        self.assertTrue(
            any("resolves outside the repository" in error for error in errors)
        )

    def test_symlink_escaping_the_repository_is_rejected(self):
        research = copy.deepcopy(load(ROOT / "research/SOURCES.yaml"))
        research["sources"][0]["url"] = "repo:research/linked-report.md"
        errors = self._lint_with_research(research, symlink_escape=True)
        self.assertTrue(
            any("resolves outside the repository" in error for error in errors)
        )

    def test_repo_source_location_must_exist(self):
        research = copy.deepcopy(load(ROOT / "research/SOURCES.yaml"))
        research["sources"][0]["url"] = "repo:research/does-not-exist.md"
        errors = self._lint_with_research(research)
        self.assertTrue(
            any("does not name an existing file" in error for error in errors)
        )

    SIBLING_NAME = "outside-report.md"

    def _lint_with_research(self, research, symlink_escape=False):
        return self._lint_with(research=research, symlink_escape=symlink_escape)

    def _lint_with_grants(self, grants):
        return self._lint_with(grants=grants)

    def _lint_with(self, research=None, grants=None, symlink_escape=False):
        with tempfile.TemporaryDirectory() as directory:
            outside = Path(directory) / self.SIBLING_NAME
            outside.write_text("real file beside the checkout\n", encoding="utf-8")
            root = Path(directory) / "repo"
            root.mkdir()
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
            if symlink_escape:
                (root / "research/linked-report.md").symlink_to(outside)
            return lint(root)


if __name__ == "__main__":
    unittest.main()
