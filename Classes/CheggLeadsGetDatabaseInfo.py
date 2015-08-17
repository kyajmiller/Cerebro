from Classes.SUDBConnect import SUDBConnect


class CheggLeadsGetDatabaseInfo(object):
    def __init__(self, tag=None):
        self.tag = tag
        self.db = SUDBConnect()

    def getCheggLeadsIds(self):
        cheggLeadsIds = []

        if self.tag:
            rows = self.db.getRows("select * from dbo.CheggLeads where Tag='" + self.tag + "'")
            for row in rows:
                cheggLeadsIds.append(row.CheggLeadId)
        else:
            rows = self.db.getRows("select * from dbo.CheggLeads")
            for row in rows:
                cheggLeadsIds.append(row.CheggLeadId)

        cheggLeadsIds = [str(cheggLeadsId) for cheggLeadsId in cheggLeadsIds]
        return cheggLeadsIds

    def getTitles(self):
        titles = []

        if self.tag:
            rows = self.db.getRows("select * from dbo.CheggLeads where Tag='" + self.tag + "'")
            for row in rows:
                titles.append(row.Name)
        else:
            rows = self.db.getRows("select * from dbo.CheggLeads")
            for row in rows:
                titles.append(row.Name)
        return titles

    def getEligibilities(self):
        eligibilities = []

        if self.tag:
            rows = self.db.getRows("select * from dbo.CheggLeads where Tag='" + self.tag + "'")
            for row in rows:
                eligibilities.append(row.Eligibility)
        else:
            rows = self.db.getRows("select * from dbo.CheggLeads")
            for row in rows:
                eligibilities.append(row.Eligibility)
        return eligibilities

    def getApplicationOverviews(self):
        applicationOverviews = []

        if self.tag:
            rows = self.db.getRows("select * from dbo.CheggLeads where Tag='" + self.tag + "'")
            for row in rows:
                applicationOverviews.append(row.ApplicationOverview)
        else:
            rows = self.db.getRows("select * from dbo.CheggLeads")
            for row in rows:
                applicationOverviews.append(row.ApplicationOverview)
        return applicationOverviews

    def getDescriptions(self):
        descriptions = []

        if self.tag:
            rows = self.db.getRows("select * from dbo.CheggLeads where Tag='" + self.tag + "'")
            for row in rows:
                descriptions.append(row.Description)
        else:
            rows = self.db.getRows("select * from dbo.CheggLeads")
            for row in rows:
                descriptions.append(row.Description)
        return descriptions

    def getTitleConcatenatedEligibilityAppplictionOverviewList(self):
        wholeList = []

        titles = self.getTitles()
        concatenatedEligibilityApplicationOvewviewDescriptionsList = self.getConcatenatedEligibilityApplicationOverview()

        for i in range(len(titles)):
            title = titles[i]
            concatenatedItem = concatenatedEligibilityApplicationOvewviewDescriptionsList[i]

            listOfItems = [title, concatenatedItem]
            wholeList.append(listOfItems)
        return wholeList

    def getConcatenatedEligibilityApplicationOverview(self):
        listConcatenatedItems = []

        eligibilities = self.getEligibilities()
        applicationOverviews = self.getApplicationOverviews()

        for i in range(len(eligibilities)):
            eligibility = eligibilities[i]
            applicationOverview = applicationOverviews[i]

            concatenatedItem = '%s %s' % (eligibility, applicationOverview)
            listConcatenatedItems.append(concatenatedItem)
        return listConcatenatedItems
