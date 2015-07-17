from Classes.SUDBConnect import SUDBConnect


class GetFastFindMajorsList(object):
    @staticmethod
    def getList(tableName=None):
        fastFindMajorsList = []
        db = SUDBConnect()
        rows = db.getRows(
            "select replace( ValueShown, '(' + OtherValuesToCheck + ')', '') as Major from dbo.FastFindLists where AttributeId=417")
        for row in rows:
            fastFindMajorsList.append(row.Major)

        if tableName == 'GrantForwardItems':
            rows = db.getRows("SELECT DISTINCT Keyword FROM dbo.GrantForwardItems")
            existingKeywordsInTable = []
            for row in rows:
                existingKeywordsInTable.append(' ' + row.Keyword)

            for major in existingKeywordsInTable:
                if major in fastFindMajorsList:
                    fastFindMajorsList.remove(major)
                    fastFindMajorsList.append(major)

        '''

        if tableName == 'PivotLeads':
            rows = db.getRows("SELECT DISTINCT Keyword FROM dbo.PivotLeads")
            existingKeywordsInTable = []
            for row in rows:
                existingKeywordsInTable.append(row.Keyword)

            for major in existingKeywordsInTable:
                if major in fastFindMajorsList:
                    fastFindMajorsList.remove(major)
                    fastFindMajorsList.append(major)
        '''

        return fastFindMajorsList
