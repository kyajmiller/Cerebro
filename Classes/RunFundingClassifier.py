from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased
from Classes.SUDBConnect import SUDBConnect
from Classes.PutThingsInTables import PutThingsInTables


class RunFundingClassifier(object):
    def __init__(self, titleInfoList):
        self.titleInfoList = titleInfoList
        self.db = SUDBConnect()

    def getPredictedTags(self):
        predictedTags = ClassifyFundingTypeKeywordBased(self.titleInfoList).returnPredictedTags()
        return predictedTags

    def getPredictedTagsInsertIntoDB(self, tableName, idColumnName, idsList):
        predictedTags = self.getPredictedTags()
        for i in range(len(predictedTags)):
            tag = predictedTags[i]
            id = idsList[i]
            updateQuery = PutThingsInTables(tableName, ['Tag'], [tag], whereColumnNames=[idColumnName],
                                            whereValues=[id]).createSQLQueryUpdate()
            self.db.insertUpdateOrDelete(updateQuery)
