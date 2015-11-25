import unittest
from Classes.GoogleLeads import GoogleLeads
from Classes.ProcessGoogleLeads import ProcessGoogleLeads
from Classes.SUDBConnect import SUDBConnect


class TestStringMethods(unittest.TestCase):
    def test_ProcessGoogleLeads(self):
        ProcessGoogleLeads(
            GoogleLeads('engineering scholarships').processSearchResultsAndReturnArrayOfGoogleLeads())
        db = SUDBConnect()
        rows = db.getRowsDB("select * from dbo.GoogleLeads")
        self.assertGreater(len(rows), 10)

if __name__ == '__main__':
    unittest.main()
