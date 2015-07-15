import unittest
from Classes.GetFastFindMajorsList import GetFastFindMajorsList


class TestStringMethods(unittest.TestCase):
    def test_GetFastFindMajorsList(self):
        testfastfindmajorslist = GetFastFindMajorsList.getList()
        self.assertGreaterEqual(len(testfastfindmajorslist), 100)


if __name__ == '__main__':
    unittest.main()
