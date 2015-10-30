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
        self.testingVectors = []

        self.oneVsRestClassifier = OneVsRestClassifier(LogisticRegression())

    def makeDataFrame(self):
        frame = pandas.DataFrame(columns=['label', 'scholarshipId', 'features'])
        for index, value in enumerate(self.testingSet):
            frame.loc[index] = [value['label'], value['scholarshipId'], value['features']]

        return frame
