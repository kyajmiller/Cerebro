import unittest
from ClassStandingClassifierStuff.ClassifyClassStatus import ClassifyClassStatus


class TestStringMethods(unittest.TestCase):
    def test_classifyJuniorGetResults(self):
        testClassify = ClassifyClassStatus(classStatus='Junior', trainingPercentage=0.8)
        testClassify.trainTestAndGetResults()


if __name__ == '__main__':
    unittest.main()
