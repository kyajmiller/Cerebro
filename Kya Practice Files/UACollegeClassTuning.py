from Classes.UACollege import UACollege
import pyodbc
import re

UAColleges = ['Agriculture & Life Sciences', 'Agriculture and Life Sciences',
              'Architecture, Planning & Landscape Architecture',
              'Architecture Planning and Landscape Architecture', 'Education', 'Engineering', 'Fine Arts', 'Humanities',
              'Medicine', 'Nursing', 'Optical Science', 'Pharmacy', 'Science', 'Social and Behavioral Sciences',
              'Letters, Arts and Science',
              'Management', 'Eller', 'Honors', 'Law', 'James E. Rogers', 'Public Health', 'Outreach College',
              'Graduate College', 'School of Art', 'Landscape Architecture', 'SNRE', 'COM']

UAColleges = '|'.join(UAColleges)


def ConnectToTheDatabase():
    global cnxn, cursor
    cnxn = pyodbc.connect(r'Driver={SQL Server};Server=SUDB-DEV;Database=Spiderman;Trusted_Connection=yes;')
    cursor = cnxn.cursor()


def GetInfoFromDatabase():
    cursor.execute("SELECT ScholarshipPackageId, Elgibility FROM dbo.DepartmentTestCases WHERE AttributeId =377")


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

    testUACollege = UACollege(Eligibility, ScholarshipIds[e], UAColleges)
    print(Eligibility)
    print(testUACollege.getUACollege())
    print('\n\n')
