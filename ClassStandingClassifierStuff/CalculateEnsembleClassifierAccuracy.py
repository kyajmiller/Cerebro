from ClassStandingClassifierStuff.GetDatabaseInfoScholarshipsWithClassStatuses import \
    GetDatabaseInfoScholarshipsWithClassStatuses


class CalculateEnsembleClassifierAccuracy(object):
    def __init__(self):
        databaseInfo = GetDatabaseInfoScholarshipsWithClassStatuses()
        self.actualLabels = databaseInfo.getRequirementNeededList()
        self.predictedLabels = databaseInfo.getEnsembleClassifierPredictions()

        self.actualLabels = self.convertActualLabelStringsToList()
        self.predictedLabels = self.convertPredictedLabelStringsToList()

    def convertActualLabelStringsToList(self):
        actualLabelLists = []

        for actualLabelString in self.actualLabels:
            unformattedActualLabelList = actualLabelString.split(',')
            filteredList = [label for label in unformattedActualLabelList if label != '']
            filteredList = sorted(filteredList)
            actualLabelLists.append(filteredList)

        return actualLabelLists

    def convertPredictedLabelStringsToList(self):
        predictedLabelLists = []

        for predictedLabelString in self.predictedLabels:
            if predictedLabelString is None:
                predictedLabelList = []
            else:
                predictedLabelList = predictedLabelString.split(', ')
                predictedLabelList = sorted(predictedLabelList)
            predictedLabelLists.append(predictedLabelList)

        return predictedLabelLists

    def calculateExactMatchAccuracy(self):
        total = len(self.actualLabels)
        matches = 0

        for actualLabel, predictedLabel in zip(self.actualLabels, self.predictedLabels):
            if actualLabel == predictedLabel:
                matches += 1

        accuracy = (matches / total) * 100

        print("Exact Match Accuracy: %.2f percent" % accuracy)


CalculateEnsembleClassifierAccuracy().calculateExactMatchAccuracy()
