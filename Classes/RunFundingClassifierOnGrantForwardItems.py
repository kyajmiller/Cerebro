from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased
from Classes.GrantForwardItemsGetDatabaseInfo import GrantForwardItemsGetDatabaseInfo
from Classes.SUDBConnect import SUDBConnect
from Classes.CleanText import CleanText


class GrantForwardItemsRunFundingClassifier(object):
    @staticmethod
    def getPredictedTagsInsertIntoDatabase():
        keywordsList = GrantForwardItemsGetDatabaseInfo.getKeywords()
        db = SUDBConnect()

        for keyword in keywordsList:
            keyword = CleanText.cleanALLtheText(keyword)
            titleDescriptionList = GrantForwardItemsGetDatabaseInfo(keyword=keyword).getTitleDescriptionList()
            predictedTags = ClassifyFundingTypeKeywordBased(titleDescriptionList).returnPredictedTags()
            listGrantForwardItemIds = GrantForwardItemsGetDatabaseInfo(keyword=keyword).getGrantForwardItemIds()

            for i in range(len(predictedTags)):
                tag = predictedTags[i]
                grantForwardItemId = listGrantForwardItemIds[i]
                db.insertUpdateOrDeleteDB(
                    "update dbo.GrantForwardItems set Tag='" + tag + "' where GrantForwardItemId='" + grantForwardItemId + "'")


GrantForwardItemsRunFundingClassifier.getPredictedTagsInsertIntoDatabase()
