import nltk.data


class TokenizeIntoSentences(object):
    @staticmethod
    def doTokenize(stringToTokenize):
        sentenceTokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        return sentenceTokenizer.tokenize(stringToTokenize)
