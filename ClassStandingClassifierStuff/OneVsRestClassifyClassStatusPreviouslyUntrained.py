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

        self.trainingVectors = []
        self.featuresValueCountIndexes = []

        self.testingVectors = []

        self.oneVsRestClassifier = OneVsRestClassifier(LogisticRegression())

    def trainOVRClassifier(self):
        trainingFeaturesList = [trainingInstance['features'] for trainingInstance in self.trainingSet]
        trainingLabelsList = [trainingInstance['label'] for trainingInstance in self.trainingSet]

        featuresSeries = pandas.Series(list(itertools.chain(*trainingFeaturesList)))
        featuresValueCounts = featuresSeries.value_counts()
        self.featuresValueCountIndexes = featuresValueCounts.index

        self.trainingVectors = self.makeFeaturesVectors(trainingFeaturesList, self.featuresValueCountIndexes)

        self.oneVsRestClassifier.fit(self.trainingVectors, trainingLabelsList)

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
        frame = pandas.DataFrame(columns=['label', 'scholarshipId', 'features'])
        for index, value in enumerate(self.testingSet):
            frame.loc[index] = [value['label'], value['scholarshipId'], value['features']]

        return frame
