from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased
from Classes.CheggLeadsGetDatabaseInfo import CheggLeadsGetDatabaseInfo
from Classes.SUDBConnect import SUDBConnect


class RunFundingClassiferOnCheggLeads(object):
    @staticmethod
    def getPredictedTagsInsertIntoDatabase():
        db = SUDBConnect()

        titleConcatenatedEligibilityApplicationOverviewDescriptionList = CheggLeadsGetDatabaseInfo().getTitleConcatenatedEligibilityAppplictionOverviewDescriptionList()
        predictedTags = ClassifyFundingTypeKeywordBased(
            titleConcatenatedEligibilityApplicationOverviewDescriptionList).returnPredictedTags()
        listCheggLeadsIds = CheggLeadsGetDatabaseInfo().getCheggLeadsIds()

        for i in range(len(predictedTags)):
            tag = predictedTags[i]
            cheggLeadId = listCheggLeadsIds[i]
            db.insertUpdateOrDelete(
                "update dbo.CheggLeads set Tag='" + tag + "' where CheggLeadId='" + cheggLeadId + "'")
