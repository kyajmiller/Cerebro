import pyodbc
import re
from Classes.GPA import GPA


class MapDBtoSPR(object):
    def __init__(self):
        self.eligibilities = []
        self.scholarshipIds = []

    def connectToTheDatabase(self):
        global cnxn, cursor
        cnxn = pyodbc.connect(r'Driver={SQL Server};Server=SUDB-DEV;Database=Spiderman;Trusted_Connection=yes;')
        cursor = cnxn.cursor()

    def getInfoFromDatabase(self):
        cursor.execute("SELECT ScholarshipPackageId, Elgibility FROM dbo.DepartmentTestCases")

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

    def doGPAParser(self):
        for i in range(len(self.eligibilities)):
            scholarshipId = self.scholarshipIds[i]
            eligibility = self.eligibilities[i]
            eligibility = re.sub('<.*?>|&nbsp;', '', eligibility)

            # print(eligibility)
            parseGPA = GPA(eligibility, scholarshipId)
            print(parseGPA.getGPA())


'''
test = MapDBtoSPR()
test.populateEligibilitiesandScholarshipIds()
test.doGPAParser()
'''
