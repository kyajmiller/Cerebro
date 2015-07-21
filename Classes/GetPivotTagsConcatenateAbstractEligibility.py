from Classes.SUDBConnect import SUDBConnect
from Classes.CleanText import CleanText


class GetPivotTagsConcatenateAbstractEligibility(object):
    @staticmethod
    def getList():
        db = SUDBConnect()
        abstracts = []
        eligibilities = []
        comboAbstractsEligibilities = []

        rows = db.getRows("select * from dbo.PivotTags")
        for row in rows:
            abstracts.append(row.Abstract)
            eligibilities.append(row.Eligibility)

        for i in range(len(abstracts)):
            abstract = abstracts[i]
            eligibility = eligibilities[i]

            comboAbstractEligibility = '%s %s' % (abstract, eligibility)
            comboAbstractEligibility = CleanText.cleanALLtheText(comboAbstractEligibility)
            comboAbstractsEligibilities.append(comboAbstractEligibility)

        return comboAbstractsEligibilities
