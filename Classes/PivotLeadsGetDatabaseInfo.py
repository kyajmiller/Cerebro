from Classes.SUDBConnect import SUDBConnect
from Classes.CleanText import CleanText


class PivotLeadsGetDatabaseInfo(object):
    @staticmethod
    def getTitles(keyword):
        keyword = keyword
        db = SUDBConnect()
        titles = []

        rows = db.getRows("select Name from dbo.PivotLeads where Keyword='" + keyword + "'")
        for row in rows:
            titles.append(row.Name)
        return titles

    @staticmethod
    def getAbstracts(keyword):
        db = SUDBConnect()
        abstracts = []

        rows = db.getRows("select Abstract from dbo.PivotLeads where Keyword='" + keyword + "'")
        for row in rows:
            abstracts.append(row.Abstract)
        return abstracts

    @staticmethod
    def getEligibilities(keyword):
        db = SUDBConnect()
        eligibilities = []

        rows = db.getRows("select Eligibility from dbo.PivotLeads where Keyword='" + keyword + "'")
        for row in rows:
            eligibilities.append(row.Eligibility)
        return eligibilities

    @staticmethod
    def getTags(keyword):
        db = SUDBConnect()
        tags = []

        rows = db.getRows("select Tag from dbo.PivotLeads where Keyword='" + keyword + "'")
        for row in rows:
            tags.append(row.Tag)
        return tags

    @staticmethod
    def getKeywords():
        db = SUDBConnect()
        keywords = []
        rows = db.getRows("select distinct Keyword from dbo.PivotLeads")
        for row in rows:
            keywords.append(row.Keyword)

        return keywords

    @staticmethod
    def getPivotLeadId(keyword):
        db = SUDBConnect()
        keyword = keyword
        pivotLeadIds = []
        rows = db.getRows("select PivotLeadId from dbo.PivotLeads where Keyword='" + keyword + "'")
        for row in rows:
            pivotLeadIds.append(row.PivotLeadId)
        return pivotLeadIds

    @staticmethod
    def getListConcatenatedItems(keyword):
        titles = PivotLeadsGetDatabaseInfo.getTitles(keyword)
        abstracts = PivotLeadsGetDatabaseInfo.getAbstracts(keyword)
        eligibilities = PivotLeadsGetDatabaseInfo.getEligibilities(keyword)
        comboAbstractsEligibilities = []

        for i in range(len(abstracts)):
            abstract = abstracts[i]
            eligibility = eligibilities[i]
            title = titles[i]

            comboAbstractEligibility = '%s %s %s' % (title, abstract, eligibility)
            comboAbstractEligibility = CleanText.cleanALLtheText(comboAbstractEligibility)
            comboAbstractsEligibilities.append(comboAbstractEligibility)

        return comboAbstractsEligibilities

    @staticmethod
    def getListofListofItems(keyword):
        titles = PivotLeadsGetDatabaseInfo.getTitles(keyword)
        abstracts = PivotLeadsGetDatabaseInfo.getAbstracts(keyword)
        eligibilities = PivotLeadsGetDatabaseInfo.getEligibilities(keyword)
        pivotLeadIds = PivotLeadsGetDatabaseInfo.getPivotLeadId(keyword)
        wholeList = []

        for i in range(len(abstracts)):
            abstract = CleanText.cleanALLtheText(abstracts[i])
            eligibility = CleanText.cleanALLtheText(eligibilities[i])
            title = CleanText.cleanALLtheText(titles[i])
            pivotLeadId = str(pivotLeadIds[i])

            listOfItems = [title, abstract, eligibility, pivotLeadId]
            wholeList.append(listOfItems)

        return wholeList
