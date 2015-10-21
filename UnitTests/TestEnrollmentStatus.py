import unittest
from Classes.EnrollmentStatus import EnrollmentStatus

class TestStringMethods(unittest.TestCase):
    def test_EnrollmentStatus(self):
        testenrollmentstatus = EnrollmentStatus('I am enrolled full-time at the UA.')
        self.assertIsNotNone(testenrollmentstatus)
        self.assertEqual(testenrollmentstatus.checkContext('enroll|study'), True)
        self.assertEqual(testenrollmentstatus.getEnrollmentStatus(), ['full-time'])

    def test_EnrollmentStatusFailure(self):
        failenrollmentstatus = EnrollmentStatus('I have a part time job.')
        self.assertIsNotNone(failenrollmentstatus)
        self.assertEqual(failenrollmentstatus.checkContext('enroll|study'), False)
        self.assertEqual(failenrollmentstatus.checkContext('job|work|employ'), True)
        self.assertNotEqual(failenrollmentstatus.getEnrollmentStatus(), ['part time'])
        self.assertEqual(failenrollmentstatus.getEnrollmentStatus(), [])


if __name__ == '__main__':
    unittest.main()