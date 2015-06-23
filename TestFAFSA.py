import unittest
from Classes.FAFSA import FAFSA

class TestStringMethods(unittest.TestCase):
    def test_FAFSA(self):
        testfafsa = FAFSA('Need to have a completed FAFSA')
        self.assertIsNotNone(testfafsa)
        self.assertEqual(testfafsa.getFAFSA(), ['yes'])

    def test_FAFSAFailure(self):
        failfafsa = FAFSA('This string does not talk about financial aid.')
        self.assertIsNotNone(failfafsa)
        self.assertNotEqual(failfafsa.getFAFSA(), ['yes'])
        self.assertEqual(failfafsa.getFAFSA(), [])


if __name__ == '__main__':
    unittest.main()