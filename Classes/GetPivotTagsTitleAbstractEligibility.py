from Classes.SUDBConnect import SUDBConnect
from Classes.CleanText import CleanText


class GetPivotTagsTitleAbstractEligibility(object):
    @staticmethod
    def getListConcatenatedItems():
        db = SUDBConnect()
        titles = []
        abstracts = []
        eligibilities = []
        comboAbstractsEligibilities = []

        rows = db.getRows("select * from dbo.PivotTags")
        for row in rows:
            abstracts.append(row.Abstract)
            eligibilities.append(row.Eligibility)
            titles.append(row.Name)

        for i in range(len(abstracts)):
            abstract = abstracts[i]
            eligibility = eligibilities[i]
            title = titles[i]

            comboAbstractEligibility = '%s %s %s' % (title, abstract, eligibility)
            comboAbstractEligibility = CleanText.cleanALLtheText(comboAbstractEligibility)
            comboAbstractsEligibilities.append(comboAbstractEligibility)

        return comboAbstractsEligibilities
