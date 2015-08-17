from Classes.PopulateRequirements import PopulateRequirements
from Classes.CheggLeadsGetDatabaseInfo import CheggLeadsGetDatabaseInfo


class PopulateCheggRequirements(PopulateRequirements):
    def __init__(self):
        self.tableName = 'CheggRequirements'
        self.tableColumns = ['CheggLeadId', 'AttributeId', 'AttributeValue']
        PopulateRequirements.__init__(self, self.tableName, self.tableColumns)
        self.tag = 'Scholarship'

    def loopThroughLeadsAndDoStuff(self):
        cheggLeadsDatabaseInfo = CheggLeadsGetDatabaseInfo(self.tag)
        listOfCheggLeadsIds = cheggLeadsDatabaseInfo.getCheggLeadsIds()
        listConcatenatedEligibilityApplicationOverview = cheggLeadsDatabaseInfo.getConcatenatedEligibilityApplicationOverview()

        for i in range(len(listOfCheggLeadsIds)):
            cheggLeadId = listOfCheggLeadsIds[i]

            eligibilityApplicationOverview = listConcatenatedEligibilityApplicationOverview[i]
            eligibilityApplicationOverviewSentences = self.tokenizeIntoSentences(eligibilityApplicationOverview)

            gpa = self.getGPAFromSentences(eligibilityApplicationOverviewSentences)
            majors = self.getMajorFromSentences(eligibilityApplicationOverviewSentences)

            self.doDatabaseInsertsGPAMajor(cheggLeadId, gpa, majors)


PopulateCheggRequirements().loopThroughLeadsAndDoStuff()
