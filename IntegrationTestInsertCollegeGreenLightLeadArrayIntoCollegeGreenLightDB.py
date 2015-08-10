import unittest
from Classes.InsertCollegeGreenLightLeadArrayIntoCollegeGreenLightDB import \
    InsertCollegeGreenLightLeadArrayIntoCollegeGreenLightDB
from Classes.SUDBConnect import SUDBConnect


class TestStringMethods(unittest.TestCase):
    def test_InsertCollegeGreenLightLeadArrayIntoCollegeGreenLightDB(self):
        # set up
        fakeLeadArray = ['name', 'amount', 'deadline', 'sponsor', 'description', 'requirements', 'url', 'sourceWebsite',
                         'sourceText']
        db = SUDBConnect()
        db.insertUpdateOrDelete("delete from dbo.CollegeGreenLightLeads where Name='name'")

        # test
        InsertCollegeGreenLightLeadArrayIntoCollegeGreenLightDB(fakeLeadArray)
        row = db.getRows("select * from dbo.CollegeGreenLightLeads where Name='name'")
        testRow = row[0]
        self.assertEqual('name', testRow.Name)
        self.assertEqual('amount', testRow.Amount)
        self.assertEqual('deadline', testRow.Deadline)
        self.assertEqual('sponsor', testRow.Sponsor)
        self.assertEqual('description', testRow.Description)
        self.assertEqual('requirements', testRow.Requirements)
        self.assertEqual('url', testRow.Url)
        self.assertEqual('sourceWebsite', testRow.SourceWebsite)
        self.assertEqual('sourceText', testRow.SourceText)

        # tear down
        db.insertUpdateOrDelete("delete from dbo.CollegeGreenLightLeads where Name='name'")


if __name__ == '__main__':
    unittest.main()
