import unittest
import re
from Classes.PivotLeads import PivotLeads


class TestStringMethods(unittest.TestCase):
    def test_PivotLeads(self):
        testPivotLeads = PivotLeads('engineering', isTest=True).processSearchResultsAndMakeLeadArray()
        self.assertIsNotNone(testPivotLeads)
        firstArray = testPivotLeads[0]
        self.assertEqual(len(firstArray), 13)
        firstArrayLink = firstArray[11]
        self.assertTrue(re.search('^https?://', firstArrayLink))

    def test_PivotLeadsTestNextPage(self):
        testPivotLeads = PivotLeads('engineering').processSearchResultsAndMakeLeadArray()
        self.assertIsNotNone(testPivotLeads)
        firstArray = testPivotLeads[0]
        self.assertEqual(len(firstArray), 13)
        firstArrayLink = firstArray[11]
        self.assertTrue(re.search('^https?://', firstArrayLink))


if __name__ == '__main__':
    unittest.main()
