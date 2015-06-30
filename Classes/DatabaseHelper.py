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
                                                                                 searchCriteriaRegexHelper).doesMatchExist():
            doBothMatch = True

        return doBothMatch


'''
    @staticmethod
    def useOnlyFirstRegexOrRegexHelperTrueFalse(attributeId, stringToScan, matchRegEx=True, matchRegExHelper=None):
        DB = SUDBConnect()
        rows = DB.getRows(' Select ' + str(attributeId) + ' , RegEx, RegExHelper from RegExHelpers')
        regEx = ''
        regExHelper = ''
        if len(rows) >= 1:
            regEx = rows[0].RegEx
            regExHelper = rows[0].RegExHelper

        if matchRegEx == True and not matchRegExHelper:
            return Parser(stringToScan, regEx).doesMatchExist()
        elif not matchRegEx and matchRegExHelper == True:
            return Parser(stringToScan, regExHelper).doesMatchExist()
        elif matchRegEx == False and not matchRegExHelper:
            if Parser(stringToScan, regEx).doesMatchExist() == False:
                return True
            else:
                return False
        elif not matchRegEx and matchRegExHelper == False:
            if Parser(stringToScan, regExHelper).doesMatchExist() == False:
                return True
            else:
                return False
        elif matchRegEx == True and matchRegExHelper == True:
            if Parser(stringToScan, regEx).doesMatchExist() == False and Parser(stringToScan,
                                                                               regExHelper).doesMatchExist() == True:
                return False
            elif Parser(stringToScan, regEx).doesMatchExist() == True and Parser(stringToScan, regExHelper).doesMatchExist() == False:
                return False
            elif Parser(stringToScan, regEx).doesMatchExist() == False and Parser(stringToScan, regExHelper).doesMatchExist() == False:
                return False
            else:
                return True
        elif matchRegEx == True and matchRegExHelper == False:
            if Parser(stringToScan, regEx).doesMatchExist() == False and Parser(stringToScan,
                                                                               regExHelper).doesMatchExist() == False:
                return False
            elif Parser(stringToScan, regEx).doesMatchExist() == False and Parser(stringToScan, regExHelper).doesMatchExist() == True:
                return False
            else:
                return True
        elif matchRegEx == False and matchRegExHelper == True:
            if Parser(stringToScan, regEx).doesMatchExist() == True and Parser(stringToScan,
                                                                                regExHelper).doesMatchExist() == True:
                return False
            elif Parser(stringToScan, regEx).doesMatchExist() == True and Parser(stringToScan, regExHelper).doesMatchExist() == False:
                return False
            else:
                return False
        elif matchRegEx == False and matchRegExHelper == False:
            if Parser(stringToScan, regEx).doesMatchExist() == False and Parser(stringToScan,
                                                                                regExHelper).doesMatchExist() == False:
                return True
            else:
                return False
        else:
            return False
'''
