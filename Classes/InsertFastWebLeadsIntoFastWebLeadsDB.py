from Classes.SUDBConnect import SUDBConnect


class InsertFastWebLeadIntoFastWebLeadsDB(object):
    def __init__(self, fastWebLeadArray):
        self.fastWebLeadArray = fastWebLeadArray
        self.db = SUDBConnect()

        self.name = self.fastWebLeadArray[0]
        self.url = self.fastWebLeadArray[1]
        self.sponsor = self.fastWebLeadArray[2]
        self.amount = self.fastWebLeadArray[3]
        self.deadline = self.fastWebLeadArray[4]
        self.description = self.fastWebLeadArray[5]
        self.awardType = self.fastWebLeadArray[6]
        self.numAwards = self.fastWebLeadArray[7]
        self.majors = self.fastWebLeadArray[8]
        self.additionalInfo = self.fastWebLeadArray[9]
        self.sourceWebsite = self.fastWebLeadArray[10]
        self.sourceText = self.fastWebLeadArray[11]

        if not self.checkIfAlreadyInDatabase():
            self.db.insertUpdateOrDelete(
                "insert into dbo.FastWebLeads (Name, Url, Sponsor, Amount, Deadline, Description, AwardType, NumAwards, Majors, AdditionalInfo, SourceWebsite, SourceText) values (N'" + self.name + "', N'" + self.url + "', N'" + self.sponsor + "', N'" + self.amount + "', N'" + self.deadline + "', N'" + self.description + "', N'" + self.awardType + "', N'" + self.numAwards + "', N'" + self.majors + "', N'" + self.additionalInfo + "', N'" + self.sourceWebsite + "', N'" + self.sourceText + "')")

    def checkIfAlreadyInDatabase(self):
        matchingRow = self.db.getRows(
            "select * from dbo.FastWebLeads where Name='" + self.name + "' and Url='" + self.url + "'")
        if matchingRow != []:
            return True
        else:
            return False
