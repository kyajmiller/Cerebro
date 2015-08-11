import nltk.data
from Classes.SUDBConnect import SUDBConnect
from Classes.GetFastFindMajorsList import GetFastFindMajorsList
from Classes.GPA import GPA
from Classes.Majors import Majors
from Classes.PutThingsInTables import PutThingsInTables


class PopulateRequirements(object):
    def __init__(self, requirementsTableName, requirementsTableColumns):
        self.requirementsTableColumns = requirementsTableColumns
        self.requirementsTableName = requirementsTableName
        self.db = SUDBConnect()
        self.sentenceTokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    def tokenizeIntoSentences(self, stringToTokenize):
        sentences = self.sentenceTokenizer.tokenize(stringToTokenize)
        return sentences

    def getGPAFromSentences(self, sentences):
        gpa = []

        for sentence in sentences:
            if len(sentence) <= 1000:
                maybeGPA = GPA(sentence).getGPA()
                if maybeGPA != '':
                    gpa.append(maybeGPA)

        gpa = list(set(gpa))
        gpa = ', '.join(gpa)

        return gpa

    def getMajorFromSentences(self, sentences):
        majors = []

        majorsList = GetFastFindMajorsList.getDefaultList()
        majorsList = [major.lower() for major in majorsList]
        majorsList = list(set(majorsList))

        majorsListRegex = '|'.join(majorsList)

        for sentence in sentences:
            if len(sentence) <= 1000:
                maybeMajor = Majors(sentence, majorsListRegex).getMajors()
                if maybeMajor != '':
                    majors.append(maybeMajor)

        majors = list(set(majors))
        majors = ', '.join(majors)

        return majors

    def doDatabaseInserts(self, leadId, gpa, majors):
        if gpa != '':
            self.insertGPAIntoRequirements(leadId, gpa)

        if majors != '':
            self.insertMajorsIntoRequirements(leadId, majors)

    def insertGPAIntoRequirements(self, leadId, gpa):
        attributeId = '1'
        insertValues = [leadId, attributeId, gpa]
        sqlQuery = PutThingsInTables(self.requirementsTableName, self.requirementsTableColumns,
                                     insertValues).createSQLQuery()
        self.db.insertUpdateOrDelete(sqlQuery)

    def insertMajorsIntoRequirements(self, leadId, majors):
        attributeId = '417'
        insertValues = [leadId, attributeId, majors]
        sqlQuery = PutThingsInTables(self.requirementsTableName, self.requirementsTableColumns,
                                     insertValues).createSQLQuery()
        self.db.insertUpdateOrDelete(sqlQuery)
