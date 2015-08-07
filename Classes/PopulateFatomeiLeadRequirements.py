import nltk.data
import re
from Classes.SUDBConnect import SUDBConnect
from Classes.FatomeiLeadsGetDatabaseInfo import FatomeiLeadsGetDatabaseInfo
from Classes.GPA import GPA
from Classes.Majors import Majors
from Classes.GetFastFindMajorsList import GetFastFindMajorsList


class PopulateFatomeiLeadRequirements(object):
    def __init__(self):
        self.db = SUDBConnect()
        self.tag = 'Scholarship'
        self.sentenceTokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    def loopThroughLeadsAndDoStuff(self):
        fatomeiLeadsDatabaseInfo = FatomeiLeadsGetDatabaseInfo(self.tag)
        listOfFatomeiLeadsIds = fatomeiLeadsDatabaseInfo.getFatomeiLeadIds()
        listConcatenatedDescriptionsSourceText = fatomeiLeadsDatabaseInfo.getConcatenatedDescriptionsSourceText()

        for i in range(len(listOfFatomeiLeadsIds)):
            fatomeiLeadId = listOfFatomeiLeadsIds[i]

            descriptionSourceText = listConcatenatedDescriptionsSourceText[i]
            descriptionSourceTextSentences = self.tokenizeIntoSentences(descriptionSourceText)

            gpa = self.getGPAFromDescriptionSourceText(descriptionSourceTextSentences)
            majors = self.getMajorsFromDescriptionSourceText(descriptionSourceTextSentences)

            self.doDatabaseInserts(fatomeiLeadId, gpa, majors)

    def tokenizeIntoSentences(self, stringToTokenize):
        sentences = self.sentenceTokenizer.tokenize(stringToTokenize)
        return sentences

    def getGPAFromDescriptionSourceText(self, descriptionSourceTextSentences):
        gpa = []

        for sentence in descriptionSourceTextSentences:
            if len(sentence) <= 1000:
                maybeGPA = GPA(sentence).getGPA()
                if maybeGPA != '':
                    gpa.append(maybeGPA)

        gpa = list(set(gpa))
        gpa = ', '.join(gpa)

        return gpa

    def getMajorsFromDescriptionSourceText(self, descriptionSourceTextSentences):
        majors = []

        majorsList = GetFastFindMajorsList.getDefaultList()
        majorsList = [major.lower() for major in majorsList]
        majorsList = list(set(majorsList))

        majorsListRegex = '|'.join(majorsList)

        for sentence in descriptionSourceTextSentences:
            if len(sentence) <= 1000:
                maybeMajor = Majors(sentence, majorsListRegex).getMajors()
                if maybeMajor != '':
                    majors.append(maybeMajor)

        majors = list(set(majors))
        majors = ', '.join(majors)

        return majors

    def doDatabaseInserts(self, fatomeiLeadId, gpa, major):
        if major != '':
            self.insertMajorIntoFatomeiLeadRequirements(fatomeiLeadId, major)

        if gpa != '':
            self.insertGPAIntoFatomeiLeadRequirements(fatomeiLeadId, gpa)

    def insertMajorIntoFatomeiLeadRequirements(self, fatomeiLeadId, major):
        attributeId = '417'
        attributeValue = major

        self.db.insertUpdateOrDelete(
            "insert into dbo.FatomeiLeadRequirements (FatomeiLeadId, AttributeId, AttributeValue) values ('" + fatomeiLeadId + "', '" + attributeId + "', '" + attributeValue + "')")

    def insertGPAIntoFatomeiLeadRequirements(self, fatomeiLeadId, gpa):
        attributeId = '1'
        attributeValue = gpa

        self.db.insertUpdateOrDelete(
            "insert into dbo.FatomeiLeadRequirements (FatomeiLeadId, AttributeId, AttributeValue) values ('" + fatomeiLeadId + "', '" + attributeId + "', '" + attributeValue + "')")


PopulateFatomeiLeadRequirements().loopThroughLeadsAndDoStuff()
