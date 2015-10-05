from Classes.SUDBConnect import SUDBConnect


class GetDatabaseInfoScholarshipsWithClassStatuses(object):
    def __init__(self, requirementNeeded):
        self.requirementNeeded = requirementNeeded
        self.formattedRequirementNeeded = '%' + self.requirementNeeded + '%'
        self.db = SUDBConnect()

        self.rows = self.db.getRows(
            "select * from dbo.ScholarshipsWithClassStatuses where RequirementNeeded like '" + self.formattedRequirementNeeded + "'")

    def getScholarshipDescriptionsList(self):
        scholarshipDescriptionsList = []

        for row in self.rows:
            scholarshipDescriptionsList.append(row.ScholarshipDescription)

        return scholarshipDescriptionsList



GetDatabaseInfoScholarshipsWithClassStatuses("cheese")
