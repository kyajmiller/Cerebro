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

    def writeFileToDisk(self):
        tableName = 'FatomeiLeads'
        user = 'Kya'
        website = re.sub('Leads', '', tableName)
        columns = self.db.getColumnNamesFromTable(tableName)
        try:
            currentRow = self.db.getRowsDB(
                "select * from dbo.FatomeiLeads where Name='" + self.name + "' and SourceWebsite='" + self.sourceWebsite + "'")[
                0]
            self.fileSystemDB.writeFile(columns, currentRow, user, website, self.sourceWebsite, self.date)
        except IndexError:
            pass

    def checkIfAlreadyInDB(self):
        matchingRow = self.db.getRowsDB(
                "SELECT * FROM dbo.FatomeiLeads WHERE Name='" + self.name + "' AND SourceWebsite='" + self.sourceWebsite + "'")
        if matchingRow != []:
            return True
        else:
            return False

    def insertUpdateLead(self):
        if not self.checkIfAlreadyInDB():
            self.db.insertUpdateOrDeleteDB(
                "INSERT INTO dbo.FatomeiLeads (Name, Description, DueDate, SourceWebsite, SourceText, Tag, BadScholarship, Date) VALUES (N'" + self.name + "', N'" + self.description + "', N'" + self.dueDate + "', N'" + self.sourceWebsite + "', N'" + self.sourceText + "', N'" + self.fundingClassification + "', N'" + self.badScholarshipClassification + "', '" + self.date + "')")
            self.writeFileToDisk()
            return True
        else:
            self.db.insertUpdateOrDeleteDB(
                "UPDATE dbo.FatomeiLeads SET Description='" + self.description + "', DueDate='" + self.dueDate + "', SourceText='" + self.sourceText + "', Tag='" + self.fundingClassification + "', BadScholarship='" + self.badScholarshipClassification + "', Date='" + self.date + "' WHERE Name='" + self.name + "' AND SourceWebsite='" + self.sourceWebsite + "'")
            self.writeFileToDisk()
            return False
