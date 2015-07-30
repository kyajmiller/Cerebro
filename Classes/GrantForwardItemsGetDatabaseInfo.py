from Classes.SUDBConnect import SUDBConnect
from Classes.CleanText import CleanText


class GrantForwardItemsGetDatabaseInfo(object):
    def __init__(self, keyword, tag=None):
        self.tag = tag
        self.keyword = keyword
        self.db = SUDBConnect()

    def getTitles(self):
        titles = []

        if self.tag:
            rows = self.db.getRows(
                "select Name from dbo.GrantForwardItems where Keyword='" + self.keyword + "' and Tag='" + self.tag + "'")
            for row in rows:
                titles.append(row.Name)
        else:
            rows = self.db.getRows("select Name from dbo.GrantForwardItems where Keyword='" + self.keyword + "'")
            for row in rows:
                titles.append(row.Name)

        return titles

    def getDescriptions(self):
        descriptions = []

        if self.tag:
            rows = self.db.getRows(
                "select Description from dbo.GrantForwardItems where Keyword='" + self.keyword + "' and Tag='" + self.tag + "'")
            for row in rows:
                descriptions.append(row.Description)
        else:
            rows = self.db.getRows("select Description from dbo.GrantForwardItems where Keyword='" + self.keyword + "'")
            for row in rows:
                descriptions.append(row.Description)

        return descriptions

    def getEligibilities(self):
        eligibilities = []

        if self.tag:
            rows = self.db.getRows(
                "select Eligibility from dbo.GrantForwardItems where Keyword='" + self.keyword + "' and Tag='" + self.tag + "'")
            for row in rows:
                eligibilities.append(row.Eligibility)
        else:
            rows = self.db.getRows("select Eligibility from dbo.GrantForwardItems where Keyword='" + self.keyword + "'")
            for row in rows:
                eligibilities.append(row.Eligibility)

        return eligibilities

    def getGrantForwardItemIds(self):
        grantForwardItemIds = []

        if self.tag:
            rows = self.db.getRows(
                "select GrantForwardItemId from dbo.GrantForwardItems where Keyword='" + self.keyword + "' and Tag='" + self.tag + "'")
            for row in rows:
                grantForwardItemIds.append(row.GrantForwardItemId)
        else:
            rows = self.db.getRows(
                "select GrantForwardItemId from dbo.GrantForwardItems where Keyword='" + self.keyword + "'")
            for row in rows:
                grantForwardItemIds.append(row.GrantForwardItemId)

        return grantForwardItemIds
