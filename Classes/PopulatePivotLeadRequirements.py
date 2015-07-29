import nltk.data
from Classes.SUDBConnect import SUDBConnect
from Classes.GetFastFindMajorsList import GetFastFindMajorsList
from Classes.PivotLeadsGetDatabaseInfo import PivotLeadsGetDatabaseInfo
from Classes.GPA import GPA
from Classes.DueDate import DueDate


class PopulatePivotLeadRequirements(object):
    def __init__(self, listOfMajors):
        self.listOfMajors = listOfMajors
        self.db = SUDBConnect()
        self.tag = 'Scholarship'
        self.sentenceTokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

        self.loopThroughListOfMajorsAndDoStuff()

    def loopThroughListOfMajorsAndDoStuff(self):
        for major in self.listOfMajors:
            pivotLeadsDatabaseInfo = PivotLeadsGetDatabaseInfo(major, self.tag)
            listOfPivotLeadsIds = pivotLeadsDatabaseInfo.getPivotLeadId()
            listOfConcatenatedAbstractEligibilities = pivotLeadsDatabaseInfo.getListStringConcatendatedAbstractEligibility()
            listOfSourceTexts = pivotLeadsDatabaseInfo.getSourceText()

            for i in range(len(listOfPivotLeadsIds)):
                pivotLeadId = listOfPivotLeadsIds[i]

                abstractEligibility = listOfConcatenatedAbstractEligibilities[i].strip()
                abstractEligibilitySentences = self.tokenizeAbstractEligibilityIntoSentences(abstractEligibility)

                sourceText = listOfSourceTexts[i]
                sourceTextSentences = self.tokenizeAbstractEligibilityIntoSentences(sourceText)

                gpa = self.getGPAFromAbstractEligibility(abstractEligibilitySentences)
                dueDate = self.getDueDateFromSourceText(sourceTextSentences)

                print(pivotLeadId, gpa, dueDate)

    def getGPAFromAbstractEligibility(self, abstractEligibilitySentences):
        gpa = []
        for sentence in abstractEligibilitySentences:
            maybeGPA = GPA(sentence).getGPA()
            if maybeGPA != '':
                gpa.append(maybeGPA)

        gpa = list(set(gpa))
        gpa = ', '.join(gpa)

        return gpa

    def getDueDateFromSourceText(self, sourceTextSentences):
        dueDates = []

        for sentence in sourceTextSentences:
            maybeDueDate = DueDate(sentence).getDueDate()
            if maybeDueDate != '':
                dueDates.append(maybeDueDate)

        dueDates = list(set(dueDates))
        dueDates = ', '.join(dueDates)

        return dueDates

    def tokenizeAbstractEligibilityIntoSentences(self, abstractEligibility):
        sentences = self.sentenceTokenizer.tokenize(abstractEligibility)
        return sentences


listOfMajors = ['Accounting']
PopulatePivotLeadRequirements(listOfMajors)
