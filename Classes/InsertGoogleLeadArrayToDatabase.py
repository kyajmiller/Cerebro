from Classes.SUDBConnect import SUDBConnect


class InsertGoogleLeadArrayToDatabase(object):
    @staticmethod
    def doInsert(GoogleLeadArray):
        db = SUDBConnect()
        title = GoogleLeadArray[0]
        url = GoogleLeadArray[1]
        description = GoogleLeadArray[2]
        db.insertUpdateOrDelete(
            "INSERT INTO dbo.LinkCrawlerHrefs ( QuestionId, LinkUrl, LinkName, LinkDescription, LinkBody, ProcessUsed, IsBadLink, InsertDate, UpdateDate) VALUES  ( 0, '" + url + "', '" + title + "', '" + description + "', '', 0, 0, GETDATE(), GETDATE())")
        return None
