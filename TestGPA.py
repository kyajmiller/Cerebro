import unittest
from Classes.GPA import GPA


class TestStringMethods(unittest.TestCase):
    def test_GPA(self):
        testgpa = GPA('The GPA is 3.159 not 5.304')
        self.assertIsNotNone(testgpa)
        self.assertEqual(testgpa.checkContext('gpa|grade\spoint\saverage|maintain'), True)
        self.assertEqual(testgpa.getGPA(), '3.159')

        failgpa = GPA("This is not the GPA you're looking for 7.4")
        self.assertIsNotNone(failgpa)
        self.assertEqual(failgpa.checkContext('gpa|grade\spoint\saverage|maintain'), True)
        self.assertNotEqual(failgpa.getGPA(), '7.4')
        self.assertEqual(failgpa.getGPA(), '')

        testSPRFforGPA = GPA('This is to test the SPRF function for the grade point average of 2.9')
        self.assertIsNotNone(testSPRFforGPA)
        self.assertEqual(testSPRFforGPA.checkContext('gpa|grade\spoint\saverage|maintain'), True)
        self.assertEqual(testSPRFforGPA.getGPA(), '2.9')
        self.assertEqual(testSPRFforGPA.getScholarshipPackageRequirementFormat(),
                         'AttributeId = 1, RequirementTypeCode = >=, RequirementValue = 2.9, LogicGroup = 0')


if __name__ == '__main__':
    unittest.main()
