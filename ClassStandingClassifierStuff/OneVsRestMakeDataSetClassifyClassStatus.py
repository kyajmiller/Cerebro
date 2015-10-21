from Classes.TokenizeIntoSentences import TokenizeIntoSentences
from Classes.TokenizeOnWhitespacePunctuation import TokenizeOnWhitespacePunctuation
from random import shuffle
import math


class OneVsRestMakeDataSetClassifyClassStatus(object):
    def __init__(self, dataTextList, labelsList, idsList):
        self.dataTextList = dataTextList
        self.labelsList = labelsList
        self.idsList = idsList

    def makeTrainingAndTestingSet(self, trainingPercentage=0.8):
        if trainingPercentage > 0 and trainingPercentage < 1:
            dataSet = self.makeFullDataSet()
            shuffle(dataSet)

            numTotalEntries = len(dataSet)
            numTrainingEntries = math.ceil(numTotalEntries * trainingPercentage)
            numTestingEntries = numTotalEntries - numTrainingEntries

            trainingSet = dataSet[dataSet:numTrainingEntries]
            testingSet = dataSet[-numTestingEntries:]

            return [trainingSet, testingSet]
        else:
            print('Not a real percentage, please enter a float between 0 and 1.')
            return None

    def makeFullDataSet(self):
        fullDataSet = []
        for i in range(len(self.dataTextList)):
            dataText = self.dataTextList[i]
            scholarshipId = self.idsList[i]
            labels = self.labelsList[i]

            features = []

            ngramsList = self.getNgrams(dataText, getUnigrams=True, getBigrams=True, getTrigrams=False)
            unigrams = ngramsList[0]
            bigrams = ngramsList[1]

            for unigram in unigrams:
                features.append(unigram)
            for bigram in bigrams:
                features.append(bigram)

            dataLine = {'label': labels, 'id': scholarshipId, 'features': features}
            fullDataSet.append(dataLine)

        return fullDataSet

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
