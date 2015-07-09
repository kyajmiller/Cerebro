import unittest
from Classes.InsertGoogleLeadArrayToGoogleLeadsDatabase import InsertGoogleLeadArrayToGoogleLeadsDatabase
from Classes.SUDBConnect import SUDBConnect


class TestStringMethods(unittest.TestCase):
    def test_InsertGoogleLeadsArrayToGoogleLeadsDatabase(self):
        fakeGoogleLeadsArray = ['title', 'link', 'description']
        InsertGoogleLeadArrayToGoogleLeadsDatabase(fakeGoogleLeadsArray)

        db = SUDBConnect()
        rows = db.getRows("select * from dbo.GoogleLeads where Title='title'")
        self.assertIsNotNone(rows)


if __name__ == '__main__':
    unittest.main()
