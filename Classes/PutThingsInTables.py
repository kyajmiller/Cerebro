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
            whereStatement = self.createWhereStatement()
            setStatement = self.createSetStatement()

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

    def createWhereStatement(self):
        convertedWhereValues = self.convertValuesToSingleQuoteForm(self.whereValues)
        whereColumnValuePairs = []

        if self.checkEqualColumnsValues(self.whereColumnNames, convertedWhereValues):
            for i in range(len(self.whereColumnNames)):
                column = self.whereColumnNames[i]
                value = convertedWhereValues[i]
                pairString = "%s=%s" % (column, value)
                whereColumnValuePairs.append(pairString)

        whereColumnValuePairsString = ' and '.join(whereColumnValuePairs)
        whereStatement = 'where %s' % whereColumnValuePairsString
        return whereStatement

    def createSetStatement(self):
        convertedInsertValues = self.convertValuesToSingleQuoteForm(self.insertValues)
        setColumnValuePairs = []

        if self.checkEqualColumnsValues(self.columnNames, convertedInsertValues):
            for i in range(len(self.columnNames)):
                column = self.columnNames[i]
                value = convertedInsertValues[i]
                pairString = "%s=%s" % (column, value)
                setColumnValuePairs.append(pairString)

        setColumnValuePairsString = ', '.join(setColumnValuePairs)
        setStatement = 'set %s' % setColumnValuePairsString
        return setStatement
