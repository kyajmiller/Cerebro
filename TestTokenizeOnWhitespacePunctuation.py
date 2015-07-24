import unittest
from Classes.TokenizeOnWhitespacePunctuation import TokenizeOnWhitespacePunctuation


class TestStringMethods(unittest.TestCase):
    def test_TokenizeOnWhitespacePunctuationUnigrams(self):
        # set up
        teststring = 'I like cats and birds.'
        unigrams = ['i', 'like', 'cats', 'and', 'birds']

        # test
        testtokenize = TokenizeOnWhitespacePunctuation(teststring)
        self.assertEqual(unigrams, testtokenize.getUnigrams())

    def test_TokenizeOnWhitespacePunctuationBigrams(self):
        # set up
        teststring = 'I like cats and birds.'
        bigrams = ['i like', 'like cats', 'cats and', 'and birds']

        # test
        testtokenize = TokenizeOnWhitespacePunctuation(teststring)
        self.assertEqual(bigrams, testtokenize.getBigrams())

    def test_TokenizeOnWhitespacePunctuationBothUnigramsBigrams(self):
        # set up
        teststring = 'I like cats and birds.'
        both = ['i', 'like', 'cats', 'and', 'birds', 'i like', 'like cats', 'cats and', 'and birds']

        # test
        testtokenize = TokenizeOnWhitespacePunctuation(teststring)
        self.assertEqual(both, testtokenize.getBothUnigramsBigrams())


if __name__ == '__main__':
    unittest.main()
