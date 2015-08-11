from Classes.GrantForwardItemsGetDatabaseInfo import GrantForwardItemsGetDatabaseInfo
from Classes.PopulateRequirements import PopulateRequirements


class PopulateGrantForwardRequirements(PopulateRequirements):
    def __init__(self, listOfMajors):
        self.listOfMajors = listOfMajors
        self.tag = 'Scholarship'
        self.requirementsTableName = 'GrantForwardRequirements'
        self.requirementsTableColumns = ['GrantForwardId', 'AttributeId', 'AttributeValue']
        PopulateRequirements.__init__(self, self.requirementsTableName, self.requirementsTableColumns)

        self.loopThroughListOfMajorsAndDoStuff()

    def loopThroughListOfMajorsAndDoStuff(self):
        for major in self.listOfMajors:
            grantForwardItemsDatabaseInfo = GrantForwardItemsGetDatabaseInfo(major, self.tag)
            listOfGrantForwardItemIds = grantForwardItemsDatabaseInfo.getGrantForwardItemIds()
            listOfConcatenatedDescriptionsEligibilities = grantForwardItemsDatabaseInfo.getListStringConcatenatedDescriptionEligibility()
            listOfSourceTexts = grantForwardItemsDatabaseInfo.getSourceTexts()

            for i in range(len(listOfGrantForwardItemIds)):
                grantForwardItemId = listOfGrantForwardItemIds[i]

                descriptionEligibility = listOfConcatenatedDescriptionsEligibilities[i].strip()
                descriptionEligibilitySentences = self.tokenizeIntoSentences(descriptionEligibility)

                sourceText = listOfSourceTexts[i]
                sourceTextSentences = self.tokenizeIntoSentences(sourceText)

                gpa = self.getGPAFromSentences(descriptionEligibilitySentences)
                dueDate = self.getDueDateFromSentences(sourceTextSentences)

                self.doDatabaseInsertsGPAMajor(grantForwardItemId, major, gpa)
                self.insertDueDateIntoGrantForwardItems(grantForwardItemId, dueDate)

    def insertDueDateIntoGrantForwardItems(self, grantForwardItemId, dueDate):
        self.db.insertUpdateOrDelete(
            "update dbo.GrantForwardItems set DueDate='" + dueDate + "' where GrantForwardItemId='" + grantForwardItemId + "'")
