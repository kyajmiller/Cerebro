from ClassStandingClassifierStuff.GetDatabaseInfoScholarshipsWithClassStatuses import \
    GetDatabaseInfoScholarshipsWithClassStatuses


class CalculateEnsembleClassifierAccuracy(object):
    def __init__(self):
        databaseInfo = GetDatabaseInfoScholarshipsWithClassStatuses()
        self.actualLabels = databaseInfo.getRequirementNeededList()
        self.predictedLabels = databaseInfo.getEnsembleClassifierPredictions()

        self.actualLabels = self.convertActualLabelStringsToList()
        self.predictedLabels = self.convertPredictedLabelStringsToList()

        self.calculateExactMatchAccuracy()
        self.calculateNumLabelsAccuracy()
        print(
            "Average Accuracy Across Labels: %.2f percent" % self.calculateAverageAccuracyWithinLists(self.actualLabels,
                                                                                                      self.predictedLabels))
        self.calculateListAccuracyWithinMatchedGreaterOrLesserListLengths()

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

    def calculateAverageAccuracyWithinLists(self, actualLabels, predictedLabels):
        total = len(actualLabels)
        accuracyCount = 0

        for actualLabel, predictedLabel in zip(actualLabels, predictedLabels):
            numAccurateLabels = 0
            totalLabels = len(predictedLabel)
            if totalLabels > 0:
                for label in predictedLabel:
                    if label in actualLabel:
                        numAccurateLabels += 1
                labelAccuracy = numAccurateLabels / totalLabels
                accuracyCount += labelAccuracy

        averageAccuracy = (accuracyCount / total) * 100
        return averageAccuracy

    def calculateNumLabelsAccuracy(self):
        total = len(self.actualLabels)

        numLabelsMatches = 0
        numLabelsGreater = 0
        numLabelsSmaller = 0

        for actualLabel, predictedLabel in zip(self.actualLabels, self.predictedLabels):
            if len(actualLabel) == len(predictedLabel):
                numLabelsMatches += 1
            elif len(predictedLabel) > len(actualLabel):
                numLabelsGreater += 1
            else:
                numLabelsSmaller += 1

        percentMatches = numLabelsMatches / total
        percentGreater = numLabelsGreater / total
        percentSmaller = numLabelsSmaller / total

        print("Num labels matches: %.2f percent" % (percentMatches * 100))
        print("Num labels greater: %.2f percent" % (percentGreater * 100))
        print("Num labels smaller: %.2f percent" % (percentSmaller * 100))

    def calculateListAccuracyWithinMatchedGreaterOrLesserListLengths(self):
        matchedLengthLabelsActual = []
        matchedLengthLabelsPredicted = []
        greaterLengthLabelsActual = []
        greaterLengthLabelsPredicted = []
        lesserLengthLabelsActual = []
        lesserLengthLabelsPredicted = []

        for actual, predicted in zip(self.actualLabels, self.predictedLabels):
            if len(actual) == len(predicted):
                matchedLengthLabelsActual.append(actual)
                matchedLengthLabelsPredicted.append(predicted)
            elif len(predicted) > len(actual):
                greaterLengthLabelsActual.append(actual)
                greaterLengthLabelsPredicted.append(predicted)
            else:
                lesserLengthLabelsActual.append(actual)
                lesserLengthLabelsPredicted.append(predicted)

        listAccuracyMatches = self.calculateAverageAccuracyWithinLists(matchedLengthLabelsActual,
                                                                       matchedLengthLabelsPredicted)
        listAccuracyGreater = self.calculateAverageAccuracyWithinLists(greaterLengthLabelsActual,
                                                                       greaterLengthLabelsPredicted)
        listAccuracyLesser = self.calculateAverageAccuracyWithinLists(lesserLengthLabelsActual,
                                                                      lesserLengthLabelsPredicted)

        print("Average Accuracy Within Matched Length Lists: %.2f percent" % listAccuracyMatches)
        print("Average Accuracy Within Greater Length Lists: %.2f percent" % listAccuracyGreater)
        print("Average Accuracy Within Lesser Length Lists: %.2f percent" % listAccuracyLesser)







CalculateEnsembleClassifierAccuracy()
