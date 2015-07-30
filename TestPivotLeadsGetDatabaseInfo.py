import unittest
from Classes.PivotLeadsGetDatabaseInfo import PivotLeadsGetDatabaseInfo
from Classes.CleanText import CleanText
from Classes.SUDBConnect import SUDBConnect


class TestStringMethods(unittest.TestCase):
    def test_GetConcatenatedItemsString(self):
        # set up
        db = SUDBConnect()
        keyword = 'Accounting'
        testConcatenatedTitleAbstractEligibility = PivotLeadsGetDatabaseInfo(
            keyword).getListStringConcatenatedTitleAbstractEligibility()
        firstItem = testConcatenatedTitleAbstractEligibility[0]

        # test
        rows = db.getRows("select * from dbo.PivotLeads where Keyword='" + keyword + "'")
        title = rows[0].Name
        abstract = rows[0].Abstract
        eligibility = rows[0].Eligibility
        combo = '%s %s %s' % (title, abstract, eligibility)
        combo = CleanText.cleanALLtheText(combo)

        self.assertEqual(combo, firstItem)

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
