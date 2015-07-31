import pyodbc

class SUDBConnect(object):
    def __init__(self, database='Spiderman', server='SUDB-DEV'):
        self.server = server
        self.database = database
        connectionString = r'Driver={SQL Server};Server=%s;Database=%s;Trusted_Connection=yes;' % (
        self.server, self.database)
        self.cnxn = pyodbc.connect(connectionString)

    def getRows(self,sql):
        cursor = self.cnxn.cursor()
        cursor.execute(sql)
        rows= cursor.fetchall()
        return rows
    def insertUpdateOrDelete(self,sql):
        cursor = self.cnxn.cursor()
        cursor.execute(sql)
        cursor.commit()
        pass
    def getAllTestCases(self):
        return self.getRows("Select * from DepartmentTestCases")
    def getNumberOfTestCases(self,numberToGet):
        return self.getRows("Select top " + str(numberToGet) + " * from DepartmentTestCases")
    def getNumberOfRandomTestCases(self,numberToGet):
        return self.getRows("Select top " + str(numberToGet) + " * from DepartmentTestCases order by newid()")
    def insertIntoJustTests(self,valToInsert):
        self.insertUpdateOrDelete("insert into justtests(testvalue) values ('" + str(valToInsert) + "')")
