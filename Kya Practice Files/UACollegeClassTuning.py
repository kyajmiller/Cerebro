from Classes.UACollege import UACollege
import pyodbc
import re

UAColleges = ['agriculture & life sciences', 'agriculture and life sciences',
              'architecture, planning & landscape architecture',
              'architecture planning and landscape architecture', 'education', 'engineering', 'fine arts', 'humanities',
              'medicine', 'nursing', 'optical science', 'pharmacy', 'science', 'social and behavioral science',
              'letters, arts and science',
              'management', 'eller', 'honors', 'law', 'james e. rogers', 'public health', 'outreach college',
              'graduate college', 'school of art', 'landscape architecture', 'snre', 'ua south']

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
