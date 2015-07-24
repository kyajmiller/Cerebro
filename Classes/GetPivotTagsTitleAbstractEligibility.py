from Classes.SUDBConnect import SUDBConnect
from Classes.CleanText import CleanText


class GetPivotTagsTitleAbstractEligibility(object):
    @staticmethod
    def getTitles():
        db = SUDBConnect()
        titles = []

        rows = db.getRows("select Name from dbo.PivotTags")
        for row in rows:
            titles.append(row.Name)
        return titles

    @staticmethod
    def getAbstracts():
        db = SUDBConnect()
        abstracts = []

        rows = db.getRows("select Abstract from dbo.PivotTags")
        for row in rows:
            abstracts.append(row.Abstract)
        return abstracts

    @staticmethod
    def getEligibilities():
        db = SUDBConnect()
        eligibilities = []

        rows = db.getRows("select Eligibility from dbo.PivotTags")
        for row in rows:
            eligibilities.append(row.Eligibility)
        return eligibilities

    @staticmethod
    def getTags():
        db = SUDBConnect()
        tags = []

        rows = db.getRows("select Tag from dbo.PivotTags")
        for row in rows:
            tags.append(row.Tag)
        return tags


    @staticmethod
    def getListConcatenatedItems():
        titles = GetPivotTagsTitleAbstractEligibility.getTitles()
        abstracts = GetPivotTagsTitleAbstractEligibility.getAbstracts()
        eligibilities = GetPivotTagsTitleAbstractEligibility.getEligibilities()
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
    def getListofListofItems():
        titles = GetPivotTagsTitleAbstractEligibility.getTitles()
        abstracts = GetPivotTagsTitleAbstractEligibility.getAbstracts()
        eligibilities = GetPivotTagsTitleAbstractEligibility.getEligibilities()
        wholeList = []

        for i in range(len(abstracts)):
            abstract = CleanText.cleanALLtheText(abstracts[i])
            eligibility = CleanText.cleanALLtheText(eligibilities[i])
            title = CleanText.cleanALLtheText(titles[i])

            listOfItems = [title, abstract, eligibility]
            wholeList.append(listOfItems)

        return wholeList
