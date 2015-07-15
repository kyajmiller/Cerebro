from Classes.SUDBConnect import SUDBConnect


class InsertGrantForwardLeadsArrayIntoGrantForwardItems(object):
    def __init__(self, grantForwardLeadArray):
        self.grantForwardLeadArray = grantForwardLeadArray
        self.db = SUDBConnect()
        self.keyword = self.grantForwardLeadArray[0]
        self.url = self.grantForwardLeadArray[1]
        self.name = self.grantForwardLeadArray[2]
        self.description = self.grantForwardLeadArray[3]
        self.sponsor = self.grantForwardLeadArray[4]
        self.amount = self.grantForwardLeadArray[5]
        self.eligibility = self.grantForwardLeadArray[6]
        self.submissionInfo = self.grantForwardLeadArray[7]
        self.categories = self.grantForwardLeadArray[8]
        self.opportunitySourceLink = self.grantForwardLeadArray[9]
        self.opportunitySourceText = self.grantForwardLeadArray[10]

        if not self.checkIfAlreadyInDatabase():
            self.db.insertUpdateOrDelete(
                "insert into dbo.GrantForwardItems (Keyword, Url, Name, Description, Sponsor, Amount, Eligibility, SubmissionInfo, Categories, OpportunitySourceLink, OpportunitySourceText) values (N'" + self.keyword + "', N'" + self.url + "', N'" + self.name + "', N'" + self.description + "', N'" + self.sponsor + "', N'" + self.amount + "', N'" + self.eligibility + "', N'" + self.submissionInfo + "', N'" + self.categories + "', N'" + self.opportunitySourceLink + "', N'" + self.opportunitySourceText + "')")

    def checkIfAlreadyInDatabase(self):
        matchingRow = self.db.getRows(
            "select * from dbo.GrantForwardItems where Keyword='" + self.keyword + "' and Url='" + self.url + "'")
        if matchingRow != []:
            return True
        else:
            return False
