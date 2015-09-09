from Classes.SUDBConnect import SUDBConnect
from Classes.CleanText import CleanText


class PivotLeadsGetDatabaseInfo(object):
    def __init__(self, keyword=None, tag=None):
        self.tag = tag
        self.keyword = keyword
        self.db = SUDBConnect()

    def getTitles(self):
        titles = []

        if self.tag and self.keyword:
            rows = self.db.getRows(
                "select Name from dbo.PivotLeads where Keyword='" + self.keyword + "' and Tag='" + self.tag + "'")
            for row in rows:
                titles.append(row.Name)
        elif self.keyword:
            rows = self.db.getRows("select Name from dbo.PivotLeads where Keyword='" + self.keyword + "'")
            for row in rows:
                titles.append(row.Name)
        elif self.tag:
            rows = self.db.getRows("select * from dbo.PivotLeads where Tag='" + self.tag + "'")
            for row in rows:
                titles.append(row.Name)
        else:
            rows = self.db.getRows("select * from dbo.PivotLeads")
            for row in rows:
                titles.append(row.Name)
        return titles

    def getAbstracts(self):
        abstracts = []

        if self.tag and self.keyword:
            rows = self.db.getRows(
                "select Abstract from dbo.PivotLeads where Keyword='" + self.keyword + "' and Tag='" + self.tag + "'")
            for row in rows:
                abstracts.append(row.Abstract)
        elif self.keyword:
            rows = self.db.getRows("select Abstract from dbo.PivotLeads where Keyword='" + self.keyword + "'")
            for row in rows:
                abstracts.append(row.Abstract)
        elif self.tag:
            rows = self.db.getRows("select * from dbo.PivotLeads where Tag='" + self.tag + "'")
            for row in rows:
                abstracts.append(row.Abstract)
        else:
            rows = self.db.getRows("select * from dbo.PivotLeads")
            for row in rows:
                abstracts.append(row.Abstract)
        return abstracts

    def getEligibilities(self):
        eligibilities = []

        if self.tag and self.keyword:
            rows = self.db.getRows(
                "select Eligibility from dbo.PivotLeads where Keyword='" + self.keyword + "' and Tag='" + self.tag + "'")
            for row in rows:
                eligibilities.append(row.Eligibility)
        elif self.keyword:
            rows = self.db.getRows("select Eligibility from dbo.PivotLeads where Keyword='" + self.keyword + "'")
            for row in rows:
                eligibilities.append(row.Eligibility)
        elif self.tag:
            rows = self.db.getRows("select * from dbo.PivotLeads where Tag='" + self.tag + "'")
            for row in rows:
                eligibilities.append(row.Eligibility)
        else:
            rows = self.db.getRows("select * from dbo.PivotLeads")
            for row in rows:
                eligibilities.append(row.Eligibility)
        return eligibilities

    def getPivotLeadId(self):
        pivotLeadIds = []

        if self.tag and self.keyword:
            rows = self.db.getRows(
                "select PivotLeadId from dbo.PivotLeads where Keyword='" + self.keyword + "' and Tag='" + self.tag + "'")
            for row in rows:
                pivotLeadIds.append(str(row.PivotLeadId))
        elif self.keyword:
            rows = self.db.getRows("select PivotLeadId from dbo.PivotLeads where Keyword='" + self.keyword + "'")
            for row in rows:
                pivotLeadIds.append(str(row.PivotLeadId))
        elif self.tag:
            rows = self.db.getRows("select * from dbo.PivotLeads where Tag='" + self.tag + "'")
            for row in rows:
                pivotLeadIds.append(str(row.PivotLeadId))
        else:
            rows = self.db.getRows("select * from dbo.PivotLeads")
            for row in rows:
                pivotLeadIds.append(str(row.PivotLeadId))
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

    def getTitleAbstractList(self):
        wholeList = []

        titles = self.getTitles()
        abstracts = self.getAbstracts()

        for i in range(len(abstracts)):
            abstract = CleanText.cleanALLtheText(abstracts[i])
            title = CleanText.cleanALLtheText(titles[i])

            listOfItems = [title, abstract]
            wholeList.append(listOfItems)

        return wholeList

    @staticmethod
    def getKeywords(tag=None):
        db = SUDBConnect()
        keywords = []
        if tag:
            rows = db.getRows("select distinct Keyword from dbo.PivotLeads where Tag='" + tag + "'")
            for row in rows:
                keywords.append(row.Keyword)
        else:
            rows = db.getRows("select distinct Keyword from dbo.PivotLeads")
            for row in rows:
                keywords.append(row.Keyword)

        return keywords