from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased
from Classes.FatomeiLeadsGetDatabaseInfo import FatomeiLeadsGetDatabaseInfo
from Classes.SUDBConnect import SUDBConnect


class RunFundingClassifierOnFatomeiLeads(object):
    @staticmethod
    def getPredictedTagsInsertIntoDatabase():
        db = SUDBConnect()

        titleDescriptionList = FatomeiLeadsGetDatabaseInfo().getTitleDescriptionList()
        predictedTags = ClassifyFundingTypeKeywordBased(titleDescriptionList).returnPredictedTags()
        listFatomeiLeadsIds = FatomeiLeadsGetDatabaseInfo().getFatomeiLeadIds()

        for i in range(len(predictedTags)):
            tag = predictedTags[i]
            fatomeiLeadId = listFatomeiLeadsIds[i]
            db.insertUpdateOrDelete(
                "update dbo.FatomeiLeads set Tag='" + tag + "' where FatomeiLeadId='" + fatomeiLeadId + "'")


RunFundingClassifierOnFatomeiLeads.getPredictedTagsInsertIntoDatabase()
