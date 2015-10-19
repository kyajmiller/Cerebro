from ClassStandingClassifierStuff.GetDatabaseInfoScholarshipsWithClassStatuses import \
    GetDatabaseInfoScholarshipsWithClassStatuses


class CalculateEnsembleClassifierAccuracy(object):
    def __init__(self):
        databaseInfo = GetDatabaseInfoScholarshipsWithClassStatuses()
        self.actualLabels = databaseInfo.getRequirementNeededList()
        self.predictedLabels = databaseInfo.getEnsembleClassifierPredictions()

        print(self.convertActualLabelStringsToList()[5])

    def convertActualLabelStringsToList(self):
        actualLabelLists = []

        for actualLabelString in self.actualLabels:
            unformattedActualLabelList = actualLabelString.split(',')
            filteredList = [label for label in unformattedActualLabelList if label != '']
            actualLabelLists.append(filteredList)

        return actualLabelLists


CalculateEnsembleClassifierAccuracy()
