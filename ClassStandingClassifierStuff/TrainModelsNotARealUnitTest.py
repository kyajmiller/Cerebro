import unittest
from ClassStandingClassifierStuff.ClassifyClassStatusUntrained import ClassifyClassStatusTrainFirst


class TestStringMethods(unittest.TestCase):
    def test_trainFreshmanModel(self):
        classStatus = 'Freshman'
        modelSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedLRModel' % classStatus
        featuresValueCountsSaveFile = 'ClasifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % classStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()

    def test_trainSophomoreModel(self):
        classStatus = 'Sophomore'
        modelSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedLRModel' % classStatus
        featuresValueCountsSaveFile = 'ClasifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % classStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()


if __name__ == '__main__':
    unittest.main()
