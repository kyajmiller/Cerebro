from Classes.SUDBConnect import SUDBConnect


class Scholarship360LeadsGetDatabaseInfo(object):
    def __init__(self, tag=None):
        self.db = SUDBConnect()
        self.tag = tag

    def getScholarships360LeadsIds(self):
        scholarships360LeadsIds = []

        if self.tag:
            rows = self.db.getRows("select * from dbo.Scholarships360Leads where Tag='" + self.tag + "'")
            for row in rows:
                scholarships360LeadsIds.append(row.Scholarships360LeadId)
        else:
            rows = self.db.getRows("select * from dbo.Scholarships360Leads")
            for row in rows:
                scholarships360LeadsIds.append(row.Scholarships360LeadId)

        return scholarships360LeadsIds

    def getDescriptions(self):
        descriptions = []

        if self.tag:
            rows = self.db.getRows("select * from dbo.Scholarships360Leads where Tag='" + self.tag + "'")
            for row in rows:
                descriptions.append(row.Description)
        else:
            rows = self.db.getRows("select * from dbo.Scholarships360Leads")
            for row in rows:
                descriptions.append(row.Description)

        return descriptions

    def getTitles(self):
        titles = []

        if self.tag:
            rows = self.db.getRows("select * from dbo.Scholarships360Leads where Tag='" + self.tag + "'")
            for row in rows:
                titles.append(row.Name)
        else:
            rows = self.db.getRows("select * from dbo.Scholarships360Leads")
            for row in rows:
                titles.append(row.Name)

        return titles

    def getTitleDescriptionList(self):
        wholeList = []

        titlesList = self.getTitles()
        descriptionsList = self.getDescriptions()

        for i in range(len(titlesList)):
            title = titlesList[i]
            description = descriptionsList[i]

            listOfItems = [title, description]
            wholeList.append(listOfItems)

        return wholeList
