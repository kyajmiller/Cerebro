import numpy
import pandas
import itertools
import pickle
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from ClassStandingClassifierStuff.MakeDataSetClassifyClassStatus import MakeDataSetClassifyClassStatus


class OneVsRestClassifyClassStatusPreviouslyUntrained(object):
    def __init__(self, dataTextList, labelsList, idsList, trainingPercentage=0.8):
        self.dataTextList = dataTextList
        self.labelsList = labelsList
        self.idsList = idsList
        self.trainingPercentage = trainingPercentage

        self.trainingSet, self.testingSet = MakeDataSetClassifyClassStatus.makeMultilabelTrainingAndTestingSet(
            self.dataTextList, self.labelsList, self.idsList, self.trainingPercentage)

        self.dataFrame = self.makeDataFrame()

        self.featuresValueCountIndexes = []

        self.oneVsRestClassifier = OneVsRestClassifier(LogisticRegression())

    def trainTestAndDisplayResults(self):
        self.trainOVRClassifier()
        self.testOVRClassifier()
        self.printResults()

    def trainOVRClassifier(self):
        trainingLabelsList = [trainingInstance['label'] for trainingInstance in self.trainingSet]
        trainingVectors = self.getTrainingAndTestingVectors(trainingOnly=True, both=False)
        self.oneVsRestClassifier.fit(trainingVectors, trainingLabelsList)

    def testOVRClassifier(self):
        testingVectors = self.getTrainingAndTestingVectors(both=False, testingOnly=True)
        self.dataFrame['prediction'] = self.oneVsRestClassifier.predict(testingVectors)

    def getTrainingAndTestingVectors(self, both=True, trainingOnly=False, testingOnly=False):
        trainingFeaturesList = [trainingInstance['features'] for trainingInstance in self.trainingSet]
        testingFeaturesList = [testingInstance['features'] for testingInstance in self.testingSet]

        featuresSeries = pandas.Series(list(itertools.chain(*trainingFeaturesList)))
        featuresValueCounts = featuresSeries.value_counts()
        self.featuresValueCountIndexes = featuresValueCounts.index

        if trainingOnly:
            trainingVectors = self.makeFeaturesVectors(trainingFeaturesList, self.featuresValueCountIndexes)
            return trainingVectors
        elif testingOnly:
            testingVectors = self.makeFeaturesVectors(testingFeaturesList, self.featuresValueCountIndexes)
            return testingVectors
        elif both:
            trainingVectors = self.makeFeaturesVectors(trainingFeaturesList, self.featuresValueCountIndexes)
            testingVectors = self.makeFeaturesVectors(testingFeaturesList, self.featuresValueCountIndexes)
            return trainingVectors, testingVectors

    def makeFeaturesVectors(self, totalFeaturesList, featuresValueCountsIndexes):
        featuresVectors = numpy.matrix(numpy.zeros((len(totalFeaturesList), featuresValueCountsIndexes.shape[0] + 1)))

        # insert bias
        featuresVectors[:, 0] = 1

        for totalFeaturesIndex, totalFeaturesData in enumerate(totalFeaturesList):
            # make regular vector
            totalFeaturesData = pandas.Series(totalFeaturesData)
            vectorCounts = totalFeaturesData.value_counts()

            # make features vector
            for featuresValueCountsIndexesIndex, featuresValueCountsIndexesValue in enumerate(
                    featuresValueCountsIndexes):
                if featuresValueCountsIndexesValue in vectorCounts.index:
                    featuresVectors[totalFeaturesIndex, featuresValueCountsIndexesIndex + 1] = vectorCounts.ix[
                        featuresValueCountsIndexesValue]

        return featuresVectors

    def makeDataFrame(self):
        frame = pandas.DataFrame(columns=['label', 'id', 'features'])
        for index, value in enumerate(self.testingSet):
            frame.loc[index] = [value['label'], value['id'], value['features']]

        return frame

    def printResults(self):
        actualLabels = self.dataFrame['label']
        predictedLabels = self.dataFrame['prediction']

        total = len(predictedLabels)
        matches = 0

        for actualLabel, predictedLabel in zip(actualLabels, predictedLabels):
            if sorted(actualLabel) == sorted(predictedLabel):
                matchMessage = 'Matched!'
                matches += 1
            else:
                matchMessage = 'No match.'

            formattedString = '%s Actual label: %s; Predicted label: %s' % (matchMessage, actualLabel, predictedLabel)
            print(formattedString)

        accuracy = matches / total
        print('Total accuracy: %.2f' % (accuracy * 100))
