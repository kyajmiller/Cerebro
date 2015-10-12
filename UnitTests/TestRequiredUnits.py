import unittest
from Classes.RequiredUnits import RequiredUnits

class TestStringMethods(unittest.TestCase):
    def test_RequiredUnits(self):
        testrequiredunits = RequiredUnits('Have a minimum of 60 units in the major')
        self.assertIsNotNone(testrequiredunits)
        self.assertEqual(True, testrequiredunits.checkContext('units?'))
        self.assertEqual(['60'], testrequiredunits.getRequiredUnits())

    def test_RequiredUnitsFailure(self):
        failrequiredunits = RequiredUnits('It is 110 degrees outside today.')
        self.assertIsNotNone(failrequiredunits)
        self.assertEqual(False, failrequiredunits.checkContext('units?'))
        self.assertNotEqual(['110'], failrequiredunits.getRequiredUnits())
        self.assertEqual([], failrequiredunits.getRequiredUnits())


if __name__ == '__main__':
    unittest.main()