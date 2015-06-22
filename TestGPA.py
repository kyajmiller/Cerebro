import unittest
from Classes.GPA import GPA


class TestStringMethods(unittest.TestCase):
    def test_GPA(self):
        testgpa = GPA('The GPA is 3.159 not 5.304', '1')
        self.assertIsNotNone(testgpa)
        self.assertEqual(True, testgpa.checkContext('gpa|grade\spoint\saverage|maintain'))
        self.assertEqual('3.159', testgpa.getGPA())

    def test_GPAfailure(self):
        failgpa = GPA("This is not the GPA you're looking for 7.4", '1')
        self.assertIsNotNone(failgpa)
        self.assertEqual(True, failgpa.checkContext('gpa|grade\spoint\saverage|maintain'))
        self.assertNotEqual('7.4', failgpa.getGPA())
        self.assertEqual('', failgpa.getGPA())

    def test_GPAvsDollarSign(self):
        testGPANoDollarSign = GPA('$3.50 is money, but 3.49 is a GPA', '1')
        self.assertIsNotNone(testGPANoDollarSign)
        self.assertEqual(True, testGPANoDollarSign.checkContext('gpa|grade\spoint\saverage|maintain'))
        self.assertNotEqual('3.50', testGPANoDollarSign.getGPA())
        self.assertEqual('3.49', testGPANoDollarSign.getGPA())

    def test_GPACreateSPRFClass(self):
        testSPRFforGPA = GPA('This is to test the SPRF function for the grade point average of 2.9', '1543')
        self.assertIsNotNone(testSPRFforGPA)
        self.assertEqual(True, testSPRFforGPA.checkContext('gpa|grade\spoint\saverage|maintain'))
        self.assertEqual('2.9', testSPRFforGPA.getGPA())
        self.assertIsNotNone(testSPRFforGPA.getScholarshipPackageRequirementFormat())
        test_SPRF = testSPRFforGPA.getScholarshipPackageRequirementFormat()
        self.assertEqual('1543', test_SPRF.scholarshipPackageId)
        self.assertEqual('1', test_SPRF.attributeId)
        self.assertEqual('>=', test_SPRF.requirementType)
        self.assertEqual('2.9', test_SPRF.requirementValue)
        self.assertEqual('0', test_SPRF.logicGroup)

    def test_updateLogicGroup(self):
        testUpdateLogicGroup = GPA('Undergraduates must have a 3.0 GPA, while graduate students must have a 3.25', '5')
        self.assertIsNotNone(testUpdateLogicGroup)
        testUpdateLogicGroup.updateLogicGroup()
        self.assertEqual('1', testUpdateLogicGroup.logicGroup)
        test_SPRFLogicGroup = testUpdateLogicGroup.getScholarshipPackageRequirementFormat()
        self.assertEqual('1', test_SPRFLogicGroup.logicGroup)

    def test_GPAWithoutGPAKeywords(self):
        testGPANoKeywords = GPA('Must have a 3.80', '5')
        self.assertIsNotNone(testGPANoKeywords)
        self.assertEqual(False, testGPANoKeywords.checkContext('gpa|grade\spoint\saverage|maintain'))
        self.assertEqual(False, testGPANoKeywords.checkContext('million|billion|trillion|version|dollar|pound|euro'))
        self.assertEqual('3.80', testGPANoKeywords.getGPA())
        failGPANoKeywords = GPA('Must have 3.80 million dollars', '5')
        self.assertIsNotNone(failGPANoKeywords)
        self.assertEqual(False, failGPANoKeywords.checkContext('gpa|grade\spoint\saverage|maintain'))
        self.assertEqual(True, failGPANoKeywords.checkContext('million|billion|trillion|version|dollar|pound|euro'))
        self.assertEqual('', failGPANoKeywords.getGPA())


if __name__ == '__main__':
    unittest.main()
