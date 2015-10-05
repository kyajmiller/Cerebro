from Classes.SUDBConnect import SUDBConnect
from Classes.CleanText import CleanText


class GetDatabaseInfoScholarshipsWithClassStatuses(object):
    def __init__(self, requirementNeeded):
        self.requirementNeeded = requirementNeeded
        self.formattedRequirementNeeded = '%' + self.requirementNeeded + '%'
        self.db = SUDBConnect()

        self.rows = self.db.getRows(
            "select * from dbo.ScholarshipsWithClassStatuses where RequirementNeeded like '" + self.formattedRequirementNeeded + "'")

        print(len(self.rows))

    def getScholarshipDescriptionsList(self):
        scholarshipDescriptionsList = []

        for row in self.rows:
            scholarshipDescriptionsList.append(CleanText.cleanALLtheText(row.ScholarshipDescription))

        return scholarshipDescriptionsList

    def getEligibilitiesList(self):
        eligibilitiesList = []

        for row in self.rows:
            eligibilitiesList.append(CleanText.cleanALLtheText(row.Eligibility))

        return eligibilitiesList
