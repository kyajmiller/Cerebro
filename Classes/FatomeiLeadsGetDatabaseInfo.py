from Classes.SUDBConnect import SUDBConnect
from Classes.CleanText import CleanText


class FatomeiLeadsGetDatabaseInfo(object):
    def __init__(self, tag=None):
        self.tag = tag
        self.db = SUDBConnect()

    def getTitles(self):
        titles = []

        if self.tag:
            rows = self.db.getRows("select Name from dbo.FatomeiLeads where Tag='" + self.tag + "'")
            for row in rows:
                titles.append(row.Name)
        else:
            rows = self.db.getRows("select Name from dbo.FatomeiLeads")
            for row in rows:
                titles.append(row.Name)

        return titles

    def getDescriptions(self):
        descriptions = []

        if self.tag:
            rows = self.db.getRows("select Description from dbo.FatomeiLeads where Tag='" + self.tag + "'")
            for row in rows:
                descriptions.append(row.Description)
        else:
            rows = self.db.getRows("select Description from dbo.FatomeiLeads")
            for row in rows:
                descriptions.append(row.Description)

        return descriptions

    def getSourceText(self):
        sourceTexts = []

        if self.tag:
            rows = self.db.getRows("select SourceText from dbo.FatomeiLeads where Tag='" + self.tag + "'")
            for row in rows:
                sourceTexts.append(row.SourceText)
        else:
            rows = self.db.getRows("select SourceText from dbo.FatomeiLeads")
            for row in rows:
                sourceTexts.append(row.SourceText)

        return sourceTexts

    def getFatomeiLeadIds(self):
        fatomeiLeadIds = []

        if self.tag:
            rows = self.db.getRows("select FatomeiLeadId from dbo.FatomeiLeads where Tag='" + self.tag + "'")
            for row in rows:
                fatomeiLeadIds.append(row.FatomeiLeadId)
        else:
            rows = self.db.getRows("select FatomeiLeadId from dbo.FatomeiLeads")
            for row in rows:
                fatomeiLeadIds.append(row.FatomeiLeadId)

        return fatomeiLeadIds

    def getTitleDescriptionList(self):
        wholeList = []

        titles = self.getTitles()
        descriptions = self.getDescriptions()

        for i in range(len(titles)):
            title = titles[i]
            description = descriptions[i]

            listOfItems = [title, description]
            wholeList.append(listOfItems)
        return wholeList
