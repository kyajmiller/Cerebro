from Classes.PopulateRequirements import PopulateRequirements
from Classes.IefaLeadsGetDatabaseInfo import IefaLeadsGetDatabaseInfo


class PopulateIefaLeadRequirements(PopulateRequirements):
    def __init__(self):
        self.tableName = 'IefaLeadRequirements'
        self.tableColumns = ['IefaLeadId', 'AttributeId', 'AttributeValue']
        PopulateRequirements.__init__(self, self.tableName, self.tableColumns)
        self.tag = 'Scholarship'

    def loopThroughLeadsAndDoStuff(self):
        iefaLeadsDatabaseInfo = IefaLeadsGetDatabaseInfo(self.tag)
        listOfIefaLeadsIds = iefaLeadsDatabaseInfo.getIefaLeadsIds()
        listOfConcatenatedDescriptionOtherCriteria = iefaLeadsDatabaseInfo.getConcatenatedDescriptionOtherCriteria()

        for i in range(len(listOfIefaLeadsIds)):
            iefaLeadId = listOfIefaLeadsIds[i]

            descriptionOtherCriteria = listOfConcatenatedDescriptionOtherCriteria[i]
            descriptionOtherCriteriaSentences = self.tokenizeIntoSentences(descriptionOtherCriteria)

            gpa = self.getGPAFromSentences(descriptionOtherCriteriaSentences)
            majors = self.getMajorFromSentences(descriptionOtherCriteriaSentences)

            self.doDatabaseInsertsGPAMajor(iefaLeadId, gpa, majors)


PopulateIefaLeadRequirements().loopThroughLeadsAndDoStuff()
