from Classes.ClassifyBadScholarships import ClassifyBadScholarships
from Classes.SUDBConnect import SUDBConnect
from Classes.PutThingsInTables import PutThingsInTables


class RunBadScholarshipClassifier(object):
    def __init__(self, sponsorList, infoTextList):
        self.sponsorList = sponsorList
        self.infoTextList = infoTextList

        self.db = SUDBConnect()

    def getPredictedBad(self):
        predictedBad = ClassifyBadScholarships(self.sponsorList, self.infoTextList).loopThroughLeadsAndDoStuff()
        return predictedBad

    def getPredictedBadInsertIntoDatabase(self, tableName, idColumnName, idsList):
        predictedBad = self.getPredictedBad()
        for i in range(len(predictedBad)):
            badScholarship = predictedBad[i]
            id = idsList[i]
            updateQuery = PutThingsInTables(tableName, ['BadScholarship'], [badScholarship],
                                            whereColumnNames=[idColumnName], whereValues=[id]).createSQLQueryUpdate()
            self.db.insertUpdateOrDeleteDB(updateQuery)
