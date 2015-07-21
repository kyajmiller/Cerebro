import unittest
from Classes.GetPivotTagsConcatenateAbstractEligibility import GetPivotTagsConcatenateAbstractEligibility
from Classes.SUDBConnect import SUDBConnect
from Classes.CleanText import CleanText


class TestStringMethods(unittest.TestCase):
    def test_GetPivotTagsConcatenateAbstractEligibility(self):
        # set up
        db = SUDBConnect()
        testConcatenatAbstractEligibility = GetPivotTagsConcatenateAbstractEligibility.getList()
        firstItem = testConcatenatAbstractEligibility[0]

        # test
        rows = db.getRows("select * from dbo.PivotTags")
        abstract = rows[0].Abstract
        eligibility = rows[0].Eligibility
        combo = '%s %s' % (abstract, eligibility)
        combo = CleanText.cleanALLtheText(combo)

        self.assertEqual(firstItem, combo)

if __name__ == '__main__':
    unittest.main()
