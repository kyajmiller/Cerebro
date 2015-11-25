import pyodbc


class SUDBConnect(object):
    def __init__(self, server='SUDB-DEV', database='Spiderman', destination='database',
                 filesystemPath='C:\crawlyjones'):
        self.filesystemPath = filesystemPath
        self.destination = destination
        self.server = server
        self.database = database
        self.okayToRunDatabase = False
        self.okayToRunFilesystem = False

        if self.destination == 'database':
            connectionString = r'Driver={SQL Server};Server=%s;Database=%s;Trusted_Connection=yes;' % (
                self.server, self.database)
            self.cnxn = pyodbc.connect(connectionString)
            self.okayToRunDatabase = True
        elif self.destination == 'filesystem':
            self.okayToRunFilesystem = True

    def getRowsDB(self, sql):
        if self.okayToRunDatabase:
            cursor = self.cnxn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows

    def insertUpdateOrDeleteDB(self, sql):
        if self.okayToRunDatabase:
            cursor = self.cnxn.cursor()
            cursor.execute(sql)
            cursor.commit()
            pass

    def getAllTestCases(self):
        return self.getRowsDB("Select * from DepartmentTestCases")

    def getNumberOfTestCases(self, numberToGet):
        return self.getRowsDB("Select top " + str(numberToGet) + " * from DepartmentTestCases")

    def getNumberOfRandomTestCases(self, numberToGet):
        return self.getRowsDB("Select top " + str(numberToGet) + " * from DepartmentTestCases order by newid()")

    def insertIntoJustTests(self, valToInsert):
        self.insertUpdateOrDeleteDB("insert into justtests(testvalue) values ('" + str(valToInsert) + "')")
