from nltk import FreqDist
from Classes.GetPivotTagsConcatenateTitleAbstractEligibility import GetPivotTagsConcatenateTitleAbstractEligibility
from Classes.TokenizeOnWhitespacePunctuation import TokenizeOnWhitespacePunctuation


class MostCommonPivotTagsTokens(object):
    def __init__(self, topNumber):
        self.topNumber = topNumber
        self.pivotTagsData = GetPivotTagsConcatenateTitleAbstractEligibility.getList()
        self.tokens = []

    def tokenizeData(self):
        for data in self.pivotTagsData:
            unigramsBigrams = TokenizeOnWhitespacePunctuation(data).getBothUnigramsBigrams()
            for token in unigramsBigrams:
                self.tokens.append(token)

    def getMostCommon(self):
        self.tokenizeData()
        freqDist = FreqDist(self.tokens)
        mostCommon = freqDist.most_common(self.topNumber)
        return mostCommon
