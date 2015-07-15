from Classes.SUDBConnect import SUDBConnect


class InsertGrantForwardLeadsArrayIntoGrantForwardItems(object):
    def __init__(self, grantForwardLeadArray):
        self.grantForwardLeadArray = grantForwardLeadArray
        db = SUDBConnect()
        keyword = self.grantForwardLeadArray[0]
        url = self.grantForwardLeadArray[1]
        name = self.grantForwardLeadArray[2]
        description = self.grantForwardLeadArray[3]
        sponsor = self.grantForwardLeadArray[4]
        amount = self.grantForwardLeadArray[5]
        eligibility = self.grantForwardLeadArray[6]
        submissionInfo = self.grantForwardLeadArray[7]
        categories = self.grantForwardLeadArray[8]
        opportunitySourceLink = self.grantForwardLeadArray[9]
        opportunitySourceText = self.grantForwardLeadArray[10]
        db.insertUpdateOrDelete(
            "insert into dbo.GrantForwardItems (Keyword, Url, Name, Description, Sponsor, Amount, Eligibility, SubmissionInfo, Categories, OpportunitySourceLink, OpportunitySourceText) values (N'" + keyword + "', N'" + url + "', N'" + name + "', N'" + description + "', N'" + sponsor + "', N'" + amount + "', N'" + eligibility + "', N'" + submissionInfo + "', N'" + categories + "', N'" + opportunitySourceLink + "', N'" + opportunitySourceText + "')")
