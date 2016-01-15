#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


class CleanText(object):
    @staticmethod
    def removeAllTags(stringToClean):
        return re.sub('<.*?>', ' ', stringToClean, flags=re.DOTALL)

    @staticmethod
    def removenbsp(stringToClean):
        return re.sub('&nbsp;', '', stringToClean)

    @staticmethod
    def convertAmpersand(stringToClean):
        return re.sub('&amp;', '&', stringToClean)

    @staticmethod
    def removeNonBodyElements(stringToClean):
        result = re.sub('<html>.*?<body.*?>', ' ', stringToClean, flags=re.DOTALL)
        result = re.sub('</body>.*?</html>', ' ', result, flags=re.DOTALL)
        return re.sub('</body>', ' ', result)

    @staticmethod
    def removeScriptAndJavascript(stringToClean):
        result = re.sub('<script.*?/script>', ' ', stringToClean, flags=re.DOTALL)
        result = re.sub('javascript.*?/javascript>', ' ', result, flags=re.DOTALL)
        return result

    @staticmethod
    def removeStyle(stringToClean):
        return re.sub('<style.*?</style>', ' ', stringToClean, flags=re.DOTALL)

    @staticmethod
    def removeNoscript(stringToClean):
        return re.sub('<noscript.*?</noscript>', ' ', stringToClean, flags=re.DOTALL)

    @staticmethod
    def replaceSingleQuotesWithTwoSingleQuotes(stringToClean):
        return re.sub("'", "''", stringToClean)

    @staticmethod
    def replaceDoubleQuotesWithTwoSingleQuotes(stringToClean):
        return re.sub('"', "''", stringToClean)

    @staticmethod
    def removeWhiteSpaces(stringToClean):
        result = re.sub(r'\r', '', stringToClean)
        result = re.sub(r'\n\n+', '\n', result)
        result = re.sub(r'\t', '', result)
        result = re.sub(r'\s\s+', ' ', result)
        result = re.sub(r'^\s', '', result)
        result = re.sub(r'\s$', '', result)
        return result

    @staticmethod
    def removeMoreLess(stringToClean):
        result = re.sub('«\sless', '', stringToClean)
        result = re.sub('more\s»', '', result)
        return result

    @staticmethod
    def cleanALLtheText(stringToClean):
        result = CleanText.removeNonBodyElements(stringToClean)
        result = CleanText.removeStyle(result)
        result = CleanText.removeScriptAndJavascript(result)
        result = CleanText.removeNoscript(result)
        result = CleanText.removeAllTags(result)
        result = CleanText.removenbsp(result)
        result = CleanText.convertAmpersand(result)
        result = CleanText.replaceSingleQuotesWithTwoSingleQuotes(result)
        result = CleanText.removeMoreLess(result)
        result = CleanText.removeWhiteSpaces(result)

        return result