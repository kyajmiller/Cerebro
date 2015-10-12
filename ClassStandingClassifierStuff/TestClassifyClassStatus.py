import unittest
from ClassStandingClassifierStuff.ClassifyClassStatus import ClassifyClassStatus


class TestStringMethods(unittest.TestCase):
    def test_classifyJuniorGetResults(self):
        testClassify = ClassifyClassStatus(classStatus='Junior', trainingPercentage=0.8)
        testClassify.trainTestAndGetResults()

    def test_classifySeniorGetResults(self):
        testClassify = ClassifyClassStatus(classStatus='Senior', trainingPercentage=0.8)
        testClassify.trainTestAndGetResults()

    def test_classifyMastersLevelGraduateGetResults(self):
        testClassify = ClassifyClassStatus(classStatus='Masters Level Graduate', trainingPercentage=0.8)
        testClassify.trainTestAndGetResults()

    def test_classifyHighSchoolSeniorGetResults(self):
        testClassify = ClassifyClassStatus(classStatus='High School Senior', trainingPercentage=0.8)
        testClassify.trainTestAndGetResults()


if __name__ == '__main__':
    unittest.main()
