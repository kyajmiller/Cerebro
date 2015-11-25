import unittest
from Classes.InsertScholarshipArrayIntoDatabase import InsertScholarshipArrayIntoDatabase
from Classes.PullPageLinkTitleDescriptionToArray import PullPageLinkTitleDescriptionToArray
from Classes.SUDBConnect import SUDBConnect


class TestStringMethods(unittest.TestCase):
    def test_InsertScholarshipArrayIntoDatabase(self):
        db = SUDBConnect()
        db.insertUpdateOrDeleteDB(
            "delete from dbo.LinkCrawlerHrefs where linkurl='http://colleges.fastweb.com/d-foreign-languages-literatures-and-linguistics'")
        InsertScholarshipArrayIntoDatabase.doInsert(PullPageLinkTitleDescriptionToArray(
            'http://colleges.fastweb.com/d-foreign-languages-literatures-and-linguistics').doArray())
        rows = db.getRowsDB(
            "select * from LinkCrawlerHrefs where linkurl='http://colleges.fastweb.com/d-foreign-languages-literatures-and-linguistics'")
        self.assertEqual(rows[0].LinkUrl, 'http://colleges.fastweb.com/d-foreign-languages-literatures-and-linguistics')


if __name__ == '__main__':
    unittest.main()
