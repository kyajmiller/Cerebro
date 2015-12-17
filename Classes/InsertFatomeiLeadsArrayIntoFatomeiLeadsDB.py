from Classes.SUDBConnect import SUDBConnect
import time


class InsertFatomeiLeadsArrayIntoFatomeiLeadsDB(object):
    def __init__(self, fatomeiLeadArray):
        self.fatomeiLeadArray = fatomeiLeadArray
        self.db = SUDBConnect()

        self.name = fatomeiLeadArray[0]
        self.description = fatomeiLeadArray[1]
        self.dueDate = fatomeiLeadArray[2]
        self.sourceWebsite = fatomeiLeadArray[3]
        self.sourceText = fatomeiLeadArray[4]
        self.date = time.strftime('%Y%m%d')

        if not self.checkIfAlreadyInDB():
            self.db.insertUpdateOrDeleteDB(
                "insert into dbo.FatomeiLeads (Name, Description, DueDate, SourceWebsite, SourceText, Date) values (N'" + self.name + "', N'" + self.description + "', N'" + self.dueDate + "', N'" + self.sourceWebsite + "', N'" + self.sourceText + "', '" + self.date + "')")
        else:
            self.db.insertUpdateOrDeleteDB(
                "update dbo.FatomeiLeads set Description='" + self.description + "', DueDate='" + self.dueDate + "', SourceText='" + self.sourceText + "', Date='" + self.date + "' where Name='" + self.name + "' and SourceWebsite='" + self.sourceWebsite + "'")

    def checkIfAlreadyInDB(self):
        matchingRow = self.db.getRowsDB(
            "select * from dbo.FatomeiLeads where Name='" + self.name + "' and SourceWebsite='" + self.sourceWebsite + "'")
        if matchingRow != []:
            return True
        else:
            return False
