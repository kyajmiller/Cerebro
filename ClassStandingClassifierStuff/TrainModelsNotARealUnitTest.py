import unittest
from ClassStandingClassifierStuff.ClassifyClassStatusUntrained import ClassifyClassStatusTrainFirst


class TestStringMethods(unittest.TestCase):
    def test_trainFreshmanModel(self):
        classStatus = 'Freshman'
        modelSaveFile = 'ClassifierTrainedModels\FreshmanClassStatusTrainedLRModel'
        featuresValueCountsSaveFile = 'ClasifierTrainedModels\FreshmanClassStatusTrainedFeaturesValueCounts'
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()


if __name__ == '__main__':
    unittest.main()
