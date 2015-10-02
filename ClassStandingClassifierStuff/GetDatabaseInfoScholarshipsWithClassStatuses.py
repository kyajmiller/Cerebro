from Classes.SUDBConnect import SUDBConnect


class GetDatabaseInfoScholarshipsWithClassStatuses(object):
    def __init__(self, requirementNeeded):
        self.requirementNeeded = requirementNeeded
        self.formattedRequirementNeeded = '%' + self.requirementNeeded + '%'
        self.db = SUDBConnect()
        print(self.formattedRequirementNeeded)


GetDatabaseInfoScholarshipsWithClassStatuses("cheese")
