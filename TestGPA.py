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

        testGPANoDollarSign = GPA('$3.50 is money, but 3.49 is a GPA')
        self.assertIsNotNone(testGPANoDollarSign)
        self.assertEqual(testGPANoDollarSign.checkContext('gpa|grade\spoint\saverage|maintain'), True)
        self.assertNotEqual(testGPANoDollarSign.getGPA(), '3.50')
        self.assertEqual(testGPANoDollarSign.getGPA(), '3.49')
        testSPRFforGPA = GPA('This is to test the SPRF function for the grade point average of 2.9')
        self.assertIsNotNone(testSPRFforGPA)
        self.assertEqual(testSPRFforGPA.checkContext('gpa|grade\spoint\saverage|maintain'), True)
        self.assertEqual(testSPRFforGPA.getGPA(), '2.9')
       # self.assertIsNotNone(testSPRFforGPA.getScholarshipPackageRequirementFormat())
      #  spr=testSPRFforGPA.getScholarshipPackageRequirementFormat()
       # self.assertEqual("2.9",spr.requirementValue)
       # self.assertEqual(">=",spr.requirementType)


if __name__ == '__main__':
    unittest.main()
