import pyodbc
import re
from Classes.GPA import GPA


class MapDBtoSPR(object):
    def __init__(self, SQLQuery):
        self.SQLQuery = SQLQuery
        self.eligibilities = []
        self.scholarshipIds = []


    def connectToTheDatabase(self):
        global cnxn, cursor
        cnxn = pyodbc.connect(r'Driver={SQL Server};Server=SUDB-DEV;Database=Spiderman;Trusted_Connection=yes;')
        cursor = cnxn.cursor()

    def getInfoFromDatabase(self):
        cursor.execute(self.SQLQuery)

    def populateEligibilitiesandScholarshipIds(self):
        self.connectToTheDatabase()
        self.getInfoFromDatabase()

        while 1:
            row = cursor.fetchone()
            if not row:
                break
            self.eligibilities.append(row.Elgibility)
            self.scholarshipIds.append(row.ScholarshipPackageId)

        return None

    def doGPAParser(self, eligibility, scholarshipId):
        parseGPA = GPA(eligibility, scholarshipId)
        if parseGPA.getGPA() != '':
            print(parseGPA.getGPA())
            # return parseGPA.getScholarshipPackageRequirementFormat()

    def loopOverEligibilities(self):
        self.populateEligibilitiesandScholarshipIds()
        for i in range(len(self.eligibilities)):
            scholarshipId = self.scholarshipIds[i]

            eligibility = self.eligibilities[i]
            eligibility = re.sub('<.*?>|&nbsp;', '', eligibility)

            splitEligibility = eligibility.split('\n')
            for eligibility in splitEligibility:
                self.doGPAParser(eligibility, scholarshipId)


test = MapDBtoSPR("SELECT ScholarshipPackageId, Elgibility FROM dbo.DepartmentTestCases")
test.loopOverEligibilities()
