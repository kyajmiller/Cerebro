from Classes.SUDBConnect import SUDBConnect
import re
import time


class InsertTeacherDotOrgLeadArrayIntoTeacherDotOrgDB(object):
    def __init__(self, teacherDotOrgLeadArray, fundingClassification, badScholarshipClassification):
        self.teacherDotOrgLeadArray = teacherDotOrgLeadArray
        self.fundingClassification = fundingClassification
        self.badScholarshipClassification = badScholarshipClassification
        self.db = SUDBConnect()
        self.fileSystemDB = SUDBConnect(destination='filesystem')

        self.name = teacherDotOrgLeadArray[0]
        self.description = teacherDotOrgLeadArray[1]
        self.requirements = teacherDotOrgLeadArray[2]
        self.sourceWebsite = teacherDotOrgLeadArray[3]
        self.sourceText = teacherDotOrgLeadArray[4]
        self.date = time.strftime('%Y%m%d')

    def writeFileToDisk(self):
        tableName = 'TeacherDotOrgLeads'
        user = 'Kya'
        website = re.sub('Leads', '', tableName)
        columns = self.db.getColumnNamesFromTable(tableName)
        currentRow = self.db.getRowsDB(
                "select * from dbo.TeacherDotOrgLeads where Name='" + self.name + "' and SourceWebsite='" + self.sourceWebsite + "'")[
            0]
        self.fileSystemDB.writeFile(columns, currentRow, user, website, self.sourceWebsite, self.date)

    def checkIfAlreadyInDatabase(self):
        matchingRow = self.db.getRowsDB(
                "select * from dbo.TeacherDotOrgLeads where Name='" + self.name + "' and SourceWebsite='" + self.sourceWebsite + "'")
        if matchingRow != []:
            return True
        else:
            return False
