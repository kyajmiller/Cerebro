import unittest
from Classes.IefaLeads import IefaLeads


class TestStringMethods(unittest.TestCase):
    def test_IefaLeads(self):
        testIefaLeads = IefaLeads(isTest=True).loopOverResultsPagesAndDoStuff()
        self.assertIsNotNone(testIefaLeads)
        firstArray = testIefaLeads[0]
        self.assertEqual(len(firstArray), 15)


if __name__ == '__main__':
    unittest.main()
