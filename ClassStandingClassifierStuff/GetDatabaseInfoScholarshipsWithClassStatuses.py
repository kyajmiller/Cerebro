from Classes.SUDBConnect import SUDBConnect
from Classes.CleanText import CleanText


class GetDatabaseInfoScholarshipsWithClassStatuses(object):
    def __init__(self, requirementNeeded=None, useNot=False):
        self.requirementNeeded = requirementNeeded
        self.formattedRequirementNeeded = '%' + self.requirementNeeded + '%'
        self.db = SUDBConnect()

        if self.requirementNeeded and useNot:
            self.rows = self.db.getRows(
                "select * from dbo.ScholarshipsWithClassStatuses where RequirementNeeded not like '" + self.formattedRequirementNeeded + "'")
        elif self.requirementNeeded:
            self.rows = self.db.getRows(
                "select * from dbo.ScholarshipsWithClassStatuses where RequirementNeeded like '" + self.formattedRequirementNeeded + "'")
        else:
            self.rows = self.db.getRows("select * from dbo.ScholarshipsWithClassStatuses")

    def getScholarshipDescriptionsList(self):
        scholarshipDescriptionsList = []

        for row in self.rows:
            scholarshipDescriptionsList.append(row.ScholarshipDescription)

        scholarshipDescriptionsList = [CleanText.cleanALLtheText(description) for description in
                                       scholarshipDescriptionsList]

        return scholarshipDescriptionsList

    def getEligibilitiesList(self):
        eligibilitiesList = []

        for row in self.rows:
            eligibilitiesList.append(row.Eligibility)

        eligibilitiesList = [CleanText.cleanALLtheText(eligibility) for eligibility in eligibilitiesList if
                             type(eligibility) == str]

        return eligibilitiesList
