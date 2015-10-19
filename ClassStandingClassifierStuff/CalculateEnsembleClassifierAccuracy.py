from ClassStandingClassifierStuff.GetDatabaseInfoScholarshipsWithClassStatuses import \
    GetDatabaseInfoScholarshipsWithClassStatuses


class CalculateEnsembleClassifierAccuracy(object):
    def __init__(self):
        databaseInfo = GetDatabaseInfoScholarshipsWithClassStatuses()
        self.actualLabels = databaseInfo.getRequirementNeededList()
        self.predictedLabels = databaseInfo.getEnsembleClassifierPredictions()

    def convertActualLabelStringsToList(self):
        actualLabelLists = []

        for actualLabelString in self.actualLabels:
            unformattedActualLabelList = actualLabelString.split(',')
            filteredList = [label for label in unformattedActualLabelList if label != '']
            actualLabelLists.append(filteredList)

        return actualLabelLists

    def convertPredictedLabelStringsToList(self):
        predictedLabelLists = []

        for predictedLabelString in self.predictedLabels:
            if predictedLabelString is None:
                predictedLabelList = []
            else:
                predictedLabelList = predictedLabelString.split(', ')
            predictedLabelLists.append(predictedLabelList)

        return predictedLabelLists
