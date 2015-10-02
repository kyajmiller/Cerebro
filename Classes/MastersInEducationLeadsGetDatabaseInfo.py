from Classes.SUDBConnect import SUDBConnect


class MastersInEducationLeadsGetDatabaseInfo(object):
    def __init__(self, tag=None):
        self.tag = tag
        self.db = SUDBConnect()

    def getTitles(self):
        titles = []

        if self.tag:
            rows = self.db.getRows("select * from dbo.MastersInEducationLeads where Tag='" + self.tag + "'")
            for row in rows:
                titles.append(row.Name)
        else:
            rows = self.db.getRows("select * from dbo.MastersInEducationLeads")
            for row in rows:
                titles.append(row.Name)

        return titles

    def getDescriptions(self):
        descriptions = []

        if self.tag:
            rows = self.db.getRows("select * from dbo.MastersInEducationLeads where Tag='" + self.tag + "'")
            for row in rows:
                descriptions.append(row.Description)
        else:
            rows = self.db.getRows("select * from dbo.MastersInEducationLeads")
            for row in rows:
                descriptions.append(row.Description)

        return descriptions

    def getMastersInEducationLeadIds(self):
        mastersInEducationLeadIds = []

        if self.tag:
            rows = self.db.getRows("select * from dbo.MastersInEducationLeads where Tag='" + self.tag + "'")
            for row in rows:
                mastersInEducationLeadIds.append(row.MastersInEducationLeadId)
        else:
            rows = self.db.getRows("select * from dbo.MastersInEducationLeads")
            for row in rows:
                mastersInEducationLeadIds.append(row.MastersInEducationLeadId)

        return mastersInEducationLeadIds

    def getTitleDescriptionList(self):
        titlesList = self.getTitles()
        descriptionsList = self.getDescriptions()

        titleDescriptionsList = [[titlesList[i], descriptionsList[i]] for i in range(len(titlesList))]
        return titleDescriptionsList
