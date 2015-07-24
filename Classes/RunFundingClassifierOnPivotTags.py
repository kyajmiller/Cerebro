from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased
from Classes.GetPivotTagsTitleAbstractEligibility import GetPivotTagsTitleAbstractEligibility
from Classes.ComputeAccuracy import ComputeAccuracy


class RunFundingClassifierOnPivotTags(object):
    @staticmethod
    def getAccuracy():
        pivotDataList = GetPivotTagsTitleAbstractEligibility.getListConcatenatedItems()
        expectedTags = GetPivotTagsTitleAbstractEligibility.getTags()
        predictedTags = ClassifyFundingTypeKeywordBased(pivotDataList).returnPredictedTags()

        accuracy = ComputeAccuracy(expectedTags, predictedTags).calculateAccuracy()
        print(accuracy)


testclass = RunFundingClassifierOnPivotTags.getAccuracy()
