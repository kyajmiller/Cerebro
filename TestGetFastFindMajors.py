import unittest
from Classes.GetFastFindMajorsList import GetFastFindMajorsList


class TestStringMethods(unittest.TestCase):
    def test_GetFastFindMajorsList(self):
        testfastfindmajorslist = GetFastFindMajorsList.getList()
        self.assertGreaterEqual(len(testfastfindmajorslist), 100)
        print(testfastfindmajorslist)

    def test_GetFastFindMajorsListGrantForwardItems(self):
        testgrantforwardmajorslist = GetFastFindMajorsList.getList('GrantForwardItems')
        self.assertGreaterEqual(len(testgrantforwardmajorslist), 100)
        print(testgrantforwardmajorslist)


if __name__ == '__main__':
    unittest.main()
