from Classes.SUDBConnect import SUDBConnect


class InsertScholarships360LeadArrayIntoScholarships360DB(object):
    def __init__(self, scholarships360LeadArray):
        self.scholarships360LeadArray = scholarships360LeadArray
        self.db = SUDBConnect()

        self.name = self.scholarships360LeadArray[0]
        self.url = self.scholarships360LeadArray[1]
        self.description = self.scholarships360LeadArray[2]
        self.eligibility = self.scholarships360LeadArray[3]
        self.amount = self.scholarships360LeadArray[4]
        self.amountInfo = self.scholarships360LeadArray[5]
        self.deadline = self.scholarships360LeadArray[6]
        self.deadlineInfo = self.scholarships360LeadArray[7]
        self.sourceWebsite = self.scholarships360LeadArray[8]
        self.sourceText = self.scholarships360LeadArray[9]

        if not self.checkIfAlreadyInDB():
            self.db.insertUpdateOrDelete(
                "INSERT INTO dbo.Scholarships360Leads (Name, Url, Description, Eligibility, Amount, AmountInfo, Deadline, DeadlineInfo, SourceWebsite, SourceText) VALUES (N'" + self.name + "', N'" + self.url + "', N'" + self.description + "', N'" + self.eligibility + "', N'" + self.amount + "', N'" + self.amountInfo + "', N'" + self.deadline + "', N'" + self.deadlineInfo + "', N'" + self.sourceWebsite + "', N'" + self.sourceText + "')")

    def checkIfAlreadyInDB(self):
        matchingRow = self.db.getRows(
            "select * from dbo.Scholarships360Leads where Name='" + self.name + "' and Description='" + self.description + "'")
        if matchingRow != []:
            return True
        else:
            return False
