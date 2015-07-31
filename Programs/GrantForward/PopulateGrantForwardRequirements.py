import nltk.data
from Classes.SUDBConnect import SUDBConnect
from Classes.GrantForwardItemsGetDatabaseInfo import GrantForwardItemsGetDatabaseInfo
from Classes.GPA import GPA
from Classes.DueDate import DueDate


class PopulateGrantForwardRequirements(object):
    def __init__(self, listOfMajors):
        self.listOfMajors = listOfMajors
        self.db = SUDBConnect()
        self.tag = 'Scholarship'
        self.sentenceTokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

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

                gpa = self.getGPAFromDescriptionEligibility(descriptionEligibilitySentences)
                dueDate = self.getDueDateFromSourceText(sourceTextSentences)

                self.doDatabaseInserts(grantForwardItemId, major, gpa, dueDate)

    def tokenizeIntoSentences(self, stringToTokenize):
        sentences = self.sentenceTokenizer.tokenize(stringToTokenize)
        return sentences

    def getGPAFromDescriptionEligibility(self, descriptionEligibilitySentences):
        gpa = []

        for sentence in descriptionEligibilitySentences:
            maybeGPA = GPA(sentence).getGPA()
            if maybeGPA != '':
                gpa.append(maybeGPA)

        gpa = list(set(gpa))
        gpa = ', '.join(gpa)

        return gpa

    def getDueDateFromSourceText(self, sourceTextSentences):
        dueDate = ''

        for sentence in sourceTextSentences:
            if len(sentence) <= 1000:
                maybeDueDate = DueDate(sentence).getDueDate()
                if maybeDueDate != '':
                    dueDate = maybeDueDate

        return dueDate

    def doDatabaseInserts(self, grantForwardItemId, major, gpa, dueDate):
        self.insertMajorIntoGrantForwardRequirements(grantForwardItemId, major)

        if gpa != '':
            self.insertGPAIntoGrantForwardRequirements(grantForwardItemId, gpa)

        if dueDate != '':
            self.insertDueDateIntoGrantForwardItems(grantForwardItemId, dueDate)

    def insertMajorIntoGrantForwardRequirements(self, grantForwardItemId, major):
        attributeId = '417'
        attributeValue = major

        self.db.insertUpdateOrDelete(
            "insert into dbo.GrantForwardRequirements (GrantForwardId, AttributeId, AttributeValue) values ('" + grantForwardItemId + "', '" + attributeId + "', '" + attributeValue + "')")

    def insertGPAIntoGrantForwardRequirements(self, grantForwardItemId, gpa):
        attributeId = '1'
        attributeValue = gpa

        self.db.insertUpdateOrDelete(
            "insert into dbo.GrantForwardRequirements (GrantForwardId, AttributeId, AttributeValue) values ('" + grantForwardItemId + "', '" + attributeId + "', '" + attributeValue + "')")

    def insertDueDateIntoGrantForwardItems(self, grantForwardItemId, dueDate):
        self.db.insertUpdateOrDelete(
            "update dbo.GrantForwardItems set DueDate='" + dueDate + "' where GrantForwardItemId='" + grantForwardItemId + "'")
