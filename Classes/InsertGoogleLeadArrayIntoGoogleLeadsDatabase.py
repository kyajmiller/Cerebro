from Classes.SUDBConnect import SUDBConnect


class InsertGoogleLeadArrayIntoGoogleLeadsDatabase(object):
    def __init__(self, googleLeadArray):
        self.googleLeadArray = googleLeadArray
        db = SUDBConnect()
        title = self.googleLeadArray[0]
        link = self.googleLeadArray[1]
        description = self.googleLeadArray[2]
        db.insertUpdateOrDeleteDB(
            "INSERT INTO dbo.GoogleLeads (GoogleLeadId, KeyTerm, Title, Link, Description, LinkBody, DateLeadGenerated, DateBodyGenerated) VALUES (0 , '', '" + title + "', '" + link + "', '" + description + "', '', GETDATE(), GETDATE())")
