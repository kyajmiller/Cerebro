import unittest
from ClassStandingClassifierStuff.ClassifyClassStatusFromPreviouslyUntrainedModel import ClassifyClassStatusTrainFirst


class TestStringMethods(unittest.TestCase):
    def test_classifyJuniorGetResults(self):
        testClassify = ClassifyClassStatusTrainFirst(classStatus='Junior', trainingPercentage=0.8)
        testClassify.trainTestAndGetResults()

    def test_classifySeniorGetResults(self):
        testClassify = ClassifyClassStatusTrainFirst(classStatus='Senior', trainingPercentage=0.8)
        testClassify.trainTestAndGetResults()

    def test_classifyMastersLevelGraduateGetResults(self):
        testClassify = ClassifyClassStatusTrainFirst(classStatus='Masters Level Graduate', trainingPercentage=0.8)
        testClassify.trainTestAndGetResults()

    def test_classifyHighSchoolSeniorGetResults(self):
        testClassify = ClassifyClassStatusTrainFirst(classStatus='High School Senior', trainingPercentage=0.8)
        testClassify.trainTestAndGetResults()


if __name__ == '__main__':
    unittest.main()
