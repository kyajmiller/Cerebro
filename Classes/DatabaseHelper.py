import pyodbc
from Classes.SUDBConnect import SUDBConnect


class DatabaseHelper(SUDBConnect):
    @staticmethod
    def getOnlyOneRegex(attributeId):
        DB = SUDBConnect()
        rows = DB.getRows(' Select ' + str(attributeId) + ' , RegEx from RegExHelpers')
        if len(rows) >= 1:
            return rows[0].RegEx
        else:
            return ''

    @staticmethod
    def getOnlyOneRegexHelper(attributeId):
        DB = SUDBConnect()
        rows = DB.getRows(' Select ' + str(attributeId) + ' , RegExHelper from RegExHelpers')
        if len(rows) >= 1:
            return rows[0].RegEx
        else:
            return ''

    @staticmethod
    def getOnlyOneRegexAndRegexHelper(attributeId):
        DB = SUDBConnect()
        rows = DB.getRows(' Select ' + str(attributeId) + ' , RegEx, RegExHelper from RegExHelpers')
        if len(rows) >= 1:
