import unittest
from Classes.SATScore import SATScore

class TestStringMethods(unittest.TestCase):
    def test_SATScore(self):
        testsatscore = SATScore('I got a 1600 on my SAT in high school.')
        self.assertIsNotNone(testsatscore)
        self.assertEqual(True, testsatscore.checkContext('sat|sat\sscore'))
        self.assertEqual(['1600'], testsatscore.getSATScore())

    def test_SATScoreContextFailure(self):
        failsatscore = SATScore('I got a 36 on my ACT test!')
        self.assertIsNotNone(failsatscore)
        self.assertEqual(False, failsatscore.checkContext('sat|sat\sscore'))
        self.assertNotEqual(['36'], failsatscore.getSATScore())
        self.assertEqual([], failsatscore.getSATScore())

    def test_SATScoreValueFailure(self):
        notarealsatscore = SATScore('89 is not a real SAT score.')
        self.assertIsNotNone(notarealsatscore)
        self.assertEqual(True, notarealsatscore.checkContext('sat|sat\sscore'))
        self.assertNotEqual(['89'], notarealsatscore.getSATScore())


if __name__ == '__main__':
    unittest.main()