from Classes.SUDBConnect import SUDBConnect
import re
import time


class InsertMastersInEducationArrayIntoDB(object):
    def __init__(self, mastersInEducationLeadArray, fundingClassification, badScholarshipClassification):
        self.mastersInEducationLeadArray = mastersInEducationLeadArray
        self.fundingClassification = fundingClassification
        self.badScholarshipClassificaion = badScholarshipClassification
        self.db = SUDBConnect()
        self.fileSystemDB = SUDBConnect(destination='filesystem')

        self.name = mastersInEducationLeadArray[0]
        self.amount = mastersInEducationLeadArray[1]
        self.deadline = mastersInEducationLeadArray[2]
        self.description = mastersInEducationLeadArray[3]
        self.sourceWebsite = mastersInEducationLeadArray[4]
        self.sourceText = mastersInEducationLeadArray[5]
        self.date = time.strftime('%Y%m%d')

    def checkIfAlreadyInDatabase(self):
        matchingRow = self.db.getRowsDB(
                "select * from dbo.MastersInEducationLeads where Name='" + self.name + "' and SourceWebsite='" + self.sourceWebsite + "'")
        if matchingRow != []:
            return True
        else:
            return False

    def writeFileToDisk(self):
        tableName = 'MastersInEducationLeads'
        user = 'Kya'
        website = re.sub('Leads', '', tableName)
        columns = self.db.getColumnNamesFromTable(tableName)
        currentRow = self.db.getRowsDB(
                "select * from dbo.MastersInEducationLeads where Name='" + self.name + "' and SourceWebsite='" + self.sourceWebsite + "'")[
            0]
        self.fileSystemDB.writeFile(columns, currentRow, user, website, self.sourceWebsite, self.date)

    def insertUpdateLead(self):
        if not self.checkIfAlreadyInDatabase():
            self.db.insertUpdateOrDeleteDB(
                    "INSERT INTO dbo.MastersInEducationLeads (Name, Deadline, Amount, Description, SourceWebsite, SourceText, Tag, BadScholarship, Date) VALUES (N'" + self.name + "', N'" + self.deadline + "', N'" + self.amount + "', N'" + self.description + "', N'" + self.sourceWebsite + "', N'" + self.sourceText + "', '" + self.fundingClassification + "', '" + self.badScholarshipClassificaion + "', '" + self.date + "')")
            self.writeFileToDisk()
            return True
        else:
            self.db.insertUpdateOrDeleteDB(
                    "update dbo.MastersInEducationLeads set Deadline='" + self.deadline + "', Amount='" + self.amount + "', Description='" + self.description + "', SourceText='" + self.sourceText + "', Tag='" + self.fundingClassification + "', BadScholarship='" + self.badScholarshipClassificaion + "', Date='" + self.date + "' where Name='" + self.name + "' and SourceWebsite='" + self.sourceWebsite + "'")
            self.writeFileToDisk()
            return False
