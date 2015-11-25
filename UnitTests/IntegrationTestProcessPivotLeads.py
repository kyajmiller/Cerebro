import unittest
from Classes.PivotLeads import PivotLeads
from Classes.ProcessPivotLeads import ProcessPivotLeads
from Classes.SUDBConnect import SUDBConnect


class TestStringMethods(unittest.TestCase):
    def test_ProcessPivotLeads(self):
        ProcessPivotLeads(PivotLeads('engineering', isTest=True).processSearchResultsAndMakeLeadArray())
        db = SUDBConnect()
        rows = db.getRowsDB("select * from dbo.PivotLeads where Keyword='engineering'")
        self.assertGreaterEqual(len(rows), 10)


if __name__ == '__main__':
    unittest.main()
