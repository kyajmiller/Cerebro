import unittest
from Classes.InsertGrantForwardLeadsArrayIntoGrantForwardItems import InsertGrantForwardLeadsArrayIntoGrantForwardItems
from Classes.SUDBConnect import SUDBConnect


class TestStringMethods(unittest.TestCase):
    def test_InsertGrantForwardLeadIntoDatabase(self):
        fakegrantforwardleadarray = ['keyword', 'url', 'name', 'description', 'sponsor', 'amount', 'eligibility',
                                     'submission info', 'categories', 'opportunity source link',
                                     'opportunity source text']
        InsertGrantForwardLeadsArrayIntoGrantForwardItems(fakegrantforwardleadarray)

        db = SUDBConnect()
        rows = db.getRows("select * from dbo.GrantForwardItems where Url='url'")
        self.assertIsNotNone(rows)
        self.assertEqual('keyword', rows[0].Keyword)
        self.assertEqual('url', rows[0].Url)
        self.assertEqual('name', rows[0].Name)
        self.assertEqual('description', rows[0].Description)
        self.assertEqual('sponsor', rows[0].Sponsor)
        self.assertEqual('eligibility', rows[0].Eligibility)
        self.assertEqual('submission info', rows[0].SubmissionInfo)
        self.assertEqual('categories', rows[0].Categories)
        self.assertEqual('opportunity source link', rows[0].OpportunitySourceLink)
        self.assertEqual('opportunity source text', rows[0].OpportunitySourceText)

        db.insertUpdateOrDelete("delete from dbo.GrantForwardItems where Url='url'")


if __name__ == '__main__':
    unittest.main()
