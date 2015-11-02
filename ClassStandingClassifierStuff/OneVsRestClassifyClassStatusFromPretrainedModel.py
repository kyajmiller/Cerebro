import pandas
import pickle
import numpy
from ClassStandingClassifierStuff.MakeDataSetClassifyClassStatus import MakeDataSetClassifyClassStatus


class OneVsRestClassifyClassStatusFromPretrainedModel(object):
    def __init__(self, pretrainedModelFile, pretrainedFeatureValueCountsFile, testingDataTextList, testingDataIdsList):
        self.pretrainedModelFile = pretrainedModelFile
        self.pretrainedFeatureValueCountsFile = pretrainedFeatureValueCountsFile
        self.testingDataTextList = testingDataTextList
        self.testingDataIdsList = testingDataIdsList

        self.trainingSet = MakeDataSetClassifyClassStatus.makeDataSet(labels='', dataTextList=self.testingDataTextList,
                                                                      idsList=self.testingDataIdsList)

        self.dataFrame = self.makeDataFrame()

        pretrainedModelInput = open(self.pretrainedModelFile, 'rb')
        self.oneVsRestLRClassifier = pickle.load(pretrainedModelInput)
        pretrainedModelInput.close()

        pretrainedFeaturesValueCountsInput = open(self.pretrainedFeatureValueCountsFile, 'rb')
        self.pretrainedFeaturesValueCountIndexes = pickle.load(pretrainedFeaturesValueCountsInput)
        pretrainedFeaturesValueCountsInput.close()

    def makeDataFrame(self):
        frame = pandas.DataFrame(columns=['label', 'id', 'features'])
        for index, value in enumerate(self.testingSet):
            frame.loc[index] = [value['label'], value['id'], value['features']]

        return frame
