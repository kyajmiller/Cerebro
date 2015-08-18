import unittest
from Classes.PutThingsInTables import PutThingsInTables
from Classes.SUDBConnect import SUDBConnect


class TestStringMethods(unittest.TestCase):
    def test_PutThingsInTablesInsert(self):
        # setup
        testQuery = PutThingsInTables('Tests', ['Regex', 'AttributeId'], ['testquery', 8]).createSQLQueryInsert()
        self.assertIsNotNone("%s" % testQuery)

        # test
        db = SUDBConnect()
        db.insertUpdateOrDelete(testQuery)

        rows = db.getRows("select * from dbo.Tests where Regex='testquery'")
        testRegexValue = rows[0].Regex
        self.assertEqual('testquery', testRegexValue)

        # tear down
        db.insertUpdateOrDelete("delete from dbo.Tests where Regex='testquery'")

    def test_PutThingInTablesUpdate(self):
        # setup
        db = SUDBConnect()
        createTestRow = PutThingsInTables('Tests', ['Regex', 'AttributeId'],
                                          ['rowToUpdate', '94']).createSQLQueryInsert()
        db.insertUpdateOrDelete(createTestRow)
        self.assertIsNotNone("%s" % createTestRow)
        rows = db.getRows("select * from dbo.Tests where Regex='rowToUpdate'")
        testRegexValue = rows[0].Regex
        self.assertEqual('rowToUpdate', testRegexValue)

        # test
        updateQuery = PutThingsInTables('Tests', ['Regex'], ['thisCellWasUpdated'], whereColumnNames=['AttributeId'],
                                        whereValues=['94']).createSQLQueryUpdate()
        db.insertUpdateOrDelete(updateQuery)
        rows = db.getRows("select * from dbo.Tests where AttributeId='94'")
        testUpdatedValue = rows[0].Regex
        self.assertEqual('thisCellWasUpdated', testUpdatedValue)

        # tear down
        db.insertUpdateOrDelete("delete from dbo.Tests where AttributeId='94'")

if __name__ == '__main__':
    unittest.main()
