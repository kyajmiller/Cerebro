import pyodbc


class AttributeIdAssociatedRegex(object):
    def __init__(self, attributeId, tableName):
        self.tableName = tableName
        self.attributeId = attributeId
        self.associatedRegex = ''

    def connectToTheDatabase(self):
        global cnxn, cursor
        cnxn = pyodbc.connect(r'Driver={SQL Server};Server=SUDB-DEV;Database=Spiderman;Trusted_Connection=yes;')
        cursor = cnxn.cursor()

    def getInfoFromDatabase(self):
        cursor.execute("SELECT RegEx FROM '" + self.tableName + "' WHERE AttributeId ='" + self.attributeId + "'")

    def getAssociatedRegexFromDatabase(self):
        self.connectToTheDatabase()
        self.getInfoFromDatabase()

        while 1:
            row = cursor.fetchone()
            if not row:
                break

            self.associatedRegex = row.RegEx

        return self.associatedRegex
