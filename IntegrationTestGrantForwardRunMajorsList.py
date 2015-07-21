import unittest
from Classes.GrantForwardRunMajorsList import GrantForwardRunMajorsList
from Classes.SUDBConnect import SUDBConnect

class TestStringMethods(unittest.TestCase):
    '''
    def test_GrantForwardRunMajorsList(self):
        #set up
        db = SUDBConnect()

        #run
        GrantForwardRunMajorsList(isTest=True)

        #test
        rows = db.getRows("select * from dbo.GrantForwardItems")
        self.assertGreaterEqual(len(rows), 100)
    '''

    def test_GrantForwardRunMajorsListActuallyDoIt(self):
        # set up
        db = SUDBConnect()

        # run
        GrantForwardRunMajorsList()

        # test
        rows = db.getRows("select * from dbo.GrantForwardItems")
        self.assertGreaterEqual(len(rows), 100)


if __name__ == '__main__':
    unittest.main()