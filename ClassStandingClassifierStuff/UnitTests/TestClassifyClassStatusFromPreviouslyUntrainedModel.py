import unittest
from ClassStandingClassifierStuff.LogisticRegressionClassifyClassStatusFromPreviouslyUntrainedModel import \
    LogisticRegressionClassifyClassStatusFromPreviouslyUntrainedModel


class TestStringMethods(unittest.TestCase):
    def test_classifyJuniorGetResults(self):
        testClassify = LogisticRegressionClassifyClassStatusFromPreviouslyUntrainedModel(classStatus='Junior',
                                                                                         trainingPercentage=0.8)
        testClassify.trainTestAndGetResults()

    def test_classifySeniorGetResults(self):
        testClassify = LogisticRegressionClassifyClassStatusFromPreviouslyUntrainedModel(classStatus='Senior',
                                                                                         trainingPercentage=0.8)
        testClassify.trainTestAndGetResults()

    def test_classifyMastersLevelGraduateGetResults(self):
        testClassify = LogisticRegressionClassifyClassStatusFromPreviouslyUntrainedModel(
            classStatus='Masters Level Graduate', trainingPercentage=0.8)
        testClassify.trainTestAndGetResults()

    def test_classifyHighSchoolSeniorGetResults(self):
        testClassify = LogisticRegressionClassifyClassStatusFromPreviouslyUntrainedModel(
            classStatus='High School Senior', trainingPercentage=0.8)
        testClassify.trainTestAndGetResults()

    def test_classifyFreshmanGetResults(self):
        testClassify = LogisticRegressionClassifyClassStatusFromPreviouslyUntrainedModel(classStatus='Freshman',
                                                                                         trainingPercentage=0.8)
        testClassify.trainTestAndGetResults()


if __name__ == '__main__':
    unittest.main()
