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
        self.assertEqual('title', rows[0].Title)
        self.assertEqual('link', rows[0].Link)
        self.assertEqual('description', rows[0].Description)

        db.insertUpdateOrDelete("delete from dbo.GoogleLeads where Title='title'")


if __name__ == '__main__':
    unittest.main()
