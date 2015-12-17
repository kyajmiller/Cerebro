from Classes.SUDBConnect import SUDBConnect
import time


class InsertCollegeGreenLightLeadArrayIntoCollegeGreenLightDB(object):
    def __init__(self, collegeGreenLightLeadArray):
        self.collegeGreenLightLeadArray = collegeGreenLightLeadArray
        self.db = SUDBConnect()

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

    def checkIfAlreadyInDatabase(self):
        matchingRow = self.db.getRowsDB(
            "select * from dbo.CollegeGreenLightLeads where Name='" + self.name + "' and Url='" + self.url + "'")
        if matchingRow != []:
            return True
        else:
            return False
