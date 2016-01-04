import unittest
from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased


class TestStringMethods(unittest.TestCase):
    def test_returnPredictedTagsFakeOpportunity(self):
        fakeTitle = 'fakeTitle'
        fakeText = 'this is a fake opportunity for a scholarship'
        fakeOpportunity = [[fakeTitle, fakeText]]
        testclassify = ClassifyFundingTypeKeywordBased(fakeOpportunity)
        predictedtag = testclassify.returnPredictedTags()[0]
        self.assertEqual('Scholarship', predictedtag)

    def test_returnPredictedTagsFakeOpportunityAnother(self):
        fakeTitle = 'fakeTitle'
        fakeText = 'this is a fake opportunity for a grant'
        fakeOpportunity = [[fakeTitle, fakeText]]
        testclassify = ClassifyFundingTypeKeywordBased(fakeOpportunity)
        predictedtag = testclassify.returnPredictedTags()[0]
        self.assertEqual('Grant', predictedtag)


if __name__ == '__main__':
    unittest.main()
