import unittest
from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased
from Classes.GetPivotTagsTitleAbstractEligibility import GetPivotTagsTitleAbstractEligibility


class TestStringMethods(unittest.TestCase):
    def test_returnPredictedTagsFakeOpportunity(self):
        fakeopportunity = ['this is a fake opportunity for a scholarship']
        testclassify = ClassifyFundingTypeKeywordBased(fakeopportunity)
        predictedtag = testclassify.returnPredictedTags()[0]
        self.assertEqual('Scholarship', predictedtag)


if __name__ == '__main__':
    unittest.main()
