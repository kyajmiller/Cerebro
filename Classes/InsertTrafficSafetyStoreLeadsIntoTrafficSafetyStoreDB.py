import time
import re
from Classes.SUDBConnect import SUDBConnect


class InsertTrafficSafetyStoreLeadsIntoTrafficSafetyStoreDB(object):
    def __init__(self, trafficSafetyStoreLeadArray, fundingClassification, badScholarshipClassification):
        self.trafficSafetyStoreLeadArray = trafficSafetyStoreLeadArray
        self.fundingClassification = fundingClassification
        self.badScholarshipClassification = badScholarshipClassification
        self.db = SUDBConnect()
        self.fileSystemDB = SUDBConnect(destination='filesystem')

        self.name = trafficSafetyStoreLeadArray[0]
        self.description = trafficSafetyStoreLeadArray[1]
        self.eligibility = trafficSafetyStoreLeadArray[2]
        self.award = trafficSafetyStoreLeadArray[3]
        self.deadline = trafficSafetyStoreLeadArray[4]
        self.sourceWebsite = trafficSafetyStoreLeadArray[5]
        self.sourceText = trafficSafetyStoreLeadArray[6]
        self.date = time.strftime('%Y%m%d')

    def writeFileToDisk(self):
        tableName = 'TrafficSafetyStoreLeads'
        user = 'Kya'
        website = re.sub('Leads', '', tableName)
        columns = self.db.getColumnNamesFromTable(tableName)
        currentRow = self.db.getRowsDB(
                "select * from dbo.TrafficSafetyStoreLeads where Name='" + self.name + "' and SourceWebsite='" + self.sourceWebsite + "'")[
            0]
        self.fileSystemDB.writeFile(columns, currentRow, user, website, self.sourceWebsite, self.date)

    def checkIfAlreadyInDatabase(self):
        matchingRow = self.db.getRowsDB(
                "select * from dbo.TrafficSafetyStoreLeads where Name='" + self.name + "' and SourceWebsite='" + self.sourceWebsite + "'")
        if matchingRow != []:
            return True
        else:
            return False

    def insertUpdateLead(self):
        if not self.checkIfAlreadyInDatabase():
            self.db.insertUpdateOrDeleteDB(
                    "insert into dbo.TrafficSafetyStoreLeads (Name, Description, Eligibility, Awards, Deadline, SourceWebsite, SourceText, FundingClassification, BadScholarship, Date) values (N'" + self.name + "', N'" + self.description + "', N'" + self.eligibility + "', N'" + self.award + "', N'" + self.deadline + "', N'" + self.sourceWebsite + "', N'" + self.sourceText + "', N'" + self.fundingClassification + "', N'" + self.badScholarshipClassification + "', '" + self.date + "')")
            self.writeFileToDisk()
            return True
        else:
            self.db.insertUpdateOrDeleteDB(
                    "update dbo.TrafficSafetyStoreLeads set Description=N'" + self.description + "', Eligibility=N'" + self.eligibility + "', Awards=N'" + self.award + "', Deadline=N'" + self.deadline + "', SourceText=N'" + self.sourceText + "', FundingClassification='" + self.fundingClassification + "', BadScholarship='" + self.badScholarshipClassification + "', Date='" + self.date + "' where Name='" + self.name + "' and SourceWebsite='" + self.sourceWebsite + "'")
            self.writeFileToDisk()
            return False
