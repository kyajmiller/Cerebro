import unittest
from Classes.PivotLeadsGetDatabaseInfo import PivotLeadsGetDatabaseInfo
from Classes.CleanText import CleanText
from Classes.SUDBConnect import SUDBConnect


class TestStringMethods(unittest.TestCase):
    def test_ListOfItemsList(self):
        # set up
        db = SUDBConnect()
        keyword = 'Accounting'
        testListTitleAbstractEligibilityPivotId = PivotLeadsGetDatabaseInfo(
            keyword).getTitleAbstractList()
        firstList = testListTitleAbstractEligibilityPivotId[0]
        testTitle = firstList[0]
        testAbstract = firstList[1]

        # test
        rows = db.getRows("select * from dbo.PivotLeads where Keyword='" + keyword + "'")
        title = CleanText.cleanALLtheText(rows[0].Name)
        abstract = CleanText.cleanALLtheText(rows[0].Abstract)

        self.assertEqual(title, testTitle)
        self.assertEqual(abstract, testAbstract)


if __name__ == '__main__':
    unittest.main()
