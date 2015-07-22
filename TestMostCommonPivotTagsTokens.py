import unittest
from Classes.MostCommonPivotTagsTokens import MostCommonPivotTagsTokens


class TestStringMethods(unittest.TestCase):
    def test_MostCommonPivotTagsTokens(self):
        testMostCommon = MostCommonPivotTagsTokens(100).getMostCommon()
        for wordWithFrequencyTuple in testMostCommon:
            print(wordWithFrequencyTuple[0])


if __name__ == '__main__':
    unittest.main()
