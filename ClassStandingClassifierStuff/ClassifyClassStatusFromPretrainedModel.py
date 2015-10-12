import pandas
import itertools
import numpy
import pickle
from sklearn.linear_model import LogisticRegression
from ClassStandingClassifierStuff.MakeDataSetClassifyClassStatus import MakeDataSetClassifyClassStatus


class ClassifyClassStatusFromPretrainedModel(object):
    def __init__(self, trainedModelInputFile, testingData):
        self.trainedModelInputFile = trainedModelInputFile
        self.testingData = testingData

        self.testing = MakeDataSetClassifyClassStatus().makeOnlyTrainingSet()

        self.dataFrame = self.makeDataFrame()

        self.testingVectors = []

        modelInput = open(trainedModelInputFile, 'rb')
        self.logisticRegressionClassifier = pickle.load(modelInput)
        modelInput.close()

    def makeDataFrame(self):
        frame = pandas.DataFrame(columns=['label', 'scholarshipId', 'features'])
        for index, value in enumerate(self.testing):
            frame.loc[index] = [value['label'], value['scholarshipId'], value['features']]

        return frame
