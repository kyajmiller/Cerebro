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
