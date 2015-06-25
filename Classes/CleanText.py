import re


class CleanText(object):
    @staticmethod
    def removeAllTags(stringToClean):
        return re.sub('<.*?>', '', stringToClean)

    @staticmethod
    def removenbsp(stringToClean):
        return re.sub('&nbsp;', '', stringToClean)

    @staticmethod
    def convertAmp(stringToClean):
        return re.sub('&amp;', '&', stringToClean)

    @staticmethod
    def removeNonBodyElements(stringToClean):
        result = re.sub('<html>.*?<body>', '', stringToClean)
        result = re.sub('</body>.*?</html>', '', result)
        return re.sub('</body>', '', result)

    @staticmethod
    def cleanALLtheText(stringToClean):
        result = CleanText.removeNonBodyElements(stringToClean)
        result = CleanText.removeAllTags(result)
        result = CleanText.removenbsp(result)
        result = CleanText.convertAmp(result)

        return result
