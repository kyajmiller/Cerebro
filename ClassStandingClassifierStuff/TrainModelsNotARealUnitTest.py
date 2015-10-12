import unittest
from ClassStandingClassifierStuff.ClassifyClassStatus import ClassifyClassStatus


class TestStringMethods(unittest.TestCase):
    def test_trainFreshmanModel(self):
        testClassify = ClassifyClassStatus(classStatus='Freshman', trainingPercentage=0.99,
                                           modelSaveFile='ClassifierTrainedModels\FreshmanClassStatusTrainedLRModel')
        testClassify.trainAndSaveModel()


if __name__ == '__main__':
    unittest.main()
