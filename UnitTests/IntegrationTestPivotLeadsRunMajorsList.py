import unittest
from Classes.PivotLeadsRunMajorsList import PivotLeadsRunMajorsList
from Classes.SUDBConnect import SUDBConnect


class TestStringMethods(unittest.TestCase):
    '''
    def test_PivotLeadsRunMajorsList(self):
        # set up
        db = SUDBConnect()

        # run
        PivotLeadsRunMajorsList(isTest=True)

        # test
        rows = db.getRows("select * from dbo.PivotLeads")
        self.assertGreaterEqual(len(rows), 100)
    '''
    def test_PivotLeadsRunMajorsListActuallyDoIt(self):
        # set up
        db = SUDBConnect()

        # run
        PivotLeadsRunMajorsList()

        # test
        rows = db.getRows("select * from dbo.PivotLeads")
        self.assertGreaterEqual(len(rows), 100)


if __name__ == '__main__':
    unittest.main()
