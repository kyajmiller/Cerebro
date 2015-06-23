from Classes.Parser import Parser
from Classes.HTMLWorker import HTMLWorker
import pyodbc
import re

def ConnectToTheDatabase():
    global cnxn, cursor
    cnxn = pyodbc.connect(r'Driver={SQL Server};Server=SUDB-DEV;Database=Spiderman;Trusted_Connection=yes;')
    cursor = cnxn.cursor()


def GetInfoFromDatabase():
    cursor.execute("SELECT ScholarshipPackageId, Elgibility FROM dbo.DepartmentTestCases WHERE AttributeId =1 OR AttributeId =364")

ConnectToTheDatabase()
GetInfoFromDatabase()

Eligibilities = []
ScholarshipIds = []
while 1:
    row = cursor.fetchone()
    if not row:
        break
    Eligibilities.append(row.Elgibility)
    ScholarshipIds.append(row.ScholarshipPackageId)

for e in range(len(Eligibilities)):
    print(ScholarshipIds[e])

    Eligibility = Eligibilities[e]
    # cleanEligibility = HTMLWorker.cleanWebPageBeforeProcessing(Eligibility)
    cleanEligibility = re.sub('<.*?>', '', Eligibility)
    print(cleanEligibility)
