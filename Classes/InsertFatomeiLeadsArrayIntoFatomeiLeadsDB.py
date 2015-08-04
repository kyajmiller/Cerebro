from Classes.SUDBConnect import SUDBConnect


class InsertFatomeiLeadsArrayIntoFatomeiLeadsDB(object):
    def __init__(self, fatomeiLeadArray):
        self.fatomeiLeadArray = fatomeiLeadArray
        self.db = SUDBConnect()

        self.name = fatomeiLeadArray[0]
        self.description = fatomeiLeadArray[1]
        self.dueDate = fatomeiLeadArray[2]
        self.sourceWebsite = fatomeiLeadArray[3]
        self.sourceText = fatomeiLeadArray[4]

        if not self.checkIfAlreadyInDB():
            self.db.insertUpdateOrDelete(
                "insert into dbo.FatomeiLeads (Name, Description, DueDate, SourceWebsite, SourceText) values (N'" + self.name + "'), N'" + self.description + "', N'" + self.dueDate + "', N'" + self.sourceWebsite + "', N'" + self.sourceText + "'")

    def checkIfAlreadyInDB(self):
        matchingRow = self.db.getRows(
            "select * from dbo.FatomeiLeads where Name='" + self.name + "' and SourceWebsite='" + self.sourceWebsite + "'")
        if matchingRow != []:
            return True
        else:
            return False
