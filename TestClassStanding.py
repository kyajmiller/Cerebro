import unittest
from Classes.ClassStanding import ClassStanding

ClassStandingOptions = ['high school senior', 'freshman', 'sophomore', 'junior', 'senior', 'masters level graduate',
                        'ph.d. level graduate', 'non-degree seeking graduate', 'law school student',
                        'medical school student', 'nursing school student', 'graduate student'
                        'doctor of nursing practice', 'dnp', 'post-baccalaureate', 'postdoctoral', 'undergraduate']

ClassStandingOptions = '|'.join(ClassStandingOptions)

class TestStringMethods(unittest.TestCase):
    def test_ClassStanding(self):
        testclassstanding = ClassStanding('Must be a college junior', ClassStandingOptions)
        self.assertIsNotNone(testclassstanding)
        self.assertEqual(testclassstanding.checkContext('must'), True)
        self.assertEqual(testclassstanding.getClassStanding(), ['junior'])

        testcsagain = ClassStanding('Must be a 3rd year student', ClassStandingOptions)
        self.assertIsNotNone(testcsagain)
        self.assertEqual(testcsagain.getClassStanding(), ['3rd Year'])

        morecstesting = ClassStanding('I am a masters student', ClassStandingOptions)
        self.assertIsNotNone(morecstesting)
        self.assertEqual(morecstesting.checkClassStandingOptions(), None)
        self.assertEqual(morecstesting.checkMastersStudent(), ['masters level graduate'])
        self.assertEqual(morecstesting.getClassStanding(), ['masters level graduate'])

        testcsignorecase = ClassStanding('HE IS A PHD STUDENT', ClassStandingOptions)
        self.assertIsNotNone(testcsignorecase)
        self.assertEqual(testcsignorecase.getClassStanding(), ['ph.d. level graduate'])


if __name__ == '__main__':
    unittest.main()