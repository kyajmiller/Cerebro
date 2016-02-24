from Classes.SUDBConnect import SUDBConnect
import time
import re


class InsertGrantForwardLeadsArrayIntoGrantForwardItems(object):
    def __init__(self, grantForwardLeadArray, fundingClassification, badScholarshipClassification):
        self.grantForwardLeadArray = grantForwardLeadArray
        self.fundingClassification = fundingClassification
        self.badScholarshipClassification = badScholarshipClassification
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
        self.sourceWebsite = self.grantForwardLeadArray[9]
        self.sourceText = self.grantForwardLeadArray[10]
        self.deadline = ''
        self.date = time.strftime('%Y%m%d')

    def checkIfAlreadyInDatabase(self):
        matchingRow = self.db.getRowsDB(
                "select * from dbo.GrantForwardItems where Name='" + self.name + "' and Url='" + self.url + "'")
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

    def insertUpdateLead(self):
        if not self.checkIfAlreadyInDatabase():
            self.db.insertUpdateOrDeleteDB(
                "INSERT INTO dbo.GrantForwardLeads (Name, Url, Keyword, Description, Sponsor, Amount, Eligibility, SubmissionInfo, Categories, SourceWebsite, SourceText, Deadline, FundingClassification, BadScholarship, Date) VALUES (N'" + self.name + "', N'" + self.url + "', N'" + self.keyword + "', N'" + self.description + "', N'" + self.sponsor + "', N'" + self.amount + "', N'" + self.eligibility + "', N'" + self.submissionInfo + "', N'" + self.categories + "', N'" + self.sourceWebsite + "', N'" + self.sourceText + "', N'" + self.deadline + "', N'" + self.fundingClassification + "', N'" + self.badScholarshipClassification + "', '" + self.date + "')")
            self.writeFileToDisk()
            return True
        else:
            self.db.insertUpdateOrDeleteDB(
                    "update dbo.GrantForwardLeads set Name=N'" + self.name + "', Description=N'" + self.description + "', Sponsor=N'" + self.sponsor + "', Amount=N'" + self.amount + "', Eligibility=N'" + self.eligibility + "', SubmissionInfo=N'" + self.submissionInfo + "', Categories=N'" + self.categories + "', SourceWebsite='" + self.sourceWebsite + "', SourceText=N'" + self.sourceText + "', Deadline=N'" + self.deadline + "', FundingClassification='" + self.fundingClassification + "', BadScholarship='" + self.badScholarshipClassification + "', Date='" + self.date + "' where Keyword='" + self.keyword + "' and Url='" + self.url + "'")
            self.writeFileToDisk()
            return False
