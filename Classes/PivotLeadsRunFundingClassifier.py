from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased
from Classes.PivotLeadsGetTitleAbstractEligibility import PivotLeadsGetTitleAbstractEligibility
from Classes.SUDBConnect import SUDBConnect


class PivotLeadsRunFundingClassifier(object):
    @staticmethod
    def getPredictedTagsInsertIntoDatabase():
        keywordsList = PivotLeadsGetTitleAbstractEligibility.getKeywords()
        for keyword in keywordsList:
            rowDataList = PivotLeadsGetTitleAbstractEligibility.getListofListofItems(keyword)
            predictedTags = ClassifyFundingTypeKeywordBased(rowDataList).returnPredictedTags()
            listPivotLeadIds = []
            for row in rowDataList:
                listPivotLeadIds.append(row[3])

            db = SUDBConnect()
            for i in range(len(predictedTags)):
                tag = predictedTags[i]
                pivotLeadId = listPivotLeadIds[i]
                db.insertUpdateOrDelete(
                    "update dbo.PivotLeads set Tag='" + tag + "' where PivotLeadId='" + pivotLeadId + "'")
