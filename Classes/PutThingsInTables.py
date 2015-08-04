from Classes.SUDBConnect import SUDBConnect


class PutThingsInTables(object):
    def __init__(self, tableName, columnNames, insertValues, server='SUDB-DEV', database='Spiderman'):
        self.tableName = 'dbo.%s' % tableName
        self.insertValues = insertValues
        self.columnNames = columnNames
        self.server = server
        self.database = database

        self.db = SUDBConnect(server=server, database=database)

    def createSQLQuery(self):
        if self.checkEqualColumnsValues():
            columns = self.convertColumnNames()
            values = self.convertInsertValues()
            query = "insert into %s (%s) values (%s)" % (self.tableName, columns, values)
            return query

    def convertInsertValues(self):
        convertedList = []
        for value in self.insertValues:
            convertedValue = "'%s'" % value
            convertedList.append(convertedValue)
        insertValuesString = ', '.join(convertedList)
        return insertValuesString

    def convertColumnNames(self):
        columnNamesString = ', '.join(self.columnNames)
        return columnNamesString

    def checkEqualColumnsValues(self):
        if len(self.insertValues) == len(self.columnNames):
            return True
