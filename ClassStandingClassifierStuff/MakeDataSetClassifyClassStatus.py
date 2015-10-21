from Classes.TokenizeOnWhitespacePunctuation import TokenizeOnWhitespacePunctuation
from Classes.TokenizeIntoSentences import TokenizeIntoSentences
from ClassStandingClassifierStuff.GetDatabaseInfoScholarshipsWithClassStatuses import \
    GetDatabaseInfoScholarshipsWithClassStatuses
from random import shuffle
import math


class MakeDataSetClassifyClassStatus():
    def __init__(self, classStatus='', badLabel='Other', testingDataTextList=None, testingDataIds=None):
        self.testingDataIds = testingDataIds
        self.testingDataTextList = testingDataTextList
        self.classStatusToUse = classStatus
        self.labelGood = classStatus
        self.labelBad = badLabel

        if classStatus != '':
            self.goodClassStatusDB = GetDatabaseInfoScholarshipsWithClassStatuses(
                requirementNeeded=self.classStatusToUse)
            self.badClassStatusDB = GetDatabaseInfoScholarshipsWithClassStatuses(
                requirementNeeded=self.classStatusToUse, useNot=True)
        self.fullDataSet = []

    def makeOnlyTrainingSet(self):
        testingDataSet = []

        if self.testingDataTextList and self.testingDataIds:
            for i in range(len(self.testingDataTextList)):
                dataText = self.testingDataTextList[i]
                scholarshipId = self.testingDataIds[i]
                features = []

                ngramsList = self.getNgrams(dataText, getUnigrams=True, getBigrams=True, getTrigrams=False)
                unigrams = ngramsList[0]
                bigrams = ngramsList[1]

                for unigram in unigrams:
                    features.append(unigram)
                for bigram in bigrams:
                    features.append(bigram)

                dataLine = {'label': self.classStatusToUse, 'scholarshipId': scholarshipId, 'features': features}
                testingDataSet.append(dataLine)

        return testingDataSet

    def makeTrainingAndTestingSets(self, trainingPercentage=0.8):
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
        idsList = self.goodClassStatusDB.getScholarshipsWithClassStatusIdsList()

        for i in range(len(scholarshipDescriptions)):
            description = scholarshipDescriptions[i]
            eligibility = eligibilities[i]
            scholarshipClassStatusId = idsList[i]
            features = []

            concatenatedText = '%s %s' % (description, eligibility)

            ngramsList = self.getNgrams(concatenatedText, getUnigrams=True, getBigrams=True, getTrigrams=False)
            unigrams = ngramsList[0]
            bigrams = ngramsList[1]

            for unigram in unigrams:
                features.append(unigram)
            for bigram in bigrams:
                features.append(bigram)

            dataLine = {'label': self.labelGood, 'scholarshipId': scholarshipClassStatusId, 'features': features}
            self.fullDataSet.append(dataLine)

    def makeDataLinesBadLabel(self):
        scholarshipDescriptions = self.badClassStatusDB.getScholarshipDescriptionsList()
        eligibilities = self.badClassStatusDB.getEligibilitiesList()
        idsList = self.badClassStatusDB.getScholarshipsWithClassStatusIdsList()

        for i in range(len(scholarshipDescriptions)):
            description = scholarshipDescriptions[i]
            eligibility = eligibilities[i]
            scholarshipClassStatusId = idsList[i]
            features = []

            concatenatedText = '%s %s' % (description, eligibility)
            ngramsList = self.getNgrams(concatenatedText, getUnigrams=True, getBigrams=True, getTrigrams=False)
            unigrams = ngramsList[0]
            bigrams = ngramsList[1]

            for unigram in unigrams:
                features.append(unigram)
            for bigram in bigrams:
                features.append(bigram)

            dataLine = {'label': self.labelBad, 'scholarshipId': scholarshipClassStatusId, 'features': features}
            self.fullDataSet.append(dataLine)

    def getNgrams(self, text, getUnigrams=True, getBigrams=True, getTrigrams=False):
        unigrams = []
        bigrams = []
        trigrams = []

        sentences = TokenizeIntoSentences().doTokenize(text)
        for sentence in sentences:
            sentenceUnigrams = TokenizeOnWhitespacePunctuation(sentence, keepCaps=False,
                                                               applyStopwords=True).getUnigrams()
            if getUnigrams:
                for sentenceUnigram in sentenceUnigrams:
                    unigrams.append(sentenceUnigram)

            if getBigrams:
                sentenceBigrams = ['%s %s' % (sentenceUnigrams[i], sentenceUnigrams[i + 1]) for i in
                                   range(len(sentenceUnigrams) - 1)]
                for sentenceBigram in sentenceBigrams:
                    bigrams.append(sentenceBigram)

            if getTrigrams:
                sentenceTrigrams = ['%s %s %s' % (sentenceUnigrams[i], sentenceUnigrams[i + 1], sentenceUnigrams[i + 2])
                                    for i in range(len(sentenceUnigrams) - 2)]
                for sentenceTrigram in sentenceTrigrams:
                    trigrams.append(sentenceTrigram)

        ngramsList = [unigrams, bigrams, trigrams]

        return ngramsList
