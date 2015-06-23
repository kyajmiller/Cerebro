import unittest
from Classes.RequiredGender import RequiredGender


class TestStringMethods(unittest.TestCase):
    def test_RequiredGender(self):
        testrequiredgender = RequiredGender('This scholarship is for females only')
        self.assertIsNotNone(testrequiredgender)
        self.assertEqual(testrequiredgender.getRequiredGender(), ['female'])

    def test_GenderFailure(self):
        failrequiredgender = RequiredGender('There is no gender in this string')
        self.assertIsNotNone(failrequiredgender)
        self.assertEqual(failrequiredgender.getRequiredGender(), [])


if __name__ == '__main__':
    unittest.main()
