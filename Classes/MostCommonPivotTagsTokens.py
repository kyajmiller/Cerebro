from nltk import FreqDist
from Classes.GetPivotTagsTitleAbstractEligibility import GetPivotTagsTitleAbstractEligibility
from Classes.TokenizeOnWhitespacePunctuation import TokenizeOnWhitespacePunctuation


class MostCommonPivotTagsTokens(object):
    def __init__(self, topNumber):
        self.topNumber = topNumber
        self.pivotTagsData = GetPivotTagsTitleAbstractEligibility.getListConcatenatedItems()
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
