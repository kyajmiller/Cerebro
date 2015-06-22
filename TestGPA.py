import unittest
from Classes.GPA import GPA


class TestStringMethods(unittest.TestCase):
    def test_GPA(self):
        testgpa = GPA('The GPA is 3.159 not 5.304', '1')
        self.assertIsNotNone(testgpa)
        self.assertEqual(testgpa.checkContext('gpa|grade\spoint\saverage|maintain'), True)
        self.assertEqual(testgpa.getGPA(), '3.159')

    def test_GPAfailure(self):
        failgpa = GPA("This is not the GPA you're looking for 7.4", '1')
        self.assertIsNotNone(failgpa)
        self.assertEqual(failgpa.checkContext('gpa|grade\spoint\saverage|maintain'), True)
        self.assertNotEqual(failgpa.getGPA(), '7.4')
        self.assertEqual(failgpa.getGPA(), '')

    def test_GPAvsDollarSign(self):
        testGPANoDollarSign = GPA('$3.50 is money, but 3.49 is a GPA', '1')
        self.assertIsNotNone(testGPANoDollarSign)
        self.assertEqual(testGPANoDollarSign.checkContext('gpa|grade\spoint\saverage|maintain'), True)
        self.assertNotEqual(testGPANoDollarSign.getGPA(), '3.50')
        self.assertEqual(testGPANoDollarSign.getGPA(), '3.49')

    def test_GPACreateSPRFClass(self):
        testSPRFforGPA = GPA('This is to test the SPRF function for the grade point average of 2.9', '1543')
        self.assertIsNotNone(testSPRFforGPA)
        self.assertEqual(testSPRFforGPA.checkContext('gpa|grade\spoint\saverage|maintain'), True)
        self.assertEqual(testSPRFforGPA.getGPA(), '2.9')
        self.assertIsNotNone(testSPRFforGPA.getScholarshipPackageRequirementFormat())
        test_SPRF = testSPRFforGPA.getScholarshipPackageRequirementFormat()
        self.assertEqual('1543', test_SPRF.scholarshipPackageId)
        self.assertEqual('1', test_SPRF.attributeId)
        self.assertEqual('>=', test_SPRF.requirementType)
        self.assertEqual('2.9', test_SPRF.requirementValue)
        self.assertEqual('0', test_SPRF.logicGroup)



if __name__ == '__main__':
    unittest.main()
