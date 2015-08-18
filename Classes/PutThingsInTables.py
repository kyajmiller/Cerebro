from Classes.SUDBConnect import SUDBConnect


class PutThingsInTables(object):
    def __init__(self, tableName, columnNames, insertValues, whereColumnNames=None, whereValues=None, server='SUDB-DEV',
                 database='Spiderman'):
        self.tableName = 'dbo.%s' % tableName
        self.insertValues = insertValues
        self.columnNames = columnNames
        self.whereValues = whereValues
        self.whereColumnNames = whereColumnNames
        self.server = server
        self.database = database

        self.db = SUDBConnect(server=server, database=database)

    def createSQLQueryInsert(self):
        if self.checkEqualColumnsValues(self.columnNames, self.insertValues):
            columns = self.convertColumnNamesToInsertString()
            values = self.convertValuesToInsertString()
            query = "insert into %s (%s) values (%s)" % (self.tableName, columns, values)
            return query

    def createSQLQueryUpdate(self):
        if self.whereColumnNames and self.whereValues:
            whereStatement = self.creatWhereStatement()

    def convertValuesToInsertString(self):
        convertedList = ["'%s'" % insertValue for insertValue in self.insertValues]
        insertValuesString = ', '.join(convertedList)
        return insertValuesString

    def convertColumnNamesToInsertString(self):
        columnNamesString = ', '.join(self.columnNames)
        return columnNamesString

    def convertValuesToSingleQuoteForm(self, valuesList):
        singleQuoteInsertValues = ["'%s'" % value for value in valuesList]
        return singleQuoteInsertValues

    def checkEqualColumnsValues(self, columns, values):
        if len(columns) == len(values):
            return True

    def creatWhereStatement(self):
        convertedWhereValues = self.convertValuesToSingleQuoteForm(self.whereValues)
        whereColumnValuePairs = []

        # for i in range(len())
