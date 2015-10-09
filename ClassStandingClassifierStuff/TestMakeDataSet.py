import unittest
import math
from ClassStandingClassifierStuff.MakeDataSetClassifyClassStatus import MakeDataSetClassifyClassStatus


class TestStringMethods(unittest.TestCase):
    def test_makeTrainingTestingSets(self):
        desiredClassStatus = 'Junior'
        setToWorkWith = MakeDataSetClassifyClassStatus(desiredClassStatus)

        trainingPercentage = 0.9
        trainingSetAndTestingSet = setToWorkWith.makeTrainingAndTestingSets(trainingPercentage)
        training = trainingSetAndTestingSet[0]
        testing = trainingSetAndTestingSet[1]
        totalSetSize = len(training) + len(testing)
        self.assertEqual(math.ceil(totalSetSize * trainingPercentage), len(training))


if __name__ == '__main__':
    unittest.main()
