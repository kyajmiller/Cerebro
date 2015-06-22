from Classes.GPA import GPA
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
    Eligibility = Eligibilities[e]
    print(ScholarshipIds[e])

    FormattedEligibilities = []
    StripULTag = re.sub('<ul>|</ul>', '', Eligibility)
    Eligibility = StripULTag
    IndividualEligibilities = Eligibility.split('</li>')
    for IndividualEligibility in IndividualEligibilities:
        IndividualEligibility.strip('\r')
        IndividualEligibility.strip('\n')
        StripXMLTags = re.sub('<\/*[a-z]*\s*\/*>', '', IndividualEligibility)
        #need to remove the xml tags first (specificially the end of line) or else the next one will capture the whole
        #string and delete it
        StripRemainingTags = re.sub('<.*>', '', StripXMLTags)
        IndividualEligibility = StripRemainingTags
        FormattedEligibilities.append(IndividualEligibility)

    JoinEligibilitytoString = ', '.join(FormattedEligibilities)
    StripApostrophe = re.sub('\'*\"*', '', JoinEligibilitytoString)
    Stripnbsp = re.sub('&nbsp;', '', StripApostrophe)
    JoinEligibilitytoString = Stripnbsp

    Eligibility = JoinEligibilitytoString

    testGPA = GPA(Eligibility, ScholarshipIds[e])
    print(Eligibility)
    print(testGPA.getGPA())
    print('\n\n')