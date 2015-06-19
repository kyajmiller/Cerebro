import unittest
from Classes.SATScore import SATScore

class TestStringMethods(unittest.TestCase):
    def test_SATScore(self):
        testsatscore = SATScore('I got a 1600 on my SAT in high school.')
        self.assertIsNotNone(testsatscore)
        self.assertEqual(testsatscore.checkContext('sat|sat\sscore'), True)
        self.assertEqual(testsatscore.getSATScore(), ['1600'])

        failsatscore = SATScore('I got a 36 on my ACT test!')
        self.assertIsNotNone(failsatscore)
        self.assertEqual(failsatscore.checkContext('sat|sat\sscore'), False)
        self.assertNotEqual(failsatscore.getSATScore(), ['36'])
        self.assertEqual(failsatscore.getSATScore(), [])

        notarealsatscore = SATScore('89 is not a real SAT score.')
        self.assertIsNotNone(notarealsatscore)
        self.assertEqual(notarealsatscore.checkContext('sat|sat\sscore'), True)
        self.assertNotEqual(notarealsatscore.getSATScore(), ['89'])


if __name__ == '__main__':
    unittest.main()