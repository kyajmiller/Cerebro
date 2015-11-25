from Classes.SUDBConnect import SUDBConnect


class InsertIefaLeadArrayIntoIefaLeadsDB(object):
    def __init__(self, iefaLeadArray):
        self.iefaLeadArray = iefaLeadArray
        self.db = SUDBConnect()

        self.name = self.iefaLeadArray[0]
        self.url = self.iefaLeadArray[1]
        self.sponsor = self.iefaLeadArray[2]
        self.submissionDeadline = self.iefaLeadArray[3]
        self.majors = self.iefaLeadArray[4]
        self.amount = self.iefaLeadArray[5]
        self.description = self.iefaLeadArray[6]
        self.otherCriteria = self.iefaLeadArray[7]
        self.numberAwards = self.iefaLeadArray[8]
        self.hostInstitution = self.iefaLeadArray[9]
        self.includes = self.iefaLeadArray[10]
        self.nationalityRequired = self.iefaLeadArray[11]
        self.hostCountries = self.iefaLeadArray[12]
        self.sourceWebsite = self.iefaLeadArray[13]
        self.sourceText = self.iefaLeadArray[14]

        if not self.checkIfAlreadyInDatabase():
            self.db.insertUpdateOrDeleteDB(
                "INSERT INTO dbo.IefaLeads (Name, Url, Sponsor, SubmissionDeadline, Majors, Amount, Description, OtherCriteria, NumberAwards, HostInstitution, Includes, NationalityRequired, HostCountries, SourceWebsite, SourceText) VALUES  (N'" + self.name + "', N'" + self.url + "', N'" + self.sponsor + "', N'" + self.submissionDeadline + "', N'" + self.majors + "', N'" + self.amount + "', N'" + self.description + "', N'" + self.otherCriteria + "', N'" + self.numberAwards + "', N'" + self.hostInstitution + "', N'" + self.includes + "', N'" + self.nationalityRequired + "', N'" + self.hostCountries + "', N'" + self.sourceWebsite + "', N'" + self.sourceText + "')")

    def checkIfAlreadyInDatabase(self):
        matchingRow = self.db.getRowsDB(
            "select * from dbo.IefaLeads where Name='" + self.name + "' and Description='" + self.description + "'")
        if matchingRow != []:
            return True
        else:
            return False
