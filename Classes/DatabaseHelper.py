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
        # trueParser = ', '.join(Parser(stringToScan, searchCriteria).getResult())
        return Parser(stringToScan, searchCriteria).doesMatchExist()

    @staticmethod
    def getOnlyOneRegexHelper(attributeId, stringToScan):
        DB = SUDBConnect()
        rows = DB.getRows(' Select ' + str(attributeId) + ' , RegExHelper from RegExHelpers')
        searchCriteria = ''
        if len(rows) >= 1:
            searchCriteria = rows[0].RegExHelper
        return Parser(stringToScan, searchCriteria).doesMatchExist()

    @staticmethod
    def getOnlyOneRegexAndRegexHelper(attributeId):
        DB = SUDBConnect()
        rows = DB.getRows(' Select ' + str(attributeId) + ' , RegEx, RegExHelper from RegExHelpers')
        if len(rows) >= 1:
            return (rows[0].RegEx, rows[0].RegExHelper)

    @staticmethod
    def getAllRegex(attributeId):
        DB = SUDBConnect()
        rows = DB.getRows(' Select ' + str(attributeId) + ' , RegEx from RegExHelpers')
        regExArray = []
        if len(rows) >= 1:
            for row in rows:
                regExArray.append(row.RegEx)
            return regExArray

    @staticmethod
    def getAllRegexHelper(attributeId):
        DB = SUDBConnect()
        rows = DB.getRows(' Select ' + str(attributeId) + ' , RegExHelper from RegExHelpers')
        regExHelperArray = []
        if len(rows) >= 1:
            for row in rows:
                regExHelperArray.append(row.RegExHelper)
            return regExHelperArray

    @staticmethod
    def getAllRegexAndRegexHelper(attributeId):
        DB = SUDBConnect()
        rows = DB.getRows(' Select ' + str(attributeId) + ' , RegEx, RegExHelper from RegExHelpers')
        regExArray = []
        regExHelperArray = []
        if len(rows) >= 1:
            for row in rows:
                regExArray.append(row.RegEx)
                regExHelperArray.append(row.RegExHelper)
            return (regExArray, regExHelperArray)