import nltk.data
from Classes.SUDBConnect import SUDBConnect
from Classes.GetFastFindMajorsList import GetFastFindMajorsList
from Classes.PivotLeadsGetDatabaseInfo import PivotLeadsGetDatabaseInfo
from Classes.GPA import GPA


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

            for i in range(len(listOfPivotLeadsIds)):
                pivotLeadId = listOfPivotLeadsIds[i]
                abstractEligibility = listOfConcatenatedAbstractEligibilities[i].strip()
                tokenizedSentences = self.tokenizeAbstractEligibilityIntoSentences(abstractEligibility)

                gpa = []
                dueDate = ''

                for sentence in tokenizedSentences:
                    maybeGPA = GPA(sentence).getGPA()
                    if maybeGPA != '':
                        gpa.append(maybeGPA)

                gpa = ', '.join(gpa)

                print(pivotLeadId, gpa)

    def tokenizeAbstractEligibilityIntoSentences(self, abstractEligibility):
        sentences = self.sentenceTokenizer.tokenize(abstractEligibility)
        return sentences


listOfMajors = ['Accounting']
PopulatePivotLeadRequirements(listOfMajors)
