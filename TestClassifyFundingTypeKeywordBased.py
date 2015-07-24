import unittest
from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased


class TestStringMethods(unittest.TestCase):
    def test_returnPredictedTagsFakeOpportunity(self):
        fakeopportunity = ['this is a fake opportunity for a scholarship']
        testclassify = ClassifyFundingTypeKeywordBased(fakeopportunity)
        predictedtag = testclassify.returnPredictedTags()[0]
        self.assertEqual('Scholarship', predictedtag)

    def test_returnPredictedTagsFakeOpportunityAnother(self):
        fakeopportunity = ['this is a fake opportunity for a grant']
        testclassify = ClassifyFundingTypeKeywordBased(fakeopportunity)
        predictedtag = testclassify.returnPredictedTags()[0]
        self.assertEqual('Grant', predictedtag)


if __name__ == '__main__':
    unittest.main()
