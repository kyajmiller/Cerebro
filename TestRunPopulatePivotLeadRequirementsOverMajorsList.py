import unittest
from Classes.LoopPopulatePivotLeadRequirementsOverMajorsList import LoopPopulatePivotLeadRequirementsOverMajorsList


class TestStringMethods(unittest.TestCase):
    def test_getMajorsList(self):
        testAllMajors = LoopPopulatePivotLeadRequirementsOverMajorsList(numberOfMajors='All').getMajorsList()
        self.assertGreater(len(testAllMajors), 75)

        testSomeMajors = LoopPopulatePivotLeadRequirementsOverMajorsList(numberOfMajors=5).getMajorsList()
        self.assertEqual(len(testSomeMajors), 5)


if __name__ == '__main__':
    unittest.main()
