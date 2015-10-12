import unittest
import re
from Classes.GrantForwardLeads import GrantForwardLeads


class TestStringMethods(unittest.TestCase):
    def test_GrantForwardLeads(self):
        testGrantForwardLeads = GrantForwardLeads('engineering', isTest=True).processSearchResultsAndMakeLeadArray()
        self.assertIsNotNone(testGrantForwardLeads)
        firstArray = testGrantForwardLeads[0]
        self.assertEqual(len(firstArray), 11)
        firstArrayLink = firstArray[9]
        self.assertTrue(re.search('^https?://', firstArrayLink))


if __name__ == '__main__':
    unittest.main()
