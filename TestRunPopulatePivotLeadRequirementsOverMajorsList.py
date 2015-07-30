import unittest
from Classes.RunPopulatePivotLeadRequirementsOverMajorsList import RunPopulatePivotLeadRequirementsOverMajorsList


class TestStringMethods(unittest.TestCase):
    def test_getMajorsList(self):
        testAllMajors = RunPopulatePivotLeadRequirementsOverMajorsList(numberOfMajors='All').getMajorsList()
        self.assertGreater(len(testAllMajors), 75)

        testSomeMajors = RunPopulatePivotLeadRequirementsOverMajorsList(numberOfMajors=5).getMajorsList()
        self.assertEqual(len(testSomeMajors), 5)


if __name__ == '__main__':
    unittest.main()
