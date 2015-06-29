import pyodbc
from Classes.SUDBConnect import SUDBConnect


class DatabaseHelper(SUDBConnect):
    @staticmethod
    def getOnlyOneRegex(attributeId):
        DB = SUDBConnect()
        rows = DB.getRows(' Select ' + str(attributeId) + ' , RegEx from RegExHelpers')
        if len(rows) >= 1:
            return rows[0].RegEx

    @staticmethod
    def getOnlyOneRegexHelper(attributeId):
        DB = SUDBConnect()
        rows = DB.getRows(' Select ' + str(attributeId) + ' , RegExHelper from RegExHelpers')
        if len(rows) >= 1:
            return rows[0].RegExHelper

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
