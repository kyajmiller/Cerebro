import unittest
from Classes.GoogleLeads import GoogleLeads


class TestStringMethods(unittest.TestCase):
    def test_GoogleLeads(self):
        testgoogleleadsarray = GoogleLeads('engineering scholarships').goToGoogleAndGetResults()
        self.assertIsNotNone(testgoogleleadsarray[0])
        self.assertEqual(3, len(testgoogleleadsarray[0]))

    def test_GoogleLeadsElseStatement(self):
        testgoogleleadsuneventhangs = GoogleLeads('engineering').goToGoogleAndGetResults()



if __name__ == '__main__':
    unittest.main()
