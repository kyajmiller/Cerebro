import nltk.data
from Classes.SUDBConnect import SUDBConnect
from Classes.CollegeGreenLightLeadsGetDatabaseInfo import CollegeGreenLightLeadsGetDatabaseInfo
from Classes.GPA import GPA
from Classes.Majors import Majors
from Classes.GetFastFindMajorsList import GetFastFindMajorsList


class PopulateCollegeGreenLightRequirements(object):
    def __init__(self):
        self.db = SUDBConnect()
        self.sentenceTokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    def loopThroughLeadsAndDoStuff(self):
        collegeGreenLightDataInfo = CollegeGreenLightLeadsGetDatabaseInfo()
        listOfCollegeGreenLightLeadsIds = collegeGreenLightDataInfo.getCollegeGreenLightLeadsIds()
        listOfConcatenatedDescriptionSourceText = collegeGreenLightDataInfo.getConcatenatedDescriptionSourceText()

        for i in range(len(listOfCollegeGreenLightLeadsIds)):
            collegeGreenLightLeadId = listOfCollegeGreenLightLeadsIds[i]

            descriptionSourceText = listOfConcatenatedDescriptionSourceText[i]
            descriptionSourceTextSentences = self.tokenizeIntoSentences(descriptionSourceText)

            gpa = self.getGPAFromDescriptionSourceText(descriptionSourceTextSentences)
            majors = self.getMajorFromDescriptionSourceText(descriptionSourceTextSentences)

            self.doDatabaseInserts(collegeGreenLightLeadId, gpa, majors)

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

    def getMajorFromDescriptionSourceText(self, descriptionSourceTextSentences):
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

    def doDatabaseInserts(self, collegeGreenLightLeadId, gpa, majors):
        if gpa != '':
            self.insertGPAIntoCollegeGreenLightRequirements(collegeGreenLightLeadId, gpa)

        if majors != '':
            self.insertMajorsIntoCollegeGreenLightLeadRequirements(collegeGreenLightLeadId, majors)

    def insertGPAIntoCollegeGreenLightRequirements(self, collegeGreenLightLeadId, gpa):
        attributeId = '1'
        attributeValue = gpa

        self.db.insertUpdateOrDelete(
            "insert into dbo.CollegeGreenLightRequirements (CollegeGreenLightLeadId, AttributeId, AttributeValue) values ('" + collegeGreenLightLeadId + "', '" + attributeId + "', '" + attributeValue + "')")

    def insertMajorsIntoCollegeGreenLightLeadRequirements(self, collegeGreenLightLeadId, majors):
        attributeId = '417'
        attributeValue = majors

        self.db.insertUpdateOrDelete(
            "insert into dbo.CollegeGreenLightRequirements (CollegeGreenLightLeadId, AttributeId, AttributeValue) values ('" + collegeGreenLightLeadId + "', '" + attributeId + "', '" + attributeValue + "')")


PopulateCollegeGreenLightRequirements().loopThroughLeadsAndDoStuff()
