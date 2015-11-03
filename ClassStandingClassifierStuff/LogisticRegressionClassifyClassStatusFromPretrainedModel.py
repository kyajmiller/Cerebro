import pandas
import pickle
import numpy
from ClassStandingClassifierStuff.MakeDataSetClassifyClassStatus import MakeDataSetClassifyClassStatus


class LogisticRegressionClassifyClassStatusFromPretrainedModel(object):
    def __init__(self, trainedModelInputFile, trainedFeaturesValueCountsIndexesFile, testingDataTextList,
                 testingDataIdsList):
        self.trainedFeaturesValueCountsIndexesFile = trainedFeaturesValueCountsIndexesFile
        self.trainedModelInputFile = trainedModelInputFile
        self.testingDataTextList = testingDataTextList
        self.testingDataIdsList = testingDataIdsList

        self.testing = MakeDataSetClassifyClassStatus.makeDataSet(labels='', dataTextList=self.testingDataTextList,
                                                                  idsList=self.testingDataIdsList)

        self.dataFrame = self.makeDataFrame()

        modelInput = open(self.trainedModelInputFile, 'rb')
        self.logisticRegressionClassifier = pickle.load(modelInput)
        modelInput.close()

        featuresValueCountsInput = open(self.trainedFeaturesValueCountsIndexesFile, 'rb')
        self.featuresValueCountsIndexes = pickle.load(featuresValueCountsInput)
        featuresValueCountsInput.close()

    def returnPredictions(self):
        self.doLogisticRegressionClassification()
        predictions = self.dataFrame['prediction']
        return predictions

    def doLogisticRegressionClassification(self):
        testingFeaturesList = [testingInstance['features'] for testingInstance in self.testing]
        testingVectors = self.makeFeaturesVectors(testingFeaturesList, self.featuresValueCountsIndexes)

        print('Classifying data...')
        self.dataFrame['prediction'] = self.logisticRegressionClassifier.predict(testingVectors)

    def makeDataFrame(self):
        frame = pandas.DataFrame(columns=['id', 'features'])
        for index, value in enumerate(self.testing):
            frame.loc[index] = [value['id'], value['features']]

        return frame

    def makeFeaturesVectors(self, totalFeaturesList, featuresValueCountsIndexes):
        print('Making features vectors...')
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
        self.doLogisticRegressionClassification()
        predictions = self.dataFrame['prediction']
        ids = self.dataFrame['id']

        countClassStatusPredictions = 0
        countOtherPredictions = 0
        total = 0

        classStatusLabel = ''

        for predictedLabel, id in zip(predictions, ids):
            print('%s: %s' % (id, predictedLabel))
            total += 1
            if predictedLabel == 'Other':
                countOtherPredictions += 1
            else:
                countClassStatusPredictions += 1
                classStatusLabel = predictedLabel

        print('\n')
        print("Counts for '%s': %s/%s (%.2f percent)" % (
        classStatusLabel, countClassStatusPredictions, total, (countClassStatusPredictions / total) * 100))
        print("Counts for 'Other': %s/%s (%.2f percent)" % (
        countOtherPredictions, total, (countOtherPredictions / total) * 100))
