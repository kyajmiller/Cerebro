from Classes.TokenizeOnWhitespacePunctuation import TokenizeOnWhitespacePunctuation
from ClassStandingClassifierStuff.GetDatabaseInfoScholarshipsWithClassStatuses import \
    GetDatabaseInfoScholarshipsWithClassStatuses
from random import shuffle
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

    def makeTrainingAndTestingSets(self, trainingPercentage):
        if trainingPercentage >= 0 and trainingPercentage <= 1:
            self.makeDataLinesGoodLabel()
            self.makeDataLinesBadLabel()
            shuffle(self.fullDataSet)

            numTotalEntries = len(self.fullDataSet)
            numTrainingEntries = math.ceil(numTotalEntries * trainingPercentage)
            numTestingEntries = numTotalEntries - numTrainingEntries

            trainingSet = self.fullDataSet[:numTrainingEntries]
            testingSet = self.fullDataSet[-numTestingEntries:]

            return [trainingSet, testingSet]

        else:
            print('Not a real percentage, please enter a float between 0 and 1.')
            return None

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
