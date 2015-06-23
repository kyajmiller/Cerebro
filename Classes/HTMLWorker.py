import re


class HTMLWorker(object):
    @staticmethod
    def removeHtmlTags(stringToParse):
        return re.sub('''<\/?\w+((\s+\w+(\s*=\s*(?:".*?"|'.*?'|[^\'">\s]+))?)+\s*|\s*)/?>''', ' ', stringToParse)

    @staticmethod
    def removeAllJavascript(stringToParse):
        return re.sub('''<\/?\w+((\s+\w+(\s*=\s*(?:".*?"|'.*?'|[^\'">\s]+))?)+\s*|\s*)/?>''', '', stringToParse)

    @staticmethod
    def removeNonBodyElements(stringToParse):
        result = re.sub('''<html>[\s\S]*<body>''', '', stringToParse)
        result = re.sub('''</body>[\s\S]*</html>''', '', result)
        return re.sub('''</body>''', '', result)

    @staticmethod
    def cleanWebPageBeforeProcessing(stringToParse):
        result = HTMLWorker.removeNonBodyElements(stringToParse)
        result = HTMLWorker.removeAllJavascript(result)
        result = HTMLWorker.removeHtmlTags(result)
        return result
