import pandas
import pickle
import numpy
from ClassStandingClassifierStuff.MakeDataSet import MakeDataSet


class OneVsRestClassifyClassStatusFromPretrainedModel(object):
    def __init__(self, pretrainedModelFile, pretrainedFeatureValueCountsFile, testingDataTextList, testingDataIdsList):
        self.pretrainedModelFile = pretrainedModelFile
        self.pretrainedFeatureValueCountsFile = pretrainedFeatureValueCountsFile
        self.testingDataTextList = testingDataTextList
        self.testingDataIdsList = testingDataIdsList

        self.testingSet = MakeDataSet.makeDataSet(labels='', dataTextList=self.testingDataTextList,
                                                  idsList=self.testingDataIdsList)

        self.dataFrame = self.makeDataFrame()

        pretrainedModelInput = open(self.pretrainedModelFile, 'rb')
        self.oneVsRestClassifier = pickle.load(pretrainedModelInput)
        pretrainedModelInput.close()

        pretrainedFeaturesValueCountsInput = open(self.pretrainedFeatureValueCountsFile, 'rb')
        self.pretrainedFeaturesValueCountIndexes = pickle.load(pretrainedFeaturesValueCountsInput)
        pretrainedFeaturesValueCountsInput.close()

    def getPredictionsAndIds(self):
        self.testOVRClassifier()
        predictions = self.dataFrame['prediction']
        ids = self.dataFrame['id']

        return predictions, ids

    def testOVRClassifier(self):
        testingFeaturesList = [testingInstance['features'] for testingInstance in self.testingSet]
        testingVectors = self.makeFeaturesVectors(testingFeaturesList, self.pretrainedFeaturesValueCountIndexes)
        self.dataFrame['prediction'] = self.oneVsRestClassifier.predict(testingVectors)

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
