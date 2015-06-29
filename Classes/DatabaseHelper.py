import pyodbc
from Classes.SUDBConnect import SUDBConnect
from Classes.Parser import Parser


class DatabaseHelper(SUDBConnect):
    @staticmethod
    def UseOnlyFirstRegex(attributeId, stringToScan):
        DB = SUDBConnect()
        rows = DB.getRows(' Select ' + str(attributeId) + ' , RegEx from RegExHelpers')
        searchCriteria = ''
        if len(rows) >= 1:
            searchCriteria = rows[0].RegEx

        return Parser(stringToScan, searchCriteria).doesMatchExist()

    @staticmethod
    def useOnlyOneRegexHelper(attributeId, stringToScan):
        DB = SUDBConnect()
        rows = DB.getRows(' Select ' + str(attributeId) + ' , RegExHelper from RegExHelpers')
        searchCriteria = ''
        if len(rows) >= 1:
            searchCriteria = rows[0].RegExHelper

        return Parser(stringToScan, searchCriteria).doesMatchExist()

    @staticmethod
    def useOnlyFirstRegexAndRegexHelper(attributeId, stringToScan):
        DB = SUDBConnect()
        rows = DB.getRows(' Select ' + str(attributeId) + ' , RegEx, RegExHelper from RegExHelpers')
        searchCriteriaRegex = ''
        searchCriteriaRegexHelper = ''
        doBothMatch = False
        if len(rows) >= 1:
            searchCriteriaRegex = rows[0].RegEx
            searchCriteriaRegexHelper = rows[0].RegExHelper
        if Parser(stringToScan, searchCriteriaRegex).doesMatchExist() and Parser(stringToScan,
                                                                                 searchCriteriaRegexHelper).doesMatchExist():
            doBothMatch = True

        return doBothMatch

    @staticmethod
    def useAllRegex(attributeId, stringToScan):
        DB = SUDBConnect()
        rows = DB.getRows(' Select ' + str(attributeId) + ' , RegEx from RegExHelpers')
        regExArray = []
        if len(rows) >= 1:
            for row in rows:
                regExArray.append(row.RegEx)
        searchCriteria = '|'.join(list(set(regExArray)))

        return Parser(stringToScan, searchCriteria).doesMatchExist()

    @staticmethod
    def useAllRegexHelper(attributeId, stringToScan):
        DB = SUDBConnect()
        rows = DB.getRows(' Select ' + str(attributeId) + ' , RegExHelper from RegExHelpers')
        regExHelperArray = []
        if len(rows) >= 1:
            for row in rows:
                regExHelperArray.append(row.RegExHelper)
        searchCriteria = '|'.join(list(set(regExHelperArray)))

        return Parser(stringToScan, searchCriteria).doesMatchExist()

    @staticmethod
    def useAllRegexAndRegexHelper(attributeId, stringToScan):
        DB = SUDBConnect()
        rows = DB.getRows(' Select ' + str(attributeId) + ' , RegEx, RegExHelper from RegExHelpers')
        regExArray = []
        regExHelperArray = []
        if len(rows) >= 1:
            for row in rows:
                regExArray.append(row.RegEx)
                regExHelperArray.append(row.RegExHelper)
        searchCriteriaRegex = '|'.join(regExArray)
        searchCriteriaRegexHelper = '|'.join(regExHelperArray)
        doBothMatch = False

        if Parser(stringToScan, searchCriteriaRegex).doesMatchExist() and Parser(stringToScan,
                                                                                 searchCriteriaRegexHelper):
            doBothMatch = True

        return doBothMatch


'''
    @staticmethod
    def UseOnlyFirstRegexTrueFalse(attributeId, stringToScan, regexMatch):
        DB = SUDBConnect()
        rows = DB.getRows(' Select ' + str(attributeId) + ' , RegEx from RegExHelpers')
        searchCriteria = ''
        if len(rows) >= 1:
            searchCriteria = rows[0].RegEx
        if regexMatch == Parser(stringToScan, searchCriteria).doesMatchExist():
            return True
        else:
            return False

    @staticmethod
    def useOnlyOneRegexHelperTrueFalse(attributeId, stringToScan, regexHelperMatch):
        DB = SUDBConnect()
        rows = DB.getRows(' Select ' + str(attributeId) + ' , RegExHelper from RegExHelpers')
        searchCriteria = ''
        if len(rows) >= 1:
            searchCriteria = rows[0].RegExHelper
        if regexHelperMatch == Parser(stringToScan, searchCriteria).doesMatchExist():
            return True
        else:
            return False
'''
