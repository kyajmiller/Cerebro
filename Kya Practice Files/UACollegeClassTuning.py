from Classes.UACollege import UACollege
import pyodbc
import re

UAColleges = ['College of Agriculture & Life Sciences', 'College of Agriculture and Life Sciences',
              'College of Architecture, Planning & Landscape Architecture',
              'College of Architecture Planning and Landscape Architecture', 'College of Education',
              'College of Engineering', 'School of Fine Arts', 'College of Humanities',
              'College of Medicine', 'College of Nursing', 'College of Optical Science', 'College of Pharmacy',
              'College of Science', 'College of Social and Behavioral Sciences',
              'College of Letters, Arts and Science',
              'College of Management', 'Eller College', 'Honors College', 'Law', 'James E. Rogers', 'Public Health',
              'Outreach College',
              'Graduate College', 'School of Art', 'College of Landscape Architecture', 'SNRE', 'COM']

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
