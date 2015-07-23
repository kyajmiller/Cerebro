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
        rows = db.getRows("select * from dbo.PivotTags")
        title = rows[0].Name
        abstract = rows[0].Abstract
        eligibility = rows[0].Eligibility
        combo = '%s %s %s' % (title, abstract, eligibility)
        combo = CleanText.cleanALLtheText(combo)

        self.assertEqual(firstItem, combo)

if __name__ == '__main__':
    unittest.main()
