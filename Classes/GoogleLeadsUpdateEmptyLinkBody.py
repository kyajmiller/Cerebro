from Classes.SUDBConnect import SUDBConnect
from Classes.RipPage import RipPage
from Classes.CleanText import CleanText


class GoogleLeadsUpdateEmptyLinkBody(object):
    def __init__(self):
        self.db = SUDBConnect()
        self.listOfEmptyLinkBodyLinks = []

        rowsWithEmptyLinkBody = self.db.getRowsDB("select * from dbo.GoogleLeads where ISNULL(LinkBody, '') = ''")
        if len(rowsWithEmptyLinkBody) >= 1:
            for row in rowsWithEmptyLinkBody:
                self.listOfEmptyLinkBodyLinks.append(row.Link)

        if len(self.listOfEmptyLinkBodyLinks) >= 1:
            for link in self.listOfEmptyLinkBodyLinks:
                linkbody = RipPage.getPageSource(link)
                linkbody = CleanText.cleanALLtheText(linkbody)
                self.db.insertUpdateOrDeleteDB(
                    "update dbo.GoogleLeads set LinkBody='" + linkbody + "', DateBodyGenerated=GETDATE() where Link='" + link + "'")
