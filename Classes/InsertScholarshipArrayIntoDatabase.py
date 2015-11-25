from Classes.PullPageLinkTitleDescriptionToArray import PullPageLinkTitleDescriptionToArray
from Classes.SUDBConnect import SUDBConnect


class InsertScholarshipArrayIntoDatabase(object):
    @staticmethod
    def doInsert(scholarshipArray):
        url = scholarshipArray[0]
        title = scholarshipArray[1]
        description = scholarshipArray[2]
        db = SUDBConnect()
        db.insertUpdateOrDeleteDB(
            "INSERT INTO dbo.LinkCrawlerHrefs ( QuestionId, LinkUrl, LinkName, LinkDescription, LinkBody, ProcessUsed, IsBadLink, InsertDate, UpdateDate) VALUES  ( 0, '" + url + "', '" + title + "', '" + description + "', '', 0, 0, GETDATE(), GETDATE())")
        return None
