import unittest
from Classes.GrantForwardLeads import GrantForwardLeads
from Classes.ProcessGrantForwardLeads import ProcessGrantForwardLeads
from Classes.SUDBConnect import SUDBConnect


class TestStringMethods(unittest.TestCase):
    def test_ProcessGrantForwardLeads(self):
        ProcessGrantForwardLeads(
            GrantForwardLeads('engineering').processSearchResultsAndMakeLeadArray())
        db = SUDBConnect()
        rows = db.getRows("select * from dbo.GrantForwardItems")
        self.assertGreater(len(rows), 10)


if __name__ == '__main__':
    unittest.main()
