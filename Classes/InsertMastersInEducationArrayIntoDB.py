from Classes.SUDBConnect import SUDBConnect


class InsertMastersInEducationArrayIntoDB(object):
    def __init__(self, mastersInEducationLeadArray):
        self.mastersInEducationLeadArray = mastersInEducationLeadArray
        self.db = SUDBConnect()

        self.name = mastersInEducationLeadArray[0]
        self.amount = mastersInEducationLeadArray[1]
        self.deadline = mastersInEducationLeadArray[2]
        self.description = mastersInEducationLeadArray[3]
        self.sourceWebsite = mastersInEducationLeadArray[4]
        self.sourceText = mastersInEducationLeadArray[5]

        if not self.checkIfAlreadyInDatabase():
            self.db.insertUpdateOrDelete(
                "INSERT INTO dbo.MastersInEducationLeads (Name, Deadline, Amount, Description, SourceWebsite, SourceText) VALUES (N'" + self.name + "', N'" + self.deadline + "', N'" + self.amount + "', N'" + self.description + "', N'" + self.sourceWebsite + "', N'" + self.sourceText + "')")

    def checkIfAlreadyInDatabase(self):
        matchingRow = self.db.getRows(
            "select * from dbo.MastersInEducationLeads where Name='" + self.name + "' and Description='" + self.description + "'")
        if matchingRow != []:
            return True
        else:
            return False
