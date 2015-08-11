from Classes.PopulateRequirements import PopulateRequirements
from Classes.FatomeiLeadsGetDatabaseInfo import FatomeiLeadsGetDatabaseInfo


class PopulateFatomeiLeadRequirements(PopulateRequirements):
    def __init__(self):
        self.tableName = 'FatomeiLeadRequirements'
        self.columnNames = ['FatomeiLeadId', 'AttributeId', 'AttributeValue']
        PopulateRequirements.__init__(self, self.tableName, self.columnNames)
        self.tag = 'Scholarship'

    def loopThroughLeadsAndDoStuff(self):
        fatomeiLeadsDatabaseInfo = FatomeiLeadsGetDatabaseInfo(self.tag)
        listOfFatomeiLeadsIds = fatomeiLeadsDatabaseInfo.getFatomeiLeadIds()
        listConcatenatedDescriptionsSourceText = fatomeiLeadsDatabaseInfo.getConcatenatedDescriptionsSourceText()

        for i in range(len(listOfFatomeiLeadsIds)):
            fatomeiLeadId = listOfFatomeiLeadsIds[i]

            descriptionSourceText = listConcatenatedDescriptionsSourceText[i]
            descriptionSourceTextSentences = self.tokenizeIntoSentences(descriptionSourceText)

            gpa = self.getGPAFromSentences(descriptionSourceTextSentences)
            majors = self.getMajorFromSentences(descriptionSourceTextSentences)

            self.doDatabaseInsertsGPAMajor(fatomeiLeadId, gpa, majors)


PopulateFatomeiLeadRequirements().loopThroughLeadsAndDoStuff()
