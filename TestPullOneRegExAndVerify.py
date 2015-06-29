import unittest
from Classes.PullOneRegExAndVerify import PullOneRegExAndVerify


class TestStringMethods(unittest.TestCase):
    def test_RequiredUnits(self):
        result = PullOneRegExAndVerify("this has engineering", 417)
        self.assertEqual(417, result.attributeId)


if __name__ == '__main__':
    unittest.main()
