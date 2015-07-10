import unittest
from Classes.ProcessGoogleLeads import ProcessGoogleLeads
from Classes.GoogleLeads import GoogleLeads
from Classes.GoogleLeadsUpdateEmptyLinkBody import GoogleLeadsUpdateEmptyLinkBody
from Classes.SUDBConnect import SUDBConnect


class TestStringMethods(unittest.TestCase):
    def test_ProcessGoogleLeads(self):
        # don't run this test too much, it doesn't have a tear-down method to delete what it inserts
        ProcessGoogleLeads(GoogleLeads('engineering scholarships').processSearchResultsAndReturnArrayOfGoogleLeads())
        db = SUDBConnect()
        rows = db.getRows(
            "select * from dbo.GoogleLeads where Link='https://colleges.niche.com/scholarships/major/engineering-all-areas/'")
        self.assertGreater(len(rows[0].Title), 15)
        self.assertGreater(len(rows[0].Description), 30)
        self.assertEqual(len(rows[0].LinkBody), 0)
        GoogleLeadsUpdateEmptyLinkBody()
        rows = db.getRows(
            "select * from dbo.GoogleLeads where Link='https://colleges.niche.com/scholarships/major/engineering-all-areas/'")
        self.assertGreater(len(rows[0].LinkBody), 50)


if __name__ == '__main__':
    unittest.main()
