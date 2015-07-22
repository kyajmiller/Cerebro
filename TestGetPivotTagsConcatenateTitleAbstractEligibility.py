import unittest
from Classes.GetPivotTagsConcatenateTitleAbstractEligibility import GetPivotTagsConcatenateTitleAbstractEligibility
from Classes.SUDBConnect import SUDBConnect
from Classes.CleanText import CleanText


class TestStringMethods(unittest.TestCase):
    def test_GetPivotTagsConcatenateTitleAbstractEligibility(self):
        # set up
        db = SUDBConnect()
        testConcatenatAbstractEligibility = GetPivotTagsConcatenateTitleAbstractEligibility.getList()
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
