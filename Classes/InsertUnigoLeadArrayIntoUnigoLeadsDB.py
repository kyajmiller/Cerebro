from Classes.SUDBConnect import SUDBConnect


class InsertUnigoLeadArrayIntoUnigoLeadsDB(object):
    def __init__(self, unigoLeadArray):
        self.unigoLeadArray = unigoLeadArray
        self.db = SUDBConnect()

        self.name = self.unigoLeadArray[0]
        self.amount = self.unigoLeadArray[1]
        self.deadline = self.unigoLeadArray[2]
        self.sponsor = self.unigoLeadArray[3]
        self.awardAmount = self.unigoLeadArray[4]
        self.recipients = self.unigoLeadArray[5]
        self.requirements = self.unigoLeadArray[6]
        self.additionalInfo = self.unigoLeadArray[7]
        self.contact = self.unigoLeadArray[8]
        self.address = self.unigoLeadArray[9]
        self.sourceWebsite = self.unigoLeadArray[10]
        self.sourceText = self.unigoLeadArray[11]

        if not self.checkIfAlreadyInDatabase():
            self.db.insertUpdateOrDeleteDB(
                "INSERT INTO dbo.UnigoLeads (Name, Amount, Deadline, Sponsor, AwardAmount, Recipients, Requirements, AdditionalInfo, Contact, Address, SourceWebsite, SourceText) VALUES ( N'" + self.name + "', N'" + self.amount + "', N'" + self.deadline + "', N'" + self.sponsor + "', N'" + self.awardAmount + "', N'" + self.recipients + "', N'" + self.requirements + "', N'" + self.additionalInfo + "', N'" + self.contact + "', N'" + self.address + "', N'" + self.sourceWebsite + "', N'" + self.sourceText + "')")

    def checkIfAlreadyInDatabase(self):
        matchingRow = self.db.getRowsDB(
            "select Name, AdditionalInfo from dbo.UnigoLeads where Name='" + self.name + "' and AdditionalInfo='" + self.additionalInfo + "'")
        if matchingRow != []:
            return True
        else:
            return False
