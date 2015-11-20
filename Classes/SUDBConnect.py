import pyodbc


class SUDBConnect(object):
    def __init__(self, server='SUDB-DEV', database='Spiderman', destination='database',
                 filesystemPath='C:\crawlyjones'):
        self.filesystemPath = filesystemPath
        self.destination = destination
        self.server = server
        self.database = database
        self.okayToRun = False

        if self.destination == 'database':
            connectionString = r'Driver={SQL Server};Server=%s;Database=%s;Trusted_Connection=yes;' % (
                self.server, self.database)
            self.cnxn = pyodbc.connect(connectionString)
            self.okayToRun = True
        elif self.destination == 'filesystem' and self.filesystemPath != 'C:\crawlyjones':
            self.okayToRun = True

    def getRows(self, sql):
        if self.okayToRun:
            cursor = self.cnxn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows

    def insertUpdateOrDelete(self, sql):
        if self.okayToRun:
            cursor = self.cnxn.cursor()
            cursor.execute(sql)
            cursor.commit()
            pass

    def getAllTestCases(self):
        return self.getRows("Select * from DepartmentTestCases")

    def getNumberOfTestCases(self, numberToGet):
        return self.getRows("Select top " + str(numberToGet) + " * from DepartmentTestCases")

    def getNumberOfRandomTestCases(self, numberToGet):
        return self.getRows("Select top " + str(numberToGet) + " * from DepartmentTestCases order by newid()")

    def insertIntoJustTests(self, valToInsert):
        self.insertUpdateOrDelete("insert into justtests(testvalue) values ('" + str(valToInsert) + "')")
