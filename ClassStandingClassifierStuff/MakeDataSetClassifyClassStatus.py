from Classes.TokenizeOnWhitespacePunctuation import TokenizeOnWhitespacePunctuation
from ClassStandingClassifierStuff.GetDatabaseInfoScholarshipsWithClassStatuses import \
    GetDatabaseInfoScholarshipsWithClassStatuses
import math


class MakeDataSetClassifyClassStatus():
    def __init__(self, classStatusToUse):
        self.classStatusToUse = classStatusToUse
        self.labelGood = classStatusToUse
        self.labelBad = 'Other'
        self.goodClassStatusDB = GetDatabaseInfoScholarshipsWithClassStatuses(requirementNeeded=self.classStatusToUse)
        self.badClassStatusDB = GetDatabaseInfoScholarshipsWithClassStatuses(requirementNeeded=self.classStatusToUse,
                                                                             useNot=True)
        self.fullDataSet = []
        self.makeDataLinesGoodLabel()
        self.makeDataLinesBadLabel()

    def makeTrainingAndTestingSets(self, trainingPercentage):
        numTotalEntries = len(self.fullDataSet)
        numTrainingEntries = math.ceil(numTotalEntries * trainingPercentage)
        numTestingEntries = numTotalEntries - numTrainingEntries

        trainingSet = self.fullDataSet[:numTrainingEntries]
        testingSet = self.fullDataSet[-numTestingEntries:]

        return [trainingSet, testingSet]

    def makeDataLinesGoodLabel(self):
        scholarshipDescriptions = self.goodClassStatusDB.getScholarshipDescriptionsList()
        eligibilities = self.goodClassStatusDB.getEligibilitiesList()

        for i in range(len(scholarshipDescriptions)):
            description = scholarshipDescriptions[i]
            eligibility = eligibilities[i]
            features = []

            concatenatedText = '%s %s' % (description, eligibility)
            unigrams = TokenizeOnWhitespacePunctuation(concatenatedText, keepCaps=False).getUnigrams()
            bigrams = ['%s %s' % (unigrams[i], unigrams[i + 1]) for i in range(len(unigrams) - 1)]

            for unigram in unigrams:
                features.append(unigram)
            for bigram in bigrams:
                features.append(bigram)

            dataLine = {'label': self.labelGood, 'features': features}
            self.fullDataSet.append(dataLine)

    def makeDataLinesBadLabel(self):
        scholarshipDescriptions = self.badClassStatusDB.getScholarshipDescriptionsList()
        eligibilities = self.badClassStatusDB.getEligibilitiesList()

        for i in range(len(scholarshipDescriptions)):
            description = scholarshipDescriptions[i]
            eligibility = eligibilities[i]
            features = []

            concatenatedText = '%s %s' % (description, eligibility)
            unigrams = TokenizeOnWhitespacePunctuation(concatenatedText, keepCaps=False).getUnigrams()
            bigrams = ['%s %s' % (unigrams[i], unigrams[i + 1]) for i in range(len(unigrams) - 1)]

            for unigram in unigrams:
                features.append(unigram)
            for bigram in bigrams:
                features.append(bigram)

            dataLine = {'label': self.labelBad, 'features': features}
            self.fullDataSet.append(dataLine)


testClass = MakeDataSetClassifyClassStatus('Junior')
print(len(testClass.fullDataSet))
trainingSetAndTestingSet = testClass.makeTrainingAndTestingSets()
'''
training = trainingSetAndTestingSet[0]
testing = trainingSetAndTestingSet[1]
print(len(training))
print(len(testing))
'''
