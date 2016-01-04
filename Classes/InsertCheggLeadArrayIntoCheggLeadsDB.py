from Classes.SUDBConnect import SUDBConnect
import time

class InsertCheggLeadArrayIntoCheggLeadsDB(object):
    def __init__(self, cheggLeadArray, fundingClassification):
        self.cheggLeadArray = cheggLeadArray
        self.fundingClassification = fundingClassification
        self.db = SUDBConnect()

        self.name = self.cheggLeadArray[0]
        self.url = self.cheggLeadArray[1]
        self.deadline = self.cheggLeadArray[2]
        self.amount = self.cheggLeadArray[3]
        self.eligibility = self.cheggLeadArray[4]
        self.applicationOverview = self.cheggLeadArray[5]
        self.description = self.cheggLeadArray[6]
        self.sponsor = self.cheggLeadArray[7]
        self.sourceWebsite = self.cheggLeadArray[8]
        self.sourceText = self.cheggLeadArray[9]
        self.date = time.strftime('%Y%m%d')

        if not self.checkIfAlreadyInDatabase():
            self.db.insertUpdateOrDeleteDB(
                "insert into dbo.CheggLeads (Name, Url, Deadline, Amount, Eligibility, ApplicationOverview, Description, Sponsor, SourceWebsite, SourceText, Date) values (N'" + self.name + "', N'" + self.url + "', N'" + self.deadline + "', N'" + self.amount + "', N'" + self.eligibility + "', N'" + self.applicationOverview + "', N'" + self.description + "', N'" + self.sponsor + "', N'" + self.sourceWebsite + "', N'" + self.sourceText + "', '" + self.date + "')")
        else:
            self.db.insertUpdateOrDeleteDB(
                "update dbo.CheggLeads set Deadline=N'" + self.deadline + "', Amount=N'" + self.amount + "', Eligibility=N'" + self.eligibility + "', ApplicationOverview=N'" + self.applicationOverview + "', Description=N'" + self.description + "', Sponsor=N'" + self.sponsor + "', SourceWebsite=N'" + self.sourceWebsite + "', SourceText=N'" + self.sourceText + "', Date='" + self.date + "' where Name='" + self.name + "' and Url='" + self.url + "'")

    def checkIfAlreadyInDatabase(self):
        matchingRow = self.db.getRowsDB(
            "select * from dbo.CheggLeads where Name='" + self.name + "' and Url='" + self.url + "'")
        if matchingRow != []:
            return True
        else:
            return False