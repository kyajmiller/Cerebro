from Classes.SUDBConnect import SUDBConnect


class FastWebLeadsGetDatabaseInfo(object):
    def __init__(self, tag=None):
        self.tag = tag
        self.db = SUDBConnect()

    def getTitles(self):
        titles = []

        if self.tag:
            rows = self.db.getRows("select * from dbo.FastWebLeads where Tag='" + self.tag + "'")
            for row in rows:
                titles.append(row.Name)
        else:
            rows = self.db.getRows("select * from dbo.FastWebLeads")
            for row in rows:
                titles.append(row.Name)

        return titles

    def getDescriptions(self):
        descriptions = []

        if self.tag:
            rows = self.db.getRows("select * from dbo.FastWebLeads where Tag='" + self.tag + "'")
            for row in rows:
                descriptions.append(row.Description)
        else:
            rows = self.db.getRows("select * from dbo.FastWebLeads")
            for row in rows:
                descriptions.append(row.Description)

        return descriptions

    def getSourceTexts(self):
        sourceTexts = []

        if self.tag:
            rows = self.db.getRows("select * from dbo.FastWebLeads where Tag='" + self.tag + "'")
            for row in rows:
                sourceTexts.append(row.SourceText)
        else:
            rows = self.db.getRows("select * from dbo.FastWebLeads")
            for row in rows:
                sourceTexts.append(row.SourceText)

        return sourceTexts

    def getFastWebLeadsIds(self):
        fastWebLeadsIds = []

        if self.tag:
            rows = self.db.getRows("select * from dbo.FastWebLeads where Tag='" + self.tag + "'")
            for row in rows:
                fastWebLeadsIds.append(row.FastWebLeadId)
        else:
            rows = self.db.getRows("select * from dbo.FastWebLeads")
            for row in rows:
                fastWebLeadsIds.append(row.FastWebLeadId)

        return fastWebLeadsIds

    def getSponsors(self):
        sponsors = []

        if self.tag:
            rows = self.db.getRows("select * from dbo.FastWebLeads where Tag='" + self.tag + "'")
            for row in rows:
                sponsors.append(row.Sponsor)
        else:
            rows = self.db.getRows("select * from dbo.FastWebLeads")
            for row in rows:
                sponsors.append(row.Sponsor)

        return sponsors

    def getConcatenatedDescriptionSourceText(self):
        concatenatedItems = []

        descriptions = self.getDescriptions()
        sourceTexts = self.getSourceTexts()

        for i in range(len(descriptions)):
            description = descriptions[i]
            sourceText = sourceTexts[i]
            concatenatedItem = '%s %s' % (description, sourceText)
            concatenatedItems.append(concatenatedItem)

        return concatenatedItems

    def getTitleConcatenatedDescriptionSourceTextList(self):
        wholeList = []

        titles = self.getTitles()
        concatenatedDescriptionSourceTexts = self.getConcatenatedDescriptionSourceText()

        for i in range(len(titles)):
            title = titles[i]
            concatenatedItem = concatenatedDescriptionSourceTexts[i]

            listOfItems = [title, concatenatedItem]
            wholeList.append(listOfItems)

        return wholeList
