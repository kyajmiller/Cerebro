from Classes.SUDBConnect import SUDBConnect
import time
import re


class InsertGrantForwardLeadsArrayIntoGrantForwardItems(object):
    def __init__(self, grantForwardLeadArray, fundingClassification, badScholarshipClassification):
        self.grantForwardLeadArray = grantForwardLeadArray
        self.fundingClassification = fundingClassification
        self.badScholarshipClassificaion = badScholarshipClassification
        self.db = SUDBConnect()
        self.fileSystemDB = SUDBConnect(destination='filesystem')

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
        self.date = time.strftime('%Y%m%d')

        if not self.checkIfAlreadyInDatabase():
            self.db.insertUpdateOrDeleteDB(
                "insert into dbo.GrantForwardItems (Keyword, Url, Name, Description, Sponsor, Amount, Eligibility, SubmissionInfo, Categories, OpportunitySourceLink, OpportunitySourceText) values (N'" + self.keyword + "', N'" + self.url + "', N'" + self.name + "', N'" + self.description + "', N'" + self.sponsor + "', N'" + self.amount + "', N'" + self.eligibility + "', N'" + self.submissionInfo + "', N'" + self.categories + "', N'" + self.opportunitySourceLink + "', N'" + self.opportunitySourceText + "')")

    def checkIfAlreadyInDatabase(self):
        matchingRow = self.db.getRowsDB(
                "select * from dbo.GrantForwardItems where Keyword='" + self.keyword + "' and Url='" + self.url + "'")
        if matchingRow != []:
            return True
        else:
            return False

    def writeFileToDisk(self):
        tableName = 'GrantForwardLeads'
        user = 'Kya'
        website = re.sub('Leads', '', tableName)
        columns = self.db.getColumnNamesFromTable(tableName)
        currentRow = self.db.getRowsDB(
                "select * from dbo.GrantForwardLeads where Name='" + self.name + "' and Url='" + self.url + "'")[0]
        self.fileSystemDB.writeFile(columns, currentRow, user, website, self.url, self.date)
