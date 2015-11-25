import unittest
from Classes.GrantForwardItemsGetDatabaseInfo import GrantForwardItemsGetDatabaseInfo
from Classes.CleanText import CleanText
from Classes.SUDBConnect import SUDBConnect


class TestStringMethods(unittest.TestCase):
    def test_ListOfItemsList(self):
        # set up
        db = SUDBConnect()
        keyword = 'Accounting'
        testListTitleDescriptionEligibilityPivotId = GrantForwardItemsGetDatabaseInfo(
            keyword).getTitleDescriptionList()
        firstList = testListTitleDescriptionEligibilityPivotId[0]
        testTitle = firstList[0]
        testDescription = firstList[1]

        # test
        rows = db.getRowsDB("select * from dbo.GrantForwardItems where Keyword='" + keyword + "'")
        title = CleanText.cleanALLtheText(rows[0].Name)
        description = CleanText.cleanALLtheText(rows[0].Description)

        self.assertEqual(title, testTitle)
        self.assertEqual(description, testDescription)

    def test_getListConcatenatedDescriptionEligibility(self):
        # set up
        db = SUDBConnect()
        keyword = 'East Asian Studies'
        testListConcatenatedDescriptionEligibility = GrantForwardItemsGetDatabaseInfo(
            keyword=keyword).getListStringConcatenatedDescriptionEligibility()
        firstCombo = testListConcatenatedDescriptionEligibility[0]

        # test
        rows = db.getRowsDB("select * from dbo.GrantForwardItems where Keyword='" + keyword + "'")
        description = CleanText.cleanALLtheText(rows[0].Description)
        eligibility = CleanText.cleanALLtheText(rows[0].Eligibility)
        testCombo = '%s %s' % (description, eligibility)

        self.assertEqual(testCombo, firstCombo)


if __name__ == '__main__':
    unittest.main()
