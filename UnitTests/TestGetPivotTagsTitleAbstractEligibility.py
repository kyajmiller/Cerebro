import unittest
from Classes.GetPivotTagsTitleAbstractEligibility import GetPivotTagsTitleAbstractEligibility
from Classes.SUDBConnect import SUDBConnect
from Classes.CleanText import CleanText


class TestStringMethods(unittest.TestCase):
    def test_GetPivotTagsTitleAbstractEligibilityConcatenatedItems(self):
        # set up
        db = SUDBConnect()
        testConcatenatAbstractEligibility = GetPivotTagsTitleAbstractEligibility.getListConcatenatedItems()
        firstItem = testConcatenatAbstractEligibility[0]

        # test
        rows = db.getRowsDB("select * from dbo.PivotTags")
        title = rows[0].Name
        abstract = rows[0].Abstract
        eligibility = rows[0].Eligibility
        combo = '%s %s %s' % (title, abstract, eligibility)
        combo = CleanText.cleanALLtheText(combo)

        self.assertEqual(firstItem, combo)

    def test_GetPivotTagsTitleAbstractEligibilityListItems(self):
        # set up
        db = SUDBConnect()
        testListItems = GetPivotTagsTitleAbstractEligibility.getListofListofItems()
        firstList = testListItems[0]
        testtitle = firstList[0]
        testabstract = firstList[1]
        testeligibility = firstList[2]

        # test
        rows = db.getRowsDB("select * from dbo.PivotTags")
        title = CleanText.cleanALLtheText(rows[0].Name)
        abstract = CleanText.cleanALLtheText(rows[0].Abstract)
        eligibility = CleanText.cleanALLtheText(rows[0].Eligibility)

        self.assertEqual(title, testtitle)
        self.assertEqual(abstract, testabstract)
        self.assertEqual(eligibility, testeligibility)

if __name__ == '__main__':
    unittest.main()
