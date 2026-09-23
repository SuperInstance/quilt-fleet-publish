import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import unittest

from fleet_publish import discover_repos, has_pypi, has_npm, has_crates, REPOS_DIR


class TestDiscover(unittest.TestCase):

    def test_discover(self):
        repos = discover_repos()
        self.assertGreater(len(repos), 10)  # we have 19+

    def test_repos_sorted(self):
        repos = discover_repos()
        self.assertEqual(repos, sorted(repos))


class TestDetect(unittest.TestCase):

    def test_has_pypi(self):
        result = has_pypi(os.path.join(REPOS_DIR, "quilt-egg"))
        self.assertTrue(result)

    def test_has_npm(self):
        result = has_npm(os.path.join(REPOS_DIR, "quilt-bridge"))
        self.assertTrue(result)

    def test_has_crates(self):
        result = has_crates(os.path.join(REPOS_DIR, "quilt-egg-rust"))
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
