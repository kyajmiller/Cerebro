from Classes.FastWebLeadsGetDatabaseInfo import FastWebLeadsGetDatabaseInfo
from Classes.PopulateRequirements import PopulateRequirements


class PopulateFastWebLeadRequirements(PopulateRequirements):
    def __init__(self):
        self.tableName = 'FastWebLeadRequirements'
        self.columnNames = ['FastWebLeadId', 'AttributeId', 'AttributeValue']
        PopulateRequirements.__init__(self, self.tableName, self.columnNames)
        self.tag = 'Scholarship'

    def loopThroughLeadsAndDoStuff(self):
        fastWebLeadsDatabaseInfo = FastWebLeadsGetDatabaseInfo(self.tag)
        listOfFastWebLeadsIds = fastWebLeadsDatabaseInfo.getFastWebLeadsIds()
        listConcatenatedDescriptionsSourceText = fastWebLeadsDatabaseInfo.getConcatenatedDescriptionSourceText()

        for i in range(len(listOfFastWebLeadsIds)):
            fastWebLeadId = listOfFastWebLeadsIds[i]

            descriptionSourceText = listConcatenatedDescriptionsSourceText[i]
            descriptionSourceTextSentences = self.tokenizeIntoSentences(descriptionSourceText)

            gpa = self.getGPAFromSentences(descriptionSourceTextSentences)
            majors = self.getMajorFromSentences(descriptionSourceTextSentences)

            self.doDatabaseInsertsGPAMajor(fastWebLeadId, gpa, majors)


PopulateFastWebLeadRequirements().loopThroughLeadsAndDoStuff()
