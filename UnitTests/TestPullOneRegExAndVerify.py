import unittest
from Classes.PullOneRegExAndVerify import PullOneRegExAndVerify


class TestPullOneRegExAndVerify(unittest.TestCase):
    def test_RequiredUnits(self):
        result = PullOneRegExAndVerify("this has Engineering", 417)
        self.assertEqual(417, result.attributeId, "The world is watching'")
        self.assertEqual(True, result.IsMatched)


if __name__ == '__main__':
    unittest.main()
