import pyodbc
import sys


def ConnectToTheDatabase():
    global cnxn, cursor
    cnxn = pyodbc.connect(r'Driver={SQL Server};Server=SUDB-DEV;Database=Spiderman;Trusted_Connection=yes;')
    cursor = cnxn.cursor()


def InsertIntoTestTable():
    cursor.execute("SELECT * FROM dbo.DepartmentTestCases")

def GetRequirementValue():
    requirementvalues = cursor.execute("SELECT TOP 10 RequirementValue FROM dbo.DepartmentTestCases")
    return requirementvalues



ConnectToTheDatabase()
#InsertIntoTestTable()
requirementValues = GetRequirementValue()
print (requirementValues)
#while 1:
#    row = cursor.fetchone()
#    if not row:
#        break
#    print (row.ScholarshipPackageId)
    #process the values and figure out what the answer is
    #call a function that inserts your answer into database
print ("done")
cnxn.close()

