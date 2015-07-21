import re


class TokenizeOnWhitespacePunctuation(object):
    def __init__(self, stringToTokenize):
        self.stringToTokenize = stringToTokenize

        self.unigrams = []
        self.bigrams = []
        self.bothUnigramsBigrams = []

    def getUnigrams(self):
        self.unigrams = re.findall(r"[\w']+", self.stringToTokenize)
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
