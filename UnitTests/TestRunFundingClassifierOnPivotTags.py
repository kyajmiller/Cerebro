import unittest
from Classes.RunFundingClassifierOnPivotTags import RunFundingClassifierOnPivotTags


class TestStringMethods(unittest.TestCase):
    def test_GetOverallAccuracy(self):
        RunFundingClassifierOnPivotTags.getOverallAccuracy()

    def test_InsertPredictedTagsIntoDatabase(self):
        RunFundingClassifierOnPivotTags.insertPredictedTagsIntoDatabase()


if __name__ == '__main__':
    unittest.main()
