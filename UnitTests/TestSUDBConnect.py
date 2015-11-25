import unittest
from Classes.SUDBConnect import SUDBConnect


class TestStringMethods(unittest.TestCase):
    def test_ConnectToDBDefaultArguments(self):
        db = SUDBConnect()
        rows = db.getRowsDB("select * from dbo.Tests")
        self.assertIsNotNone(rows)
        self.assertGreater(len(rows), 0)

    def test_ConnectToDBInsertUpdateDelete(self):
        db = SUDBConnect()
        rows = db.getRowsDB("select * from dbo.Tests")
        self.assertGreater(len(rows), 0)
        db.insertUpdateOrDeleteDB("insert into dbo.Tests (Regex, AttributeId) values ('meow', 2)")
        rows = db.getRowsDB("select * from dbo.Tests where Regex='meow'")
        self.assertGreater(len(rows), 0)
        db.insertUpdateOrDeleteDB("update dbo.Tests set Regex='kitty' where Regex='meow'")
        rows = db.getRowsDB("select * from dbo.Tests where Regex='kitty'")
        self.assertGreater(len(rows), 0)
        db.insertUpdateOrDeleteDB("delete from dbo.Tests where Regex='kitty'")
        rows = db.getRowsDB("select * from dbo.Tests where Regex='kitty'")
        self.assertEqual(len(rows), 0)

    def test_ConnectToDifferentDB(self):
        db = SUDBConnect(database='ScholarshipUniverse')
        rows = db.getRowsDB("select * from dbo.PotentialScholarships")
        self.assertIsNotNone(rows)
        self.assertGreater(len(rows), 0)

    def test_seeIfCanFindFilesAtAll(self):
        filesystemPath = 'C:\crawlyjones'
        fileName = 'sudbconnecttest.txt'
        totalFilePath = '%s\%s' % (filesystemPath, fileName)

        # try writing to file, read back in file, see what happens
        writeFile = open(totalFilePath, 'w')
        writeFile.write('cheese')
        writeFile.close()

        readFile = open(totalFilePath, 'r+')
        fileData = readFile.read()
        self.assertEqual(fileData, 'cheese')
        readFile.close()



if __name__ == '__main__':
    unittest.main()
