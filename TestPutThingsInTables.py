import unittest
from Classes.PutThingsInTables import PutThingsInTables
from Classes.SUDBConnect import SUDBConnect


class TestStringMethods(unittest.TestCase):
    def test_PutThingsInTables(self):
        # setup
        testQuery = PutThingsInTables('Tests', ['testquery', 8], ['Regex', 'AttributeId']).createSQLQuery()
        self.assertIsNotNone("%s" % testQuery)

        # test
        db = SUDBConnect()
        db.insertUpdateOrDelete(testQuery)

        rows = db.getRows("select * from dbo.Tests where Regex='testquery'")
        testRegexValue = rows[0].Regex
        self.assertEqual('testquery', testRegexValue)

        # tear down
        db.insertUpdateOrDelete("delete from dbo.Tests where Regex='testquery'")


if __name__ == '__main__':
    unittest.main()
