from Classes.TokenizeIntoSentences import TokenizeIntoSentences
from Classes.TokenizeOnWhitespacePunctuation import TokenizeOnWhitespacePunctuation
from random import shuffle
import math


class MakeDataSetClassifyClassStatus(object):
    @staticmethod
    def makeMultilabelTrainingAndTestingSet(dataTextList, labelsList, idsList, trainingPercentage=0.8):
        if trainingPercentage > 0 and trainingPercentage < 1:
            dataSet = MakeDataSetClassifyClassStatus.makeDataSet(labelsList, dataTextList, idsList)
            shuffle(dataSet)

            numTotalEntries = len(dataSet)
            numTrainingEntries = math.ceil(numTotalEntries * trainingPercentage)
            numTestingEntries = numTotalEntries - numTrainingEntries

            trainingSet = dataSet[:numTrainingEntries]
            testingSet = dataSet[-numTestingEntries:]

            return trainingSet, testingSet
        else:
            print('Not a real percentage, please enter a float between 0 and 1.')
            return None

    @staticmethod
    def makeBinaryLabelTrainingAndTestingSet(firstLabel, secondLabel, firstLabelTextList, secondLabelTextList,
                                             firstLabelIdsList, secondLabelIdsList, trainingPercentage=0.8):
        if trainingPercentage > 0 and trainingPercentage < 1:
            fullDataSet = []
            firstLabelDataset = MakeDataSetClassifyClassStatus.makeDataSet(firstLabel, firstLabelTextList,
                                                                                    firstLabelIdsList)
            secondLabelDataset = MakeDataSetClassifyClassStatus.makeDataSet(secondLabel, secondLabelTextList,
                                                                                     secondLabelIdsList)

            for dataLine in firstLabelDataset:
                fullDataSet.append(dataLine)
            for dataLine in secondLabelDataset:
                fullDataSet.append(dataLine)

            shuffle(fullDataSet)

            numTotalEntries = len(fullDataSet)
            numTrainingEntries = math.ceil(numTotalEntries * trainingPercentage)
            numTestingEntries = numTotalEntries - numTrainingEntries

            trainingSet = fullDataSet[:numTrainingEntries]
            testingSet = fullDataSet[-numTestingEntries:]

            return trainingSet, testingSet
        else:
            print('Not a real percentage, please enter a float between 0 and 1.')
            return None

    @staticmethod
    def makeDataSet(labels, dataTextList, idsList):
        dataSet = []

        for i in range(len(dataTextList)):
            dataText = dataTextList[i]
            scholarshipId = idsList[i]
            label = ''
            if type(labels) == list:
                label = labels[i]
            elif type(labels) == str:
                label = labels

            features = []

            ngramsList = MakeDataSetClassifyClassStatus.getNgrams(dataText, getUnigrams=True, getBigrams=True,
                                                                           getTrigrams=False)
            unigrams = ngramsList[0]
            bigrams = ngramsList[1]

            for unigram in unigrams:
                features.append(unigram)
            for bigram in bigrams:
                features.append(bigram)

            dataLine = {'label': label, 'id': scholarshipId, 'features': features}
            dataSet.append(dataLine)

        return dataSet

    @staticmethod
    def getNgrams(text, getUnigrams=True, getBigrams=True, getTrigrams=False):
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
