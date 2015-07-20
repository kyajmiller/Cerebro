import unittest
from Classes.GetFastFindMajorsList import GetFastFindMajorsList


class TestStringMethods(unittest.TestCase):
    def test_GetFastFindMajorsList(self):
        testfastfindmajorslist = GetFastFindMajorsList.getDefaultList()
        self.assertGreaterEqual(len(testfastfindmajorslist), 100)
        print(testfastfindmajorslist)

    def test_GetFastFindMajorsListGrantForwardItems(self):
        testgrantforwardmajorslist = GetFastFindMajorsList.getGrantForwardItemsList()
        self.assertGreaterEqual(len(testgrantforwardmajorslist), 100)
        print(testgrantforwardmajorslist)

    def test_CompareLists(self):
        testdefault = GetFastFindMajorsList.getDefaultList()
        testgf = GetFastFindMajorsList.getGrantForwardItemsList()
        testpivot = GetFastFindMajorsList.getPivotLeadsList()

        print(testdefault)
        print(testpivot)
        print(testgf)


if __name__ == '__main__':
    unittest.main()
