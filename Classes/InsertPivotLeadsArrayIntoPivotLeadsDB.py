from Classes.SUDBConnect import SUDBConnect


class InsertPivotLeadsArrayIntoPivotLeadsDB(object):
    def __init__(self, pivotLeadsArray):
        self.pivotLeadsArray = pivotLeadsArray
        self.db = SUDBConnect()

        self.keyword = self.pivotLeadsArray[0]
        self.url = self.pivotLeadsArray[1]
        self.name = self.pivotLeadsArray[2]
        self.abstract = self.pivotLeadsArray[3]
        self.sponsor = self.pivotLeadsArray[4]
        self.amount = self.pivotLeadsArray[5]
        self.applicantType = self.pivotLeadsArray[6]
        self.citizenshipResidency = self.pivotLeadsArray[7]
        self.activityLocation = self.pivotLeadsArray[8]
        self.eligibility = self.pivotLeadsArray[9]
        self.categories = self.pivotLeadsArray[10]
        self.sourceWebsite = self.pivotLeadsArray[11]
        self.sourceText = self.pivotLeadsArray[12]

        if not self.checkIfAlreadyInDatabase():
            self.db.insertUpdateOrDelete(
                "insert into dbo.PivotLeads (Keyword, Url, Name, Abstract, Sponsor, Amount, ApplicantType, CitizenshipResidency, ActivityLocation, Eligibility, Categories, SourceWebsite, SourceText) values (N'" + self.keyword + "', N'" + self.url + "', N'" + self.name + "', N'" + self.abstract + "', N'" + self.sponsor + "', N'" + self.amount + "', N'" + self.applicantType + "', N'" + self.citizenshipResidency + "', N'" + self.activityLocation + "', N'" + self.eligibility + "', N'" + self.categories + "', N'" + self.sourceWebsite + "', N'" + self.sourceText + "')")

    def checkIfAlreadyInDatabase(self):
        matchingRow = self.db.getRows(
            "select * from dbo.PivotLeads where Keyword='" + self.keyword + "' and Url='" + self.url + "'")
        if matchingRow != []:
            return True
        else:
            return False
