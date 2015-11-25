from Classes.PivotLeadsGetDatabaseInfo import PivotLeadsGetDatabaseInfo
from Classes.PopulateRequirements import PopulateRequirements


class PopulatePivotLeadRequirements(PopulateRequirements):
    def __init__(self, listOfMajors):
        self.listOfMajors = listOfMajors
        self.tag = 'Scholarship'
        self.requirementsTableName = 'PivotLeadRequirements'
        self.requirementsTableColumns = ['PivotLeadId', 'AttributeId', 'AttributeValue']
        PopulateRequirements.__init__(self, self.requirementsTableName, self.requirementsTableColumns)

        self.loopThroughListOfMajorsAndDoStuff()

    def loopThroughListOfMajorsAndDoStuff(self):
        for major in self.listOfMajors:
            pivotLeadsDatabaseInfo = PivotLeadsGetDatabaseInfo(major, self.tag)
            listOfPivotLeadsIds = pivotLeadsDatabaseInfo.getPivotLeadId()
            listOfConcatenatedAbstractEligibilities = pivotLeadsDatabaseInfo.getListStringConcatendatedAbstractEligibility()
            listOfSourceTexts = pivotLeadsDatabaseInfo.getSourceText()

            for i in range(len(listOfPivotLeadsIds)):
                pivotLeadId = str(listOfPivotLeadsIds[i])

                abstractEligibility = listOfConcatenatedAbstractEligibilities[i].strip()
                abstractEligibilitySentences = self.tokenizeIntoSentences(abstractEligibility)

                sourceText = listOfSourceTexts[i]
                sourceTextSentences = self.tokenizeIntoSentences(sourceText)

                gpa = self.getGPAFromSentences(abstractEligibilitySentences)
                dueDate = self.getDueDateFromSentences(sourceTextSentences)

                self.doDatabaseInsertsGPAMajor(pivotLeadId, major, gpa)
                self.insertDueDateIntoPivotLeads(pivotLeadId, dueDate)

    def insertDueDateIntoPivotLeads(self, pivotLeadId, dueDate):
        self.db.insertUpdateOrDeleteDB(
            "update dbo.PivotLeads set DueDate='" + dueDate + "' where PivotLeadId='" + pivotLeadId + "'")