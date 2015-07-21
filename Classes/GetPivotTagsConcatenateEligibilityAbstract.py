from Classes.SUDBConnect import SUDBConnect


class GetPivotTagsConcatenateEligibilityAbstract(object):
    def __init__(self):
        self.db = SUDBConnect()
        self.abstracts = []
        self.eligibilities = []
        self.comboAbstractsEligibilities = []

        rows = self.db.getRows("select * from dbo.PivotTags")
        for row in rows:
            self.abstracts.append(row.Abstract)
            self.eligibilities.append(row.Eligibility)

    def conatenateAbstractsEligibilities(self):
        for i in range(len(self.abstracts)):
            abstract = self.abstracts[i]
            eligibility = self.eligibilities[i]

            comboAbstractEligibility = '%s %s' % (abstract, eligibility)
            self.comboAbstractsEligibilities.append(comboAbstractEligibility)

    def getList(self):
        self.conatenateAbstractsEligibilities()
        return self.comboAbstractsEligibilities
