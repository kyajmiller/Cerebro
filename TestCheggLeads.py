import unittest
from Classes.CheggLeads import CheggLeads


class TestStringMethods(unittest.TestCase):
    def test_IefaLeads(self):
        testCheggLeads = CheggLeads().loopOverResultsPagesAndDoStuff()
        self.assertIsNotNone(testCheggLeads)
        firstArray = testCheggLeads[0]
        self.assertEqual(len(firstArray), 10)


if __name__ == '__main__':
    unittest.main()
