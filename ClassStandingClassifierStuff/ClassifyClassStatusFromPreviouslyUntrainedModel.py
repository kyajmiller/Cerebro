import pandas
import itertools
import numpy
import pickle
from sklearn.linear_model import LogisticRegression
from ClassStandingClassifierStuff.OVRLRMakeDataSetClassifyClassStatus import MakeDataSetClassifyClassStatus


class ClassifyClassStatusTrainFirst(object):
    def __init__(self, classStatus, trainingPercentage, modelSaveFile=None, featuresValuesCountsSaveFile=None):
        self.classStatus = classStatus
        self.trainingPercentage = trainingPercentage
        self.badLabel = 'Other'
        self.modelSaveFile = modelSaveFile
        self.featuresValueCountsSaveFile = featuresValuesCountsSaveFile

        print('Creating datasets...')
        trainingTestingList = MakeDataSetClassifyClassStatus(self.classStatus).makeTrainingAndTestingSets(
            self.trainingPercentage)
        self.training = trainingTestingList[0]
        self.testing = trainingTestingList[1]

        self.dataFrame = self.makeDataFrame()

        self.trainingVectors = []
        self.testingVectors = []

        self.featuresValueCountsIndexes = []
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

    def trainAndSaveModel(self):
        self.trainLogisticRegressionClassifier()
        self.saveTrainedModelToFile()
        self.saveFeaturesValueCountIndexesToFile()

    def saveTrainedModelToFile(self):
        if not self.modelSaveFile:
            print('No model save file declared.')
        else:
            print("Saving model to file '%s'..." % self.modelSaveFile)
            saveFileOutput = open(self.modelSaveFile, 'wb')
            pickle.dump(self.logisticRegressionClassifier, saveFileOutput)
            saveFileOutput.close()

    def saveFeaturesValueCountIndexesToFile(self):
        if not self.featuresValueCountsSaveFile:
            print('No features value counts save file declared.')
        else:
            print("Saving features value counts to file '%s'" % self.featuresValueCountsSaveFile)
            saveFileOutput = open(self.featuresValueCountsSaveFile, 'wb')
            pickle.dump(self.featuresValueCountsIndexes, saveFileOutput)
            saveFileOutput.close()

    def trainLogisticRegressionClassifier(self):
        trainingFeaturesList = [trainingInstance['features'] for trainingInstance in self.training]
        testingFeaturesList = [testingInstance['features'] for testingInstance in self.testing]

        trainingLabels = [trainingInstance['label'] for trainingInstance in self.training]

        featuresSeries = pandas.Series(list(itertools.chain(*trainingFeaturesList)))
        featuresValueCounts = featuresSeries.value_counts()
        featuresValueCountsIndexes = featuresValueCounts.index
        self.featuresValueCountsIndexes = featuresValueCountsIndexes

        print('Creating features vectors...')
        self.trainingVectors = self.makeFeaturesVectors(trainingFeaturesList, featuresValueCountsIndexes)
        self.testingVectors = self.makeFeaturesVectors(testingFeaturesList, featuresValueCountsIndexes)

        print("Training Logistic Regression Classifier for '%s'..." % self.classStatus)
        self.logisticRegressionClassifier.fit(self.trainingVectors, trainingLabels)

    def testLogisticRegressionClassifier(self):
        print('Classifying test data...')
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
        print('Accuracy:\t%.4f' % accuracy)
        print('Precision:\t%.4f' % precision)
        print('Recall:\t\t%.4f' % recall)
        print('F1:\t\t\t%.4f' % f1)
