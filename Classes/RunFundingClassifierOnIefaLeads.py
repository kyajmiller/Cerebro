from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased
from Classes.IefaLeadsGetDatabaseInfo import IefaLeadsGetDatabaseInfo
from Classes.SUDBConnect import SUDBConnect


class RunFundingClassifierOnIefaLeads(object):
    @staticmethod
    def getPredictedTagsInsertIntoDatabase():
        db = SUDBConnect()

        titleConcatenatedDescriptionOtherCriteriaList = IefaLeadsGetDatabaseInfo().getTitleConcatenatedDescriptionOtherCriteriaList()
        predictedTags = ClassifyFundingTypeKeywordBased(
            titleConcatenatedDescriptionOtherCriteriaList).returnPredictedTags()
        listIefaLeadsIds = IefaLeadsGetDatabaseInfo().getIefaLeadsIds()

        for i in range(len(predictedTags)):
            tag = predictedTags[i]
            iefaLeadId = listIefaLeadsIds[i]
            db.insertUpdateOrDelete("update dbo.IefaLeads set Tag='" + tag + "' where IefaLeadId='" + iefaLeadId + "'")


RunFundingClassifierOnIefaLeads.getPredictedTagsInsertIntoDatabase()
