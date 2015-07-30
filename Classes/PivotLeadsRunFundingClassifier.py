from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased
from Classes.PivotLeadsGetDatabaseInfo import PivotLeadsGetDatabaseInfo
from Classes.SUDBConnect import SUDBConnect
from Classes.CleanText import CleanText


class PivotLeadsRunFundingClassifier(object):
    @staticmethod
    def getPredictedTagsInsertIntoDatabase():
        keywordsList = PivotLeadsGetDatabaseInfo.getKeywords()
        for keyword in keywordsList:
            keyword = CleanText.cleanALLtheText(keyword)
            titleAbstractList = PivotLeadsGetDatabaseInfo(keyword).getTitleAbstractList()
            predictedTags = ClassifyFundingTypeKeywordBased(titleAbstractList).returnPredictedTags()
            listPivotLeadIds = PivotLeadsGetDatabaseInfo(keyword).getPivotLeadId()

            db = SUDBConnect()
            for i in range(len(predictedTags)):
                tag = predictedTags[i]
                pivotLeadId = listPivotLeadIds[i]
                db.insertUpdateOrDelete(
                    "update dbo.PivotLeads set Tag='" + tag + "' where PivotLeadId='" + pivotLeadId + "'")


PivotLeadsRunFundingClassifier.getPredictedTagsInsertIntoDatabase()
