import unittest
from Classes.EmploymentStatus import EmploymentStatus

class TestStringMethods(unittest.TestCase):
    def test_EmploymentStatus(self):
        testemploymentstatus = EmploymentStatus('Must be working a full time job')
        self.assertIsNotNone(testemploymentstatus)
        self.assertEqual(testemploymentstatus.checkContext('work|employ|job'), True)
        self.assertEqual(testemploymentstatus.getEmploymentStatus(), ['full time'])

        testemploymentstatushours = EmploymentStatus('Must be working 20 hours a week')
        self.assertIsNotNone(testemploymentstatushours)
        self.assertEqual(testemploymentstatushours.checkContext('work|employ|job'), True)
        self.assertEqual(testemploymentstatushours.checkContext('hour'), True)
        self.assertEqual(testemploymentstatushours.getEmploymentStatus(), ['20 Hours'])

        failemploymentstatus = EmploymentStatus('I am enrolled full-time at the UA.')
        self.assertIsNotNone(failemploymentstatus)
        self.assertEqual(failemploymentstatus.checkContext('work|employ|job'), False)
        self.assertNotEqual(failemploymentstatus.getEmploymentStatus(), ['full-time'])
        self.assertEqual(failemploymentstatus.getEmploymentStatus(), [])


if __name__ == '__main__':
    unittest.main()