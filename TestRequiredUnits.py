import unittest
from Classes.RequiredUnits import RequiredUnits

class TestStringMethods(unittest.TestCase):
    def test_RequiredUnits(self):
        testrequiredunits = RequiredUnits('Have a minimum of 60 units in the major')
        self.assertIsNotNone(testrequiredunits)
        self.assertEqual(testrequiredunits.checkContext('units?'), True)
        self.assertEqual(testrequiredunits.getRequiredUnits(), ['60'])

        failrequiredunits = RequiredUnits('It is 110 degrees outside today.')
        self.assertIsNotNone(failrequiredunits)
        self.assertEqual(failrequiredunits.checkContext('units?'), False)
        self.assertNotEqual(failrequiredunits.getRequiredUnits(), ['110'])
        self.assertEqual(failrequiredunits.getRequiredUnits(), [])


if __name__ == '__main__':
    unittest.main()