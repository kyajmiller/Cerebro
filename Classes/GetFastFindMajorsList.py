import re
from Classes.SUDBConnect import SUDBConnect


class GetFastFindMajorsList(object):
    @staticmethod
    def getDefaultList():
        fastFindMajorsList = []
        db = SUDBConnect()
        rows = db.getRows(
            "select replace( ValueShown, '(' + OtherValuesToCheck + ')', '') as Major from dbo.FastFindLists where AttributeId=417")
        for row in rows:
            fastFindMajorsList.append(row.Major)

        fastFindMajorsList = [re.sub('\(.*?\)', '', major.strip()) for major in fastFindMajorsList]

        return fastFindMajorsList

    @staticmethod
    def getGrantForwardItemsList():
        fastFindMajorsList = GetFastFindMajorsList.getDefaultList()
        db = SUDBConnect

        rows = db.getRows("SELECT DISTINCT Keyword FROM dbo.GrantForwardItems")
        existingKeywordsInTable = []
        for row in rows:
            existingKeywordsInTable.append(' ' + row.Keyword)

        for major in existingKeywordsInTable:
            if major in fastFindMajorsList:
                fastFindMajorsList.remove(major)
                fastFindMajorsList.append(major)

        return fastFindMajorsList

    @staticmethod
    def getPivotLeadsList():
        fastFindMajorsList = GetFastFindMajorsList.getDefaultList()
        db = SUDBConnect()

        rows = db.getRows("SELECT DISTINCT Keyword FROM dbo.PivotLeads")
        existingKeywordsInTable = []
        for row in rows:
            existingKeywordsInTable.append(' ' + row.Keyword)

        for major in existingKeywordsInTable:
            if major in fastFindMajorsList:
                fastFindMajorsList.remove(major)
                fastFindMajorsList.append(major)

        return fastFindMajorsList
