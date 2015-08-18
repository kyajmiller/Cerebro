from Classes.SUDBConnect import SUDBConnect


class PutThingsInTables(object):
    def __init__(self, tableName, columnNames, insertValues, server='SUDB-DEV', database='Spiderman'):
        self.tableName = 'dbo.%s' % tableName
        self.insertValues = insertValues
        self.columnNames = columnNames
        self.server = server
        self.database = database

        self.db = SUDBConnect(server=server, database=database)

    def createSQLQueryInsert(self):
        if self.checkEqualColumnsValues():
            columns = self.convertColumnNamesToInsertString()
            values = self.convertInsertValuesToInsertString()
            query = "insert into %s (%s) values (%s)" % (self.tableName, columns, values)
            return query

    # def createSQLQueryUpdate(self):


    def convertInsertValuesToInsertString(self):
        convertedList = ["'%s'" % insertValue for insertValue in self.insertValues]
        insertValuesString = ', '.join(convertedList)
        return insertValuesString

    def convertColumnNamesToInsertString(self):
        columnNamesString = ', '.join(self.columnNames)
        return columnNamesString

    def convertInsertValuesToSingleQuoteForm(self):
        singleQuoteInsertValues = ["'%s'" % insertValue for insertValue in self.insertValues]
        return singleQuoteInsertValues

    def checkEqualColumnsValues(self):
        if len(self.insertValues) == len(self.columnNames):
            return True
