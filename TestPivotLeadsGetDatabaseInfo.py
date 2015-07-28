import unittest
from Classes.PivotLeadsGetDatabaseInfo import PivotLeadsGetDatabaseInfo
from Classes.CleanText import CleanText
from Classes.SUDBConnect import SUDBConnect


class TestStringMethods(unittest.TestCase):
    def test_GetConcatenatedItemsString(self):
        # set up
        db = SUDBConnect()
        keyword = 'Accounting'
        testConcatenatedTitleAbstractEligibility = PivotLeadsGetDatabaseInfo.getListConcatenatedItems(
            keyword)
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
        testListTitleAbstractEligibilityPivotId = PivotLeadsGetDatabaseInfo.getTitleAbstractEligibilityPivotLeadIdList(
            keyword)
        firstList = testListTitleAbstractEligibilityPivotId[0]
        testTitle = firstList[0]
        testAbstract = firstList[1]
        testEligibility = firstList[2]
        testPivotLeadId = firstList[3]

        # test
        rows = db.getRows("select * from dbo.PivotLeads where Keyword='" + keyword + "'")
        title = CleanText.cleanALLtheText(rows[0].Name)
        abstract = CleanText.cleanALLtheText(rows[0].Abstract)
        eligibility = CleanText.cleanALLtheText(rows[0].Eligibility)
        pivotLeadId = str(rows[0].PivotLeadId)

        self.assertEqual(title, testTitle)
        self.assertEqual(abstract, testAbstract)
        self.assertEqual(eligibility, testEligibility)
        self.assertEqual(pivotLeadId, testPivotLeadId)


if __name__ == '__main__':
    unittest.main()
