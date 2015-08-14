from Classes.SUDBConnect import SUDBConnect


class IefaLeadsGetDatabaseInfo(object):
    def __init__(self, tag=None):
        self.tag = tag
        self.db = SUDBConnect()

    def getTitles(self):
        titles = []

        if self.tag:
            rows = self.db.getRows("select Name from dbo.IefaLeads where Tag='" + self.tag + "'")
            for row in rows:
                titles.append(row.Name)
        else:
            rows = self.db.getRows("select Name from dbo.IefaLeads")
            for row in rows:
                titles.append(row.Name)

        return titles

    def getDescriptions(self):
        descriptions = []

        if self.tag:
            rows = self.db.getRows("select Description from dbo.IefaLeads where Tag='" + self.tag + "'")
            for row in rows:
                descriptions.append(row.Description)
        else:
            rows = self.db.getRows("select Description from dbo.IefaLeads")
            for row in rows:
                descriptions.append(row.Description)

        return descriptions

    def getOtherCriterias(self):
        otherCriteria = []

        if self.tag:
            rows = self.db.getRows("select OtherCriteria from dbo.IefaLeads where Tag='" + self.tag + "'")
            for row in rows:
                otherCriteria.append(row.OtherCriteria)
        else:
            rows = self.db.getRows("select OtherCriteria from dbo.IefaLeads")
            for row in rows:
                otherCriteria.append(row.OtherCriteria)

        return otherCriteria

    def getIefaLeadsIds(self):
        iefaLeadsIds = []

        if self.tag:
            rows = self.db.getRows("select IefaLeadId from dbo.IefaLeads where Tag='" + self.tag + "'")
            for row in rows:
                iefaLeadsIds.append(str(row.IefaLeadId))
        else:
            rows = self.db.getRows("select IefaLeadId from dbo.IefaLeads")
            for row in rows:
                iefaLeadsIds.append(str(row.IefaLeadId))

        return iefaLeadsIds

    def getTitleConcatenatedDescriptionOtherCriteriaList(self):
        wholeList = []

        titles = self.getTitles()
        concatenatedDescriptionOtherCriterias = self.getConcatenatedDescriptionOtherCriteria()

        for i in range(len(titles)):
            title = titles[i]
            concatenatedItem = concatenatedDescriptionOtherCriterias[i]

            listOfItems = [title, concatenatedItem]

            wholeList.append(listOfItems)

        return wholeList

    def getConcatenatedDescriptionOtherCriteria(self):
        listConcatenatedItems = []

        descriptions = self.getDescriptions()
        otherCriterias = self.getOtherCriterias()

        for i in range(len(descriptions)):
            description = descriptions[i]
            otherCritieria = otherCriterias[i]

            concatenatedItem = '%s %s' % (description, otherCritieria)
            listConcatenatedItems.append(concatenatedItem)

        return listConcatenatedItems

