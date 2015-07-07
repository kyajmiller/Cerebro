from Classes.SUDBConnect import SUDBConnect
from Classes.RipPage import RipPage
from Classes.CleanText import CleanText


class PopulateEmptyLinkBodyUsingDatabaseLinkUrl(object):
    def __init__(self):
        self.db = SUDBConnect()
        self.linkUrlsList = []

        rowsWithEmptyLinkBody = self.db.getRows("select * from dbo.LinkCrawlerHrefs where ISNULL(LinkBody, '') = ''")
        if len(rowsWithEmptyLinkBody) >= 1:
            for row in rowsWithEmptyLinkBody:
                self.linkUrlsList.append(row.LinkUrl)

        if len(self.linkUrlsList) >= 1:
            for link in self.linkUrlsList:
                linkbody = RipPage.getPageSource(link)
                cleanLinkBody = CleanText.cleanALLtheText(linkbody)
                self.db.insertUpdateOrDelete(
                    "update dbo.LinkCrawlerHrefs set LinkBody = '" + cleanLinkBody + "' where LinkUrl = '" + link + "'")
