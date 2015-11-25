import unittest
from Classes.GoogleLeadsUpdateEmptyLinkBody import GoogleLeadsUpdateEmptyLinkBody
from Classes.InsertGoogleLeadArrayIntoGoogleLeadsDatabase import InsertGoogleLeadArrayIntoGoogleLeadsDatabase
from Classes.SUDBConnect import SUDBConnect


class TestStringMethods(unittest.TestCase):
    def test_GoogleLeadsUpdateEmptyLinkBody(self):
        # set up
        db = SUDBConnect()
        db.insertUpdateOrDeleteDB(
            "delete from dbo.GoogleLeads where Link='http://colleges.fastweb.com/d-foreign-languages-literatures-and-linguistics'")

        fakegoogleleadsarray = ['title', 'http://colleges.fastweb.com/d-foreign-languages-literatures-and-linguistics',
                                'description']
        InsertGoogleLeadArrayIntoGoogleLeadsDatabase(fakegoogleleadsarray)
        rows1 = db.getRowsDB(
            "select * from dbo.GoogleLeads where Link='http://colleges.fastweb.com/d-foreign-languages-literatures-and-linguistics'")
        self.assertEqual('title', rows1[0].Title)

        # actual test of class
        GoogleLeadsUpdateEmptyLinkBody()
        rows2 = db.getRowsDB(
            "select * from dbo.GoogleLeads where Link='http://colleges.fastweb.com/d-foreign-languages-literatures-and-linguistics'")
        self.assertEqual('title', rows2[0].Title)
        self.assertGreater(len(rows2[0].LinkBody), 10)

        # tear down
        db.insertUpdateOrDeleteDB(
            "delete from dbo.GoogleLeads where Link='http://colleges.fastweb.com/d-foreign-languages-literatures-and-linguistics'")


if __name__ == '__main__':
    unittest.main()
