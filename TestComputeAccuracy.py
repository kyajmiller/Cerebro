import unittest
from Classes.ComputeAccuracy import ComputeAccuracy


class TestStringMethods(unittest.TestCase):
    def test_ComputeAccuracy100(self):
        expectedList = ['cheese', 'eggs', 'potatoes', 'bacon', 'cheese']
        predictedList = ['cheese', 'eggs', 'potatoes', 'bacon', 'cheese']
        accuracy = ComputeAccuracy(expectedList, predictedList).calculateAccuracy()
        self.assertEqual(100.0, accuracy)

    def test_ComputeAccuracyNotPerfect(self):
        expectedList = ['cheese', 'eggs', 'potatoes', 'bacon', 'cheese']
        predictedList = ['cheese', 'hollandaise', 'potatoes', 'sausage', 'cheese']
        accuracy = ComputeAccuracy(expectedList, predictedList).calculateAccuracy()
        self.assertGreater(100.0, accuracy)


if __name__ == '__main__':
    unittest.main()
