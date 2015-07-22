import re
from Classes.StopwordsList import StopwordsList


class TokenizeOnWhitespacePunctuation(object):
    def __init__(self, stringToTokenize):
        self.stringToTokenize = stringToTokenize.lower()

        self.listOfStopwords = StopwordsList.stopwords()

        self.unigrams = []
        self.bigrams = []
        self.bothUnigramsBigrams = []

    def getUnigrams(self):
        self.unigrams = re.findall(r"[\w']+", self.stringToTokenize)
        for word in self.unigrams:
            if word in self.listOfStopwords:
                self.unigrams.remove(word)
        return self.unigrams

    def getBigrams(self):
        self.getUnigrams()
        for i in range(len(self.unigrams) - 1):
            currentToken = self.unigrams[i]
            nextToken = self.unigrams[i + 1]
            bigram = '%s %s' % (currentToken, nextToken)
            self.bigrams.append(bigram)
        return self.bigrams

    def getBothUnigramsBigrams(self):
        self.getUnigrams()
        self.getBigrams()
        self.bothUnigramsBigrams = self.unigrams[:]
        for i in self.bigrams:
            self.bothUnigramsBigrams.append(i)
        return self.bothUnigramsBigrams
