from Classes.SUDBConnect import SUDBConnect
from Classes.CleanText import CleanText


class GetDatabaseInfoScholarshipsWithClassStatuses(object):
    def __init__(self, requirementNeeded=None, useNot=False):
        self.requirementNeeded = requirementNeeded
        self.useNot = useNot
        if self.requirementNeeded:
            self.formattedRequirementNeeded = '%' + self.requirementNeeded + '%'
        self.db = SUDBConnect()

        if self.requirementNeeded == 'Senior':
            self.rows = self.db.getRows(
                "select * from dbo.ScholarshipsWithClassStatuses where RequirementNeeded like '%Senior%' and RequirementNeeded not like '%High School Senior%'")
        elif self.requirementNeeded and self.useNot:
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
                                       scholarshipDescriptionsList if type(description) == str]

        return scholarshipDescriptionsList

    def getEligibilitiesList(self):
        eligibilitiesList = []

        for row in self.rows:
            eligibilitiesList.append(row.Eligibility)

        eligibilitiesList = [CleanText.cleanALLtheText(eligibility) for eligibility in eligibilitiesList if
                             type(eligibility) == str]

        return eligibilitiesList

    def getScholarshipsWithClassStatusIdsList(self):
        idsList = []

        for row in self.rows:
            idsList.append(str(row.ScholarshipsWithClassStatusId))

        return idsList

    def getConcatenatedDescriptionsEligibilities(self):
        descriptionsList = self.getScholarshipDescriptionsList()
        eligibilitiesList = self.getEligibilitiesList()

        concatenatedItemsList = []

        for i in range(len(descriptionsList)):
            description = descriptionsList[i]
            eligibility = eligibilitiesList[i]

            concatenatedItem = '%s %s' % (description, eligibility)
            concatenatedItemsList.append(concatenatedItem)

        return concatenatedItemsList

    def getEnsembleClassifierPredictions(self):
        predictionsList = []

        for row in self.rows:
            predictionsList.append(row.EnsembleClassifierPrediction)

        return predictionsList

    def getRequirementNeededList(self):
        requirementNeededList = []

        for row in self.rows:
            requirementNeededList.append(row.RequirementNeeded)

        return requirementNeededList
