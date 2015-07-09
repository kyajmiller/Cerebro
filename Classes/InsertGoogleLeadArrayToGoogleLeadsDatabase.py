from Classes.SUDBConnect import SUDBConnect


class InsertGoogleLeadArrayToGoogleLeadsDatabase(object):
    @staticmethod
    def doInsert(GoogleLeadArray):
        db = SUDBConnect()
        title = GoogleLeadArray[0]
        link = GoogleLeadArray[1]
        description = GoogleLeadArray[2]
        db.insertUpdateOrDelete(
            "INSERT INTO dbo.GoogleLeads ( GoogleLeadId, KeyTerm, Title, Link, Description, LinkBody, DateLeadGenerated, DateBodyGenerated) VALUES  ( 0, '', '" + title + "', '" + link + "', '" + description + "', '', GETDATE(), ''")
        return None
