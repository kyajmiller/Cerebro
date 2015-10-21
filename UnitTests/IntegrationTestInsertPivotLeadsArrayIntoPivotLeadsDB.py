import unittest
from Classes.SUDBConnect import SUDBConnect
from Classes.InsertPivotLeadsArrayIntoPivotLeadsDB import InsertPivotLeadsArrayIntoPivotLeadsDB


class TestStringMethods(unittest.TestCase):
    def test_InsertPivotLeadsArrayIntoPivotLeadsDB(self):
        fakepivotleadsarray = ['keyword', 'url', 'name', 'abstract', 'sponsor', 'amount', 'applicant type',
                               'citizenship residency', 'activity location', 'eligibility', 'categories',
                               'source website', 'source text']
        InsertPivotLeadsArrayIntoPivotLeadsDB(fakepivotleadsarray)

        db = SUDBConnect()
        rows = db.getRows("select * from dbo.PivotLeads where Url='url'")
        self.assertIsNotNone(rows)

        self.assertEqual('keyword', rows[0].Keyword)
        self.assertEqual('url', rows[0].Url)
        self.assertEqual('name', rows[0].Name)
        self.assertEqual('abstract', rows[0].Abstract)
        self.assertEqual('sponsor', rows[0].Sponsor)
        self.assertEqual('amount', rows[0].Amount)
        self.assertEqual('applicant type', rows[0].ApplicantType)
        self.assertEqual('citizenship residency', rows[0].CitizenshipResidency)
        self.assertEqual('activity location', rows[0].ActivityLocation)
        self.assertEqual('eligibility', rows[0].Eligibility)
        self.assertEqual('categories', rows[0].Categories)
        self.assertEqual('source website', rows[0].SourceWebsite)
        self.assertEqual('source text', rows[0].SourceText)

        db.insertUpdateOrDelete("delete from dbo.PivotLeads where Url='url'")


if __name__ == '__main__':
    unittest.main()
