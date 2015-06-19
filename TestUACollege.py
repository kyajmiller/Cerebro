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
        self.assertEqual(testuacollege.checkContext('college|college\sof|school\sof'), True)
        self.assertEqual(testuacollege.getUACollege(), ['social and behavioral science'])

        failuacollege = UACollege('Majoring in optical science', UAColleges)
        self.assertIsNotNone(failuacollege)
        self.assertEqual(failuacollege.checkContext('college|college\sof|school\sof'), False)
        self.assertNotEqual(failuacollege.getUACollege(), ['optical science'])
        self.assertEqual(failuacollege.getUACollege(), [])


if __name__ == '__main__':
    unittest.main()
