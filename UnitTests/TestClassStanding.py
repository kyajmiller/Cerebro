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

    def test_ClassStandingYear(self):
        testclassstandingyear = ClassStanding('Must be a 3rd year student', ClassStandingOptions)
        self.assertIsNotNone(testclassstandingyear)
        self.assertEqual(testclassstandingyear.getClassStanding(), ['3rd Year'])

    def test_ClassStandingContextBased(self):
        testclassstandingcontext = ClassStanding('I am a masters student', ClassStandingOptions)
        self.assertIsNotNone(testclassstandingcontext)
        self.assertEqual(testclassstandingcontext.checkClassStandingOptions(), None)
        self.assertEqual(testclassstandingcontext.checkMastersStudent(), ['masters level graduate'])
        self.assertEqual(testclassstandingcontext.getClassStanding(), ['masters level graduate'])

    def test_ClassStandingContextIgnoreCase(self):
        testcsignorecase = ClassStanding('HE IS A PHD STUDENT', ClassStandingOptions)
        self.assertIsNotNone(testcsignorecase)
        self.assertEqual(testcsignorecase.getClassStanding(), ['ph.d. level graduate'])


if __name__ == '__main__':
    unittest.main()