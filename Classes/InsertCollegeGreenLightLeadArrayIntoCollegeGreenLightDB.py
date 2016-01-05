from Classes.SUDBConnect import SUDBConnect
import time
import re


class InsertCollegeGreenLightLeadArrayIntoCollegeGreenLightDB(object):
    def __init__(self, collegeGreenLightLeadArray, fundingClassification, badScholarshipClassification):
        self.badScholarshipClassification = badScholarshipClassification
        self.fundingClassification = fundingClassification
        self.collegeGreenLightLeadArray = collegeGreenLightLeadArray
        self.db = SUDBConnect()
        self.fileSystemDB = SUDBConnect(destination='filesystem')

        self.name = self.collegeGreenLightLeadArray[0]
        self.amount = self.collegeGreenLightLeadArray[1]
        self.deadline = self.collegeGreenLightLeadArray[2]
        self.sponsor = self.collegeGreenLightLeadArray[3]
        self.description = self.collegeGreenLightLeadArray[4]
        self.requirements = self.collegeGreenLightLeadArray[5]
        self.url = self.collegeGreenLightLeadArray[6]
        self.sourceWebsite = self.collegeGreenLightLeadArray[7]
        self.sourceText = self.collegeGreenLightLeadArray[8]
        self.date = time.strftime('%Y%m%d')

        if not self.checkIfAlreadyInDatabase():
            self.db.insertUpdateOrDeleteDB(
                "INSERT INTO dbo.CollegeGreenLightLeads (Name, Amount, Deadline, Sponsor, Description, Requirements, Url, SourceWebsite, SourceText, Date) VALUES  (N'" + self.name + "', N'" + self.amount + "', N'" + self.deadline + "', N'" + self.sponsor + "', N'" + self.description + "', N'" + self.requirements + "', N'" + self.url + "', N'" + self.sourceWebsite + "', N'" + self.sourceText + "', '" + self.date + "')")
        else:
            self.db.insertUpdateOrDeleteDB(
                "update dbo.CollegeGreenLightLeads set Amount='" + self.amount + "', Deadline='" + self.deadline + "', Sponsor='" + self.sponsor + "', Description='" + self.description + "', Requirements='" + self.requirements + "', SourceWebsite='" + self.sourceWebsite + "', SourceText='" + self.sourceText + "', Date='" + self.date + "' where Name='" + self.name + "' and Url='" + self.url + "'")
        self.writeFileToDisk()

    def writeFileToDisk(self):
        tableName = 'CollegeGreenLightLeads'
        user = 'Kya'
        website = re.sub('Leads', '', tableName)
        columns = self.db.getColumnNamesFromTable(tableName)
        currentRow = self.db.getRowsDB(
            "select * from dbo.CollegeGreenLightLeads where Name='" + self.name + "' and Url='" + self.url + "'")[0]
        self.fileSystemDB.writeFile(columns, currentRow, user, website, self.url, self.date)


    def checkIfAlreadyInDatabase(self):
        matchingRow = self.db.getRowsDB(
            "select * from dbo.CollegeGreenLightLeads where Name='" + self.name + "' and Url='" + self.url + "'")
        if matchingRow != []:
            return True
        else:
            return False
