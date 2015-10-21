import unittest
from Classes.ScholarsiteLeads import ScholarsiteLeads


class TestStringMethods(unittest.TestCase):
    def test_ScholarsiteLeads(self):
        testScholarsiteLeads = ScholarsiteLeads(isTest=True)
        self.assertIsNotNone(testScholarsiteLeads)
        firstArray = testScholarsiteLeads.processResultsPages()[0]
        self.assertEqual(len(firstArray), 19)


if __name__ == '__main__':
    unittest.main()
