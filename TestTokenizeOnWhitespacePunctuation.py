import unittest
from Classes.TokenizeOnWhitespacePunctuation import TokenizeOnWhitespacePunctuation


class TestStringMethods(unittest.TestCase):
    def test_TokenizeOnWhitespacePunctuationUnigrams(self):
        # set up
        teststring = 'I like cats and birds.'
        unigrams = ['I', 'like', 'cats', 'and', 'birds']

        # test
        testtokenize = TokenizeOnWhitespacePunctuation(teststring)
        self.assertEqual(unigrams, testtokenize.getUnigrams())

    def test_TokenizeOnWhitespacePunctuationBigrams(self):
        # set up
        teststring = 'I like cats and birds.'
        bigrams = ['I like', 'like cats', 'cats and', 'and birds']

        # test
        testtokenize = TokenizeOnWhitespacePunctuation(teststring)
        self.assertEqual(bigrams, testtokenize.getBigrams())

    def test_TokenizeOnWhitespacePunctuationBoth(self):
        # set up
        teststring = 'I like cats and birds.'
        both = ['I', 'like', 'cats', 'and', 'birds', 'I like', 'like cats', 'cats and', 'and birds']

        # test
        testtokenize = TokenizeOnWhitespacePunctuation(teststring)
        self.assertEqual(both, testtokenize.getBothUnigramsBigrams())


if __name__ == '__main__':
    unittest.main()
