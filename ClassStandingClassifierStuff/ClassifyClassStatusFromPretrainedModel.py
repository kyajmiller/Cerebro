import pandas
import pickle
import numpy
import itertools
from ClassStandingClassifierStuff.MakeDataSetClassifyClassStatus import MakeDataSetClassifyClassStatus


class ClassifyClassStatusFromPretrainedModel(object):
    def __init__(self, trainedModelInputFile, testingDataTextList, testingDataIdsList):
        self.trainedModelInputFile = trainedModelInputFile
        self.testingDataTextList = testingDataTextList
        self.testingDataIdsList = testingDataIdsList

        self.testing = MakeDataSetClassifyClassStatus(testingDataTextList=self.testingDataTextList,
                                                      testingDataIds=testingDataIdsList).makeOnlyTrainingSet()

        self.dataFrame = self.makeDataFrame()

        self.testingVectors = []

        modelInput = open(trainedModelInputFile, 'rb')
        self.logisticRegressionClassifier = pickle.load(modelInput)
        modelInput.close()

    def testLogisticRegressionClassifier(self):
        testingFeaturesList = [testingInstance['features'] for testingInstance in self.testing]
        featuresSeries = pandas.Series(list(itertools.chain(*testingFeaturesList)))
        featuresValueCounts = featuresSeries.value_counts()
        featuresValueCountsIndexes = featuresValueCounts.index
        self.testingVectors = self.makeFeaturesVectors(testingFeaturesList, featuresValueCountsIndexes)

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

    def displayResults(self):
        self.testLogisticRegressionClassifier()
        predictions = self.dataFrame['prediction']
        ids = self.dataFrame['scholarshipIds']

        for predictedLabel, id in zip(predictions, ids):
            print('%s: %s' % (id, predictedLabel))
