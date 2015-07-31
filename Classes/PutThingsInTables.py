from Classes.SUDBConnect import SUDBConnect


class PutThingsInTables(object):
    def __init__(self, tableName, insertValues, columnNames, server='SUDB-DEV', database='Spiderman'):
        self.tableName = tableName
        self.tableName = 'dbo.%s' % tableName
        self.insertValues = insertValues
        self.columnNames = columnNames
        self.server = server
        self.database = database

        self.db = SUDBConnect(server=server, database=database)

    def doInsert(self):
        convertInsertValuesToStrings = []
        for value in self.insertValues:
            convertInsertValuesToStrings.append(str(value))
        insertValueString = ', '.join(convertInsertValuesToStrings)
        print(insertValueString)


PutThingsInTables('Tests', ['testinsert', 8], ['Regex', 'AttributeId']).doInsert()
