import unittest
from Classes.GoogleLeads import GoogleLeads
from Classes.ProcessGoogleLeads import ProcessGoogleLeads
from Classes.GoogleLeadsUpdateEmptyLinkBody import GoogleLeadsUpdateEmptyLinkBody
from Classes.SUDBConnect import SUDBConnect


class TestStringMethods(unittest.TestCase):
    def test_ProcessGoogleLeads(self):
        ProcessGoogleLeads(
            GoogleLeads('engineering scholarships').processSearchResultsAndReturnArrayOfGoogleLeads()[0:9])
        db = SUDBConnect()
        rows = db.getRows("select * from dbo.GoogleLeads")
        self.assertGreater(len(rows), 1)
        # self.assertEqual(len(rows), 100)

if __name__ == '__main__':
    unittest.main()
