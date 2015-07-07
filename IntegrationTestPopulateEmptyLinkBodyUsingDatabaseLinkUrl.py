import unittest
from Classes.PopulateEmptyLinkBodyUsingDatabaseLinkUrl import PopulateEmptyLinkBodyUsingDatabaseLinkUrl
from Classes.SUDBConnect import SUDBConnect
from Classes.InsertScholarshipArrayIntoDatabase import InsertScholarshipArrayIntoDatabase
from Classes.PullPageLinkTitleDescriptionToArray import PullPageLinkTitleDescriptionToArray


class TestStringMethods(unittest.TestCase):
    def test_PopulateEmptyLinkBodyUsingDatabaseLinkUrl(self):
        # need to first insert a link that has an empty linkbody for testing
        db = SUDBConnect()
        db.insertUpdateOrDelete(
            "delete from dbo.LinkCrawlerHrefs where linkurl='http://colleges.fastweb.com/d-foreign-languages-literatures-and-linguistics'")
        InsertScholarshipArrayIntoDatabase.doInsert(PullPageLinkTitleDescriptionToArray(
            'http://colleges.fastweb.com/d-foreign-languages-literatures-and-linguistics').doArray())
        rows = db.getRows(
            "select * from LinkCrawlerHrefs where linkurl='http://colleges.fastweb.com/d-foreign-languages-literatures-and-linguistics'")
        self.assertEqual(rows[0].LinkUrl, 'http://colleges.fastweb.com/d-foreign-languages-literatures-and-linguistics')

        # now actual testing of the class
        PopulateEmptyLinkBodyUsingDatabaseLinkUrl()

        rows = db.getRows(
            "select * from LinkCrawlerHrefs where linkurl='http://colleges.fastweb.com/d-foreign-languages-literatures-and-linguistics'")
        self.assertGreater(len(rows[0].LinkBody), 10)


if __name__ == '__main__':
    unittest.main()
