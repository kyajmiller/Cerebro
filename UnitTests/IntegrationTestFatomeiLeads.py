import unittest
from Classes.FatomeiLeads import FatomeiLeads


class TestStringMethods(unittest.TestCase):
    def test_FatomeiLeads(self):
        testFatomeiLeads = FatomeiLeads(isTest=True)
        self.assertIsNotNone(testFatomeiLeads)
        firstArray = testFatomeiLeads.getFatomeiLeadsArrays()[0]
        self.assertEqual(len(firstArray), 5)


if __name__ == '__main__':
    unittest.main()
