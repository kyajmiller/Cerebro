import unittest
from Classes.MapDBtoSPR import MapDBtoSPR


class TestStringMethods(unittest.TestCase):
    def test_MapDBtoSPR(self):
        testMapDBtoSPR = MapDBtoSPR(
            "SELECT TOP 1 ScholarshipPackageId, Elgibility FROM dbo.DepartmentTestCases WHERE AttributeId =417")
        self.assertIsNotNone(testMapDBtoSPR)


if __name__ == '__main__':
    unittest.main()
