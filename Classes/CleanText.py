import re


class CleanText(object):
    @staticmethod
    def removeAllTags(stringToClean):
        return re.sub('<.*?>', '', stringToClean, flags=re.DOTALL)

    @staticmethod
    def removenbsp(stringToClean):
        return re.sub('&nbsp;', '', stringToClean)

    @staticmethod
    def convertAmpersand(stringToClean):
        return re.sub('&amp;', '&', stringToClean)

    @staticmethod
    def removeNonBodyElements(stringToClean):
        result = re.sub('<html>.*?<body>', '', stringToClean, flags=re.DOTALL)
        result = re.sub('</body>.*?</html>', '', result, flags=re.DOTALL)
        return re.sub('</body>', '', result)

    @staticmethod
    def removeScriptAndJavascript(stringToClean):
        return re.sub('<script.*?/script>', '', flags=re.DOTALL)

    @staticmethod
    def cleanALLtheText(stringToClean):
        result = CleanText.removeNonBodyElements(stringToClean)
        result = CleanText.removeAllTags(result)
        result = CleanText.removenbsp(result)
        result = CleanText.convertAmpersand(result)

        return result
