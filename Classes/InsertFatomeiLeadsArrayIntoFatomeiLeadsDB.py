from Classes.SUDBConnect import SUDBConnect
import time
import re


class InsertFatomeiLeadsArrayIntoFatomeiLeadsDB(object):
    def __init__(self, fatomeiLeadArray, fundingClassification, badScholarshipClassification):
        self.badScholarshipClassification = badScholarshipClassification
        self.fundingClassification = fundingClassification
        self.fatomeiLeadArray = fatomeiLeadArray
        self.db = SUDBConnect()
        self.fileSystemDB = SUDBConnect(destination='filesystem')

        self.name = fatomeiLeadArray[0]
        self.description = fatomeiLeadArray[1]
        self.dueDate = fatomeiLeadArray[2]
        self.sourceWebsite = fatomeiLeadArray[3]
        self.sourceText = fatomeiLeadArray[4]
        self.date = time.strftime('%Y%m%d')

        if not self.checkIfAlreadyInDB():
            self.db.insertUpdateOrDeleteDB(
                "insert into dbo.FatomeiLeads (Name, Description, DueDate, SourceWebsite, SourceText, Date, Tag, BadScholarship) values (N'" + self.name + "', N'" + self.description + "', N'" + self.dueDate + "', N'" + self.sourceWebsite + "', N'" + self.sourceText + "', '" + self.date + "', '" + self.fundingClassification + "', '" + self.badScholarshipClassification + "')")
        else:
            self.db.insertUpdateOrDeleteDB(
                "update dbo.FatomeiLeads set Description='" + self.description + "', DueDate='" + self.dueDate + "', SourceText='" + self.sourceText + "', Date='" + self.date + "', Tag='" + self.fundingClassification + "', BadScholarship='" + self.badScholarshipClassification + "' where Name='" + self.name + "' and SourceWebsite='" + self.sourceWebsite + "'")
        self.writeFileToDisk()

    def writeFileToDisk(self):
        tableName = 'FatomeiLeads'
        user = 'Kya'
        website = re.sub('Leads', '', tableName)
        columns = self.db.getColumnNamesFromTable(tableName)
        currentRow = self.db.getRowsDB(
            "select * from dbo.FatomeiLeads where Name='" + self.name + "' and SourceWebsite='" + self.sourceWebsite + "'")[
            0]
        self.fileSystemDB.writeFile(columns, currentRow, user, website, self.sourceWebsite, self.date)

    def checkIfAlreadyInDB(self):
        matchingRow = self.db.getRowsDB(
            "select * from dbo.FatomeiLeads where Name='" + self.name + "' and SourceWebsite='" + self.sourceWebsite + "'")
        if matchingRow != []:
            return True
        else:
            return False
