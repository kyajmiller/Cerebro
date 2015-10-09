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
        features = pandas.Series(list(itertools.chain(*[trainingLine['features'] for trainingLine in self.training])))
        features = features.value_counts()

    def makeFeaturesVectors(self, featuresValues, featuresCounts):
        featuresVectors = numpy.matrix(numpy.zeros((len(featuresValues), featuresCounts.shape[0] + 1)))

        # insert bias
        featuresVectors[:, 0] = 1

        for featuresValuesIndex, featuresValuesData in enumerate(featuresValues):
            # make regular vector
            featuresValuesData = pandas.Series(featuresValuesData)
            vectorCounts = featuresValuesData.value_counts()

            # make features vector
            for featuresCountsIndex, featuresCountsValue in enumerate(featuresCounts):
                if featuresCountsValue in vectorCounts.index:
                    featuresVectors[featuresValuesIndex, featuresCountsIndex + 1] = vectorCounts.ix[featuresCountsValue]

        return featuresValues
