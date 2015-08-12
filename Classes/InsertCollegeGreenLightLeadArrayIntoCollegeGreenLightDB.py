from Classes.SUDBConnect import SUDBConnect


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

        if not self.checkIfAlreadyInDatabase():
            self.db.insertUpdateOrDelete(
                "INSERT INTO dbo.CollegeGreenLightLeads (Name, Amount, Deadline, Sponsor, Description, Requirements, Url, SourceWebsite, SourceText) VALUES  (N'" + self.name + "', N'" + self.amount + "', N'" + self.deadline + "', N'" + self.sponsor + "', N'" + self.description + "', N'" + self.requirements + "', N'" + self.url + "', N'" + self.sourceWebsite + "', N'" + self.sourceText + "')")

    def checkIfAlreadyInDatabase(self):
        matchingRow = self.db.getRows(
            "select * from dbo.CollegeGreenLightLeads where Name='" + self.name + "' and Url='" + self.url + "'")
        if matchingRow != []:
            return True
        else:
            return False