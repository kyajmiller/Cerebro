import unittest
from Classes.Gender import Gender


class TestStringMethods(unittest.TestCase):
    def test_RequiredGender(self):
        testrequiredgender = Gender('This scholarship is for females only')
        self.assertIsNotNone(testrequiredgender)
        self.assertEqual(testrequiredgender.getRequiredGender(), ['female'])

    def test_GenderFailure(self):
        failrequiredgender = Gender('There is no gender in this string')
        self.assertIsNotNone(failrequiredgender)
        self.assertEqual(failrequiredgender.getRequiredGender(), [])
    def test_betterGender(self):
        testReq = Gender('This scholarship is for <b>Women </b> only')
        self.assertIsNotNone(testReq)
        self.assertEqual(True,testReq.doesMatchExist())

if __name__ == '__main__':
    unittest.main()
