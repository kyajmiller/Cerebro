import pandas
import itertools
import numpy
from sklearn.linear_model import LogisticRegression
from ClassStandingClassifierStuff.MakeDataSetClassifyClassStatus import MakeDataSetClassifyClassStatus


class ClassifyClassStatus(object):
    def __init__(self, classStatus, trainingPercentage):
        self.classStatus = classStatus
        self.trainingPercentage = trainingPercentage
        self.badLabel = 'Other'

        trainingTestingList = MakeDataSetClassifyClassStatus(classStatus).makeTrainingAndTestingSets(
            self.trainingPercentage)
        self.training = trainingTestingList[0]
        self.testing = trainingTestingList[1]

        self.dataFrame = self.makeDataFrame()

        self.trainingVectors = []
        self.testingVectors = []

        self.logisticRegressionClassifier = LogisticRegression()

    def trainTestAndGetResults(self):
        self.trainLogisticRegressionClassifier()
        self.testLogisticRegressionClassifier()

        print("Results for label '%s':" % self.classStatus)
        self.printMetrics(*self.computeMetrics(
            *self.getTrueFalsePositivesNegatives(self.dataFrame['label'], self.dataFrame['prediction'],
                                                 desiredLabel=self.classStatus)))

        print("Results for label '%s':" % self.badLabel)
        self.printMetrics(*self.computeMetrics(
            *self.getTrueFalsePositivesNegatives(self.dataFrame['label'], self.dataFrame['prediction'],
                                                 desiredLabel=self.badLabel)))

    def trainLogisticRegressionClassifier(self):
        trainingFeaturesList = [trainingInstance['features'] for trainingInstance in self.training]
        testingFeaturesList = [testingInstance['features'] for testingInstance in self.testing]

        trainingLabels = [trainingInstance['label'] for trainingInstance in self.training]

        featuresSeries = pandas.Series(list(itertools.chain(*trainingFeaturesList)))
        featuresValueCounts = featuresSeries.value_counts()
        featuresValueCountsIndexes = featuresValueCounts.index

        self.trainingVectors = self.makeFeaturesVectors(trainingFeaturesList, featuresValueCountsIndexes)
        self.testingVectors = self.makeFeaturesVectors(testingFeaturesList, featuresValueCountsIndexes)

        self.logisticRegressionClassifier.fit(self.trainingVectors, trainingLabels)

    def testLogisticRegressionClassifier(self):
        self.dataFrame['prediction'] = self.logisticRegressionClassifier.predict(self.testingVectors)

    def makeDataFrame(self):
        frame = pandas.DataFrame(columns=['label', 'scholarshipId', 'features'])
        for index, value in enumerate(self.testing):
            frame.loc[index] = [value['label'], value['scholarshipId'], value['features']]

        return frame

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

    def getTrueFalsePositivesNegatives(self, actualLablesList, predictedLabelsList, desiredLabel):
        truePositives = 0
        trueNegatives = 0
        falsePositives = 0
        falseNegatives = 0

        for actualLabel, predictedLabel in zip(actualLablesList, predictedLabelsList):
            if actualLabel == predictedLabel:
                if actualLabel == desiredLabel:
                    truePositives += 1
                else:
                    trueNegatives += 1
            else:
                if actualLabel == desiredLabel:
                    falseNegatives += 1
                else:
                    falsePositives += 1

        return truePositives, trueNegatives, falsePositives, falseNegatives

    def computeMetrics(self, truePositives, trueNegatives, falsePositives, falseNegatives):
        accuracy = (truePositives + trueNegatives) / (truePositives + trueNegatives + falsePositives + falseNegatives)
        precision = truePositives / (truePositives + falsePositives)
        recall = truePositives / (truePositives + falseNegatives)
        f1 = 2 * ((precision * recall) / (precision + recall))

        return accuracy, precision, recall, f1

    def printMetrics(self, accuracy, precision, recall, f1):
        print('Accuracy:\t%s' % accuracy)
        print('Precision:\t%s' % precision)
        print('Recall:\t\t%s' % recall)
        print('F1:\t\t\t%s' % f1)
