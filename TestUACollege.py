import unittest
from Classes.UACollege import UACollege

UAColleges = ['Agriculture & Life Sciences', 'Agriculture and Life Sciences',
              'Architecture, Planning & Landscape Architecture',
              'Architecture Planning and Landscape Architecture', 'Education', 'Engineering', 'Fine Arts', 'Humanities',
              'Medicine', 'Nursing', 'Optical Science', 'Pharmacy', 'Science', 'Social and Behavioral Sciences',
              'Letters, Arts and Science',
              'Management', 'Eller', 'Honors', 'Law', 'James E. Rogers', 'Public Health', 'Outreach College',
              'Graduate College', 'School of Art', 'Landscape Architecture', 'SNRE', 'COM']

UAColleges = '|'.join(UAColleges)


class TestStringMethods(unittest.TestCase):
    def test_UACollege(self):
        testuacollege = UACollege('I am in the College of Social and Behavioral Sciences.', '2', UAColleges)
        self.assertIsNotNone(testuacollege)
        self.assertEqual(True, testuacollege.checkContext('college|college\sof|school\sof'))
        self.assertEqual('Social and Behavioral Sciences', testuacollege.getUACollege())

    def test_UACollegeFailure(self):
        failuacollege = UACollege('Majoring in optical science', '3', UAColleges)
        self.assertIsNotNone(failuacollege)
        self.assertEqual(False, failuacollege.checkContext('college|college\sof|school\sof'))
        self.assertNotEqual('optical science', failuacollege.getUACollege())
        self.assertEqual('', failuacollege.getUACollege())

    def test_UACollegeCreateSPRFClass(self):
        testSPRFforUACollege = UACollege(
            'This is to test the SPRF function for the UA College of Agriculture and Life Sciences', '1543', UAColleges)
        self.assertIsNotNone(testSPRFforUACollege)
        self.assertEqual(True, testSPRFforUACollege.checkContext('college|college\sof|school\sof'))
        self.assertEqual('Agriculture and Life Sciences', testSPRFforUACollege.getUACollege())
        self.assertIsNotNone(testSPRFforUACollege.getScholarshipPackageRequirementFormat())
        test_SPRF = testSPRFforUACollege.getScholarshipPackageRequirementFormat()
        self.assertEqual('1543', test_SPRF.scholarshipPackageId)
        self.assertEqual('377', test_SPRF.attributeId)
        self.assertEqual('*', test_SPRF.requirementType)
        self.assertEqual('Agriculture and Life Sciences', test_SPRF.requirementValue)
        self.assertEqual('0', test_SPRF.logicGroup)

if __name__ == '__main__':
    unittest.main()
