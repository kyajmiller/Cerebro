from Classes.SUDBConnect import SUDBConnect
from Classes.CleanText import CleanText


class PivotLeadsGetDatabaseInfo(object):
    @staticmethod
    def getTitles(keyword, tag=None):
        db = SUDBConnect()
        titles = []

        if tag:
            rows = db.getRows("select Name from dbo.PivotLeads where Keyword='" + keyword + "' and Tag='" + tag + "'")
            for row in rows:
                titles.append(row.Name)
        else:
            rows = db.getRows("select Name from dbo.PivotLeads where Keyword='" + keyword + "'")
            for row in rows:
                titles.append(row.Name)
        return titles

    @staticmethod
    def getAbstracts(keyword, tag=None):
        db = SUDBConnect()
        abstracts = []

        if tag:
            rows = db.getRows(
                "select Abstract from dbo.PivotLeads where Keyword='" + keyword + "' and Tag='" + tag + "'")
            for row in rows:
                abstracts.append(row.Abstract)
        else:
            rows = db.getRows("select Abstract from dbo.PivotLeads where Keyword='" + keyword + "'")
            for row in rows:
                abstracts.append(row.Abstract)
        return abstracts

    @staticmethod
    def getEligibilities(keyword, tag=None):
        db = SUDBConnect()
        eligibilities = []

        if tag:
            rows = db.getRows(
                "select Eligibility from dbo.PivotLeads where Keyword='" + keyword + "' and Tag='" + tag + "'")
            for row in rows:
                eligibilities.append(row.Eligibility)
        else:
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
    def getPivotLeadId(keyword, tag=None):
        db = SUDBConnect()
        keyword = keyword
        pivotLeadIds = []

        if tag:
            rows = db.getRows(
                "select PivotLeadId from dbo.PivotLeads where Keyword='" + keyword + "' and Tag='" + tag + "'")
            for row in rows:
                pivotLeadIds.append(row.PivotLeadId)
        else:
            rows = db.getRows("select PivotLeadId from dbo.PivotLeads where Keyword='" + keyword + "'")
            for row in rows:
                pivotLeadIds.append(row.PivotLeadId)
        return pivotLeadIds

    @staticmethod
    def getListStringConcatenatedTitleAbstractEligibility(keyword, tag=None):
        comboTitleAbstractsEligibilitiesList = []

        if tag:
            titles = PivotLeadsGetDatabaseInfo.getTitles(keyword, tag)
            abstracts = PivotLeadsGetDatabaseInfo.getAbstracts(keyword, tag)
            eligibilities = PivotLeadsGetDatabaseInfo.getEligibilities(keyword, tag)

            for i in range(len(abstracts)):
                abstract = abstracts[i]
                eligibility = eligibilities[i]
                title = titles[i]

                comboTitleAbstractEligibility = '%s %s %s' % (title, abstract, eligibility)
                comboTitleAbstractEligibility = CleanText.cleanALLtheText(comboTitleAbstractEligibility)
                comboTitleAbstractsEligibilitiesList.append(comboTitleAbstractEligibility)
        else:
            titles = PivotLeadsGetDatabaseInfo.getTitles(keyword)
            abstracts = PivotLeadsGetDatabaseInfo.getAbstracts(keyword)
            eligibilities = PivotLeadsGetDatabaseInfo.getEligibilities(keyword)

            for i in range(len(abstracts)):
                abstract = abstracts[i]
                eligibility = eligibilities[i]
                title = titles[i]

                comboTitleAbstractEligibility = '%s %s %s' % (title, abstract, eligibility)
                comboTitleAbstractEligibility = CleanText.cleanALLtheText(comboTitleAbstractEligibility)
                comboTitleAbstractsEligibilitiesList.append(comboTitleAbstractEligibility)

        return comboTitleAbstractsEligibilitiesList

    @staticmethod
    def getTitleAbstractEligibilityPivotLeadIdList(keyword, tag=None):
        wholeList = []

        if tag:
            titles = PivotLeadsGetDatabaseInfo.getTitles(keyword, tag)
            abstracts = PivotLeadsGetDatabaseInfo.getAbstracts(keyword, tag)
            eligibilities = PivotLeadsGetDatabaseInfo.getEligibilities(keyword, tag)
            pivotLeadIds = PivotLeadsGetDatabaseInfo.getPivotLeadId(keyword, tag)

            for i in range(len(abstracts)):
                abstract = CleanText.cleanALLtheText(abstracts[i])
                eligibility = CleanText.cleanALLtheText(eligibilities[i])
                title = CleanText.cleanALLtheText(titles[i])
                pivotLeadId = str(pivotLeadIds[i])

                listOfItems = [title, abstract, eligibility, pivotLeadId]
                wholeList.append(listOfItems)
        else:
            titles = PivotLeadsGetDatabaseInfo.getTitles(keyword)
            abstracts = PivotLeadsGetDatabaseInfo.getAbstracts(keyword)
            eligibilities = PivotLeadsGetDatabaseInfo.getEligibilities(keyword)
            pivotLeadIds = PivotLeadsGetDatabaseInfo.getPivotLeadId(keyword)

            for i in range(len(abstracts)):
                abstract = CleanText.cleanALLtheText(abstracts[i])
                eligibility = CleanText.cleanALLtheText(eligibilities[i])
                title = CleanText.cleanALLtheText(titles[i])
                pivotLeadId = str(pivotLeadIds[i])

                listOfItems = [title, abstract, eligibility, pivotLeadId]
                wholeList.append(listOfItems)

        return wholeList

    @staticmethod
    def getListStringConcatendatedAbstractEligibility(keyword, tag=None):
        comboAbstractsEligibilitiesList = []

        if tag:
            abstracts = PivotLeadsGetDatabaseInfo.getTitles(keyword, tag)
            eligibilities = PivotLeadsGetDatabaseInfo.getEligibilities(keyword, tag)

            for i in range(len(abstracts)):
                abstract = abstracts[i]
                eligibility = eligibilities[i]

                comboAbstractEligibility = '%s %s' % (abstract, eligibility)
                comboAbstractEligibility = CleanText.cleanALLtheText(comboAbstractEligibility)
                comboAbstractsEligibilitiesList.append(comboAbstractEligibility)
        else:
            abstracts = PivotLeadsGetDatabaseInfo.getTitles(keyword)
            eligibilities = PivotLeadsGetDatabaseInfo.getEligibilities(keyword)

            for i in range(len(abstracts)):
                abstract = abstracts[i]
                eligibility = eligibilities[i]

                comboAbstractEligibility = '%s %s' % (abstract, eligibility)
                comboAbstractEligibility = CleanText.cleanALLtheText(comboAbstractEligibility)
                comboAbstractsEligibilitiesList.append(comboAbstractEligibility)

        return comboAbstractsEligibilitiesList
