from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased
from Classes.GetPivotTagsTitleAbstractEligibility import GetPivotTagsTitleAbstractEligibility
from Classes.ComputeAccuracy import ComputeAccuracy
from Classes.SUDBConnect import SUDBConnect


class RunFundingClassifierOnPivotTags(object):
    @staticmethod
    def getOverallAccuracy():
        pivotDataList = GetPivotTagsTitleAbstractEligibility.getListofListofItems()
        expectedTags = GetPivotTagsTitleAbstractEligibility.getTags()
        predictedTags = ClassifyFundingTypeKeywordBased(pivotDataList).returnPredictedTags()

        accuracy = ComputeAccuracy(expectedTags, predictedTags).calculateAccuracy()
        print(accuracy)

    @staticmethod
    def insertPredictedTagsIntoDatabase():
        pivotDataList = GetPivotTagsTitleAbstractEligibility.getListofListofItems()
        predictedTags = ClassifyFundingTypeKeywordBased(pivotDataList).returnPredictedTags()
        db = SUDBConnect()

        for i in range(len(predictedTags)):
            predictedTag = predictedTags[i]
            pivotTagId = str(i + 1)
            db.insertUpdateOrDelete(
                "update dbo.PivotTags set Predicted='" + predictedTag + "' where PivotTagId='" + pivotTagId + "'")
