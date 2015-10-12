import unittest
from ClassStandingClassifierStuff.ClassifyClassStatusFromPreviouslyUntrainedModel import ClassifyClassStatusTrainFirst


class TestStringMethods(unittest.TestCase):
    def test_trainFreshmanModel(self):
        classStatus = 'Freshman'
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % classStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % classStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()

    def test_trainSophomoreModel(self):
        classStatus = 'Sophomore'
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % classStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % classStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()

    def test_seeIfCanWriteToFile(self):
        classStatus = 'Freshman'
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % classStatus
        outputFile = open(featuresValueCountsSaveFile, 'w')
        outputFile.write('cheese')
        outputFile.close()



if __name__ == '__main__':
    unittest.main()
