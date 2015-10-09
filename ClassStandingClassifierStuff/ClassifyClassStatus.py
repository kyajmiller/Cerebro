import pandas
import itertools
import numpy
from sklearn.linear_model import LogisticRegression
from ClassStandingClassifierStuff.MakeDataSetClassifyClassStatus import MakeDataSetClassifyClassStatus


class ClassifyClassStatus(object):
    def __init__(self, classStatus, trainingPercentage):
        self.classStatus = classStatus
        self.trainingPercentage = trainingPercentage

        trainingTestingList = MakeDataSetClassifyClassStatus(classStatus).makeTrainingAndTestingSets(
            self.trainingPercentage)
        self.training = trainingTestingList[0]
        self.testing = trainingTestingList[1]

        self.dataFrame = self.makeDataFrame()

    def makeDataFrame(self):
        frame = pandas.DataFrame(columns=['label', 'features'])
        for index, value in enumerate(self.testing):
            frame.loc[index] = [value['label'], value['features']]

        return frame

    def trainLogisticRegressionClassifier(self):
        totalFeaturesList = [trainingLine['features'] for trainingLine in self.training]

        featuresSeries = pandas.Series(list(itertools.chain(*totalFeaturesList)))
        featuresValueCounts = featuresSeries.value_counts()
        featuresValueCountsIndexes = featuresValueCounts.index

        trainingVectors = self.makeFeaturesVectors(totalFeaturesList, featuresValueCountsIndexes)

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

        return totalFeaturesList
