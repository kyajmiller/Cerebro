import unittest
from Classes.InsertGoogleLeadArrayIntoGoogleLeadsDatabase import InsertGoogleLeadArrayIntoGoogleLeadsDatabase
from Classes.SUDBConnect import SUDBConnect


class TestStringMethods(unittest.TestCase):
    def test_InsertGoogleLeadsArrayToGoogleLeadsDatabase(self):
        fakeGoogleLeadsArray = ['title', 'link', 'description']
        InsertGoogleLeadArrayIntoGoogleLeadsDatabase(fakeGoogleLeadsArray)

        db = SUDBConnect()
        rows = db.getRows("select * from dbo.GoogleLeads where Title='title'")
        self.assertIsNotNone(rows)


if __name__ == '__main__':
    unittest.main()
