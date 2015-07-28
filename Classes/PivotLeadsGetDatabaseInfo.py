from Classes.SUDBConnect import SUDBConnect
from Classes.CleanText import CleanText


class PivotLeadsGetDatabaseInfo(object):
    def __init__(self, keyword, tag=None):
        self.tag = tag
        self.keyword = keyword
        self.db = SUDBConnect()

    def getTitles(self):
        titles = []

        if self.tag:
            rows = self.db.getRows(
                "select Name from dbo.PivotLeads where Keyword='" + self.keyword + "' and Tag='" + self.tag + "'")
            for row in rows:
                titles.append(row.Name)
        else:
            rows = self.db.getRows("select Name from dbo.PivotLeads where Keyword='" + self.keyword + "'")
            for row in rows:
                titles.append(row.Name)
        return titles

    def getAbstracts(self):
        abstracts = []

        if self.tag:
            rows = self.db.getRows(
                "select Abstract from dbo.PivotLeads where Keyword='" + self.keyword + "' and Tag='" + self.tag + "'")
            for row in rows:
                abstracts.append(row.Abstract)
        else:
            rows = self.db.getRows("select Abstract from dbo.PivotLeads where Keyword='" + self.keyword + "'")
            for row in rows:
                abstracts.append(row.Abstract)
        return abstracts

    def getEligibilities(self):
        eligibilities = []

        if self.tag:
            rows = self.db.getRows(
                "select Eligibility from dbo.PivotLeads where Keyword='" + self.keyword + "' and Tag='" + self.tag + "'")
            for row in rows:
                eligibilities.append(row.Eligibility)
        else:
            rows = self.db.getRows("select Eligibility from dbo.PivotLeads where Keyword='" + self.keyword + "'")
            for row in rows:
                eligibilities.append(row.Eligibility)
        return eligibilities

    def getTags(self):
        tags = []

        rows = self.db.getRows("select Tag from dbo.PivotLeads where Keyword='" + self.keyword + "'")
        for row in rows:
            tags.append(row.Tag)
        return tags

    def getPivotLeadId(self):
        pivotLeadIds = []

        if self.tag:
            rows = self.db.getRows(
                "select PivotLeadId from dbo.PivotLeads where Keyword='" + self.keyword + "' and Tag='" + self.tag + "'")
            for row in rows:
                pivotLeadIds.append(row.PivotLeadId)
        else:
            rows = self.db.getRows("select PivotLeadId from dbo.PivotLeads where Keyword='" + self.keyword + "'")
            for row in rows:
                pivotLeadIds.append(row.PivotLeadId)
        return pivotLeadIds

    def getSourceText(self):
        sourceTexts = []

        if self.tag:
            rows = self.db.getRows(
                "select SourceText from dbo.PivotLeads where Keyword='" + self.keyword + "' and Tag='" + self.tag + "'")
            for row in rows:
                sourceTexts.append(row.SourceText)
        else:
            rows = self.db.getRows("select SourceText from dbo.PivotLeads where Keyword='" + self.keyword + "'")
            for row in rows:
                sourceTexts.append(row.SourceText)
        return sourceTexts

    def getListStringConcatenatedTitleAbstractEligibility(self):
        comboTitleAbstractsEligibilitiesList = []

        titles = self.getTitles()
        abstracts = self.getAbstracts()
        eligibilities = self.getEligibilities()

        for i in range(len(abstracts)):
            abstract = abstracts[i]
            eligibility = eligibilities[i]
            title = titles[i]

            comboTitleAbstractEligibility = '%s %s %s' % (title, abstract, eligibility)
            comboTitleAbstractEligibility = CleanText.cleanALLtheText(comboTitleAbstractEligibility)
            comboTitleAbstractsEligibilitiesList.append(comboTitleAbstractEligibility)

        return comboTitleAbstractsEligibilitiesList

    def getListStringConcatendatedAbstractEligibility(self):
        comboAbstractsEligibilitiesList = []

        abstracts = self.getTitles()
        eligibilities = self.getEligibilities()

        for i in range(len(abstracts)):
            abstract = abstracts[i]
            eligibility = eligibilities[i]

            comboAbstractEligibility = '%s %s' % (abstract, eligibility)
            comboAbstractEligibility = CleanText.cleanALLtheText(comboAbstractEligibility)
            comboAbstractsEligibilitiesList.append(comboAbstractEligibility)

        return comboAbstractsEligibilitiesList

    def getTitleAbstractEligibilityPivotLeadIdList(self):
        wholeList = []

        titles = self.getTitles()
        abstracts = self.getAbstracts()
        eligibilities = self.getEligibilities()
        pivotLeadIds = self.getPivotLeadId()

        for i in range(len(abstracts)):
            abstract = CleanText.cleanALLtheText(abstracts[i])
            eligibility = CleanText.cleanALLtheText(eligibilities[i])
            title = CleanText.cleanALLtheText(titles[i])
            pivotLeadId = str(pivotLeadIds[i])

            listOfItems = [title, abstract, eligibility, pivotLeadId]
            wholeList.append(listOfItems)

        return wholeList

    @staticmethod
    def getKeywords():
        db = SUDBConnect()
        keywords = []
        rows = db.getRows("select distinct Keyword from dbo.PivotLeads")
        for row in rows:
            keywords.append(row.Keyword)

        return keywords