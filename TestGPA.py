import unittest
from Classes.GPA import GPA

class TestStringMethods(unittest.TestCase):
    def test_GPA(self):
        testgpa = GPA('The GPA is 3.159 not 5.304')
        self.assertIsNotNone(testgpa)
        self.assertEqual(testgpa.checkContext('gpa'), True)
        self.assertEqual(testgpa.getGPA(), ['3.159'])

        failgpa = GPA("This is not the GPA you're looking for 7.4")
        self.assertIsNotNone(failgpa)
        self.assertEqual(failgpa.checkContext('gpa'), True)
        self.assertNotEqual(failgpa.getGPA(), ['7.4'])
        self.assertEqual(failgpa.getGPA(), [])


if __name__ == '__main__':
    unittest.main()