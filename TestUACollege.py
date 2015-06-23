import unittest
from Classes.UACollege import UACollege

UAColleges = ['agriculture & life sciences', 'agriculture and life sciences',
              'architecture, planning & landscape architecture',
              'architecture planning and landscape architecture', 'education', 'engineering', 'fine arts', 'humanities',
              'medicine', 'nursing', 'optical science', 'pharmacy', 'science', 'social and behavioral science',
              'letters, arts and science',
              'management', 'eller', 'honors', 'law', 'james e. rogers', 'public health', 'outreach college',
              'graduate college', 'school of art', 'landscape architecture', 'snre']

UAColleges = '|'.join(UAColleges)


class TestStringMethods(unittest.TestCase):
    def test_UACollege(self):
        testuacollege = UACollege('I am in the College of Social and Behavioral Sciences.', UAColleges)
        self.assertIsNotNone(testuacollege)
        self.assertEqual(True, testuacollege.checkContext('college|college\sof|school\sof'))
        self.assertEqual(['social and behavioral science'], testuacollege.getUACollege())

    def test_UACollegeFailure(self):
        failuacollege = UACollege('Majoring in optical science', UAColleges)
        self.assertIsNotNone(failuacollege)
        self.assertEqual(False, failuacollege.checkContext('college|college\sof|school\sof'))
        self.assertNotEqual(['optical science'], failuacollege.getUACollege())
        self.assertEqual([], failuacollege.getUACollege())


if __name__ == '__main__':
    unittest.main()
