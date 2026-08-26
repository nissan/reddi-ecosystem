import unittest

from tools.research_lint import ROOT, lint


class ResearchLintTests(unittest.TestCase):
    def test_registries_are_valid(self):
        self.assertEqual([], lint(ROOT))


if __name__ == "__main__":
    unittest.main()

