from Classes.PullPageLinkTitleDescriptionToArray import PullPageLinkTitleDescriptionToArray
from Classes.SUDBConnect import SUDBConnect


class InsertScholarshipArrayIntoDatabase(object):
    def __init__(self, scholarshipArray):
        self.scholarshipArray = scholarshipArray
        self.url = self.scholarshipArray[0]
        self.title = self.scholarshipArray[1]
        self.description = self.scholarshipArray[2]
        self.db = SUDBConnect()

    def insertScholarshipArrayIntoDatabase(self):
        self.db.insertUpdateOrDelete(
            "INSERT INTO dbo.LinkCrawlerHrefs ( QuestionId, LinkUrl, LinkName, LinkDescription, LinkBody, ProcessUsed, IsBadLink, InsertDate, UpdateDate) VALUES  ( 0, '" + self.url + "', '" + self.title + "', '" + self.description + "', '', 0, NULL, GETDATE(), GETDATE())")
        return None
