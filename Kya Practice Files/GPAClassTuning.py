from Classes.GPA import GPA
import pyodbc

def ConnectToTheDatabase():
    global cnxn, cursor
    cnxn = pyodbc.connect(r'Driver={SQL Server};Server=SUDB-DEV;Database=Spiderman;Trusted_Connection=yes;')
    cursor = cnxn.cursor()


def GetInfoFromDatabase():
    cursor.execute("SELECT ScholarshipPackageId, Elgibility FROM dbo.DepartmentTestCases WHERE AttributeId =1 OR AttributeId =364")

ConnectToTheDatabase()
GetInfoFromDatabase()

Eligibilities = []
while 1:
    row = cursor.fetchone()
    if not row:
        break
    Eligibilities.append(row.Elgibility)

for Eligibility in Eligibilities:
    testGPA = GPA(Eligibility)
    print(Eligibility)
    print(testGPA.getGPA())
    print('\n\n')