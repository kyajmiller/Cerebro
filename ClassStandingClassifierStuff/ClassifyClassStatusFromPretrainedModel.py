import pandas
import pickle
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

    def testLogisticRegressionClassifier(self):
        print('Classifying test data...')
        self.dataFrame['prediction'] = self.logisticRegressionClassifier.predict(self.testingVectors)

    def makeDataFrame(self):
        frame = pandas.DataFrame(columns=['label', 'scholarshipId', 'features'])
        for index, value in enumerate(self.testing):
            frame.loc[index] = [value['label'], value['scholarshipId'], value['features']]

        return frame

    def displayResults(self):
        self.testLogisticRegressionClassifier()
        predictions = self.dataFrame['prediction']
        ids = self.dataFrame['scholarshipIds']

        for predictedLabel, id in zip(predictions, ids):
            print('%s: %s' % (id, predictedLabel))
