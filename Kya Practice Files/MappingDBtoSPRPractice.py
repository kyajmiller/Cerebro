from Classes.Parser import Parser
from Classes.HTMLWorker import HTMLWorker
from Classes.GPA import GPA
from Classes.Majors import Majors
import pyodbc
import re

def ConnectToTheDatabase():
    global cnxn, cursor
    cnxn = pyodbc.connect(r'Driver={SQL Server};Server=SUDB-DEV;Database=Spiderman;Trusted_Connection=yes;')
    cursor = cnxn.cursor()


def GetInfoFromDatabase():
    cursor.execute("SELECT ScholarshipPackageId, Elgibility FROM dbo.DepartmentTestCases")

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
    Eligibility = re.sub('<.*?>|&nbsp;', '', Eligibility)
    print(Eligibility)

    parseGPA = GPA(Eligibility, ScholarshipIds[e])
    # parseMajor = Majors(Eligibility)

    print(parseGPA.getGPA())
    # print(parseMajor.getMajors())
