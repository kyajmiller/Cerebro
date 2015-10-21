import unittest
from Classes.GrantForwardLeads import GrantForwardLeads
from Classes.ProcessGrantForwardLeads import ProcessGrantForwardLeads
from Classes.SUDBConnect import SUDBConnect


class TestStringMethods(unittest.TestCase):
    def test_ProcessGrantForwardLeads(self):
        ProcessGrantForwardLeads(
            GrantForwardLeads('engineering', isTest=True).processSearchResultsAndMakeLeadArray())
        db = SUDBConnect()
        rows = db.getRows("select * from dbo.GrantForwardItems")
        self.assertGreaterEqual(len(rows), 10)

    def test_ProcessGrantForwardLeadsNoResults(self):
        ProcessGrantForwardLeads(
            GrantForwardLeads('Anthropology MA)').processSearchResultsAndMakeLeadArray())


if __name__ == '__main__':
    unittest.main()
