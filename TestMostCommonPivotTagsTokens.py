import unittest
from Classes.MostCommonPivotTagsTokens import MostCommonPivotTagsTokens
from nltk import FreqDist


class TestStringMethods(unittest.TestCase):
    def test_MostCommonPivotTagsTokens(self):
        testMostCommon = MostCommonPivotTagsTokens(20).getMostCommon()


if __name__ == '__main__':
    unittest.main()
