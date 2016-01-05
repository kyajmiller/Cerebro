import unittest
import re
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

        readFile = open(totalFilePath, 'r')
        fileData = readFile.read()
        self.assertEqual(fileData, 'cheese')
        readFile.close()

    def test_OpenFile(self):
        db = SUDBConnect(destination='filesystem', filesystemPath='c:\crawlyjones')
        fileIn = db.openFile('sudbconnecttest.txt', 'r')
        self.assertIsNotNone(fileIn)

    def test_convertURL(self):
        testURL = 'www.google.com'
        db = SUDBConnect()
        convertURL = db.convertURL(testURL)
        expectedURL = 'www((dot))google((dot))com'
        self.assertEqual(expectedURL, convertURL)

        testURL2 = 'http://www.google.com'
        convertURL = db.convertURL(testURL2)
        expectedURL = 'http((col))((fs))((fs))www((dot))google((dot))com'
        self.assertEqual(expectedURL, convertURL)

        testURL3 = 'https://news.ycombinator.com/item?id=7824462'
        convertURL = db.convertURL(testURL3)
        expectedURL = 'https((col))((fs))((fs))news((dot))ycombinator((dot))com((fs))item((ques))id=7824462'
        self.assertEqual(expectedURL, convertURL)

    def test_CreateFilePath(self):
        db = SUDBConnect()
        user = 'Kya'
        website = 'KyasCatPage'
        fileName = 'cats.txt'
        filePath = db.createFilePath(user, website, fileName)
        expectedFilePath = 'c:\Cerebro\%s\%s\%s' % (user, website, fileName)
        self.assertEqual(expectedFilePath, filePath)

    def test_getColumnNames(self):
        db = SUDBConnect()
        tableName = 'Tests'
        columnNames = db.getColumnNamesFromTable(tableName)
        self.assertIsNotNone(columnNames)

    def test_writeFile(self):
        db = SUDBConnect(destination='filesystem')
        columns = ['animal', 'name']
        values = ['kitty', 'guen']
        user = 'Kya'
        website = 'KyasTestWebsite'
        url = 'www.kyastestwebsite.com'
        date = '20151204'
        db.writeFile(columns, values, user, website, url, date)

    def test_readFile(self):
        db = SUDBConnect(destination='filesystem')
        user = 'Kya'
        website = 'KyasTestWebsite'
        url = 'www.kyastestwebsite.com'
        date = '20151204'
        filePath = db.createFilePath(user, website, url, date)
        columns, values = db.readFileGetColumnsAndData(filePath)
        expectedColumns = ['animal', 'name']
        expectedValues = ['kitty', 'guen']
        self.assertEqual(expectedColumns, columns)
        self.assertEqual(expectedValues, values)

    def test_getRowValuesToPassToFunction(self):
        db = SUDBConnect()
        rows = db.getRowsDB("select * from dbo.Tests")
        columns = db.getColumnNamesFromTable('Tests')
        print(rows)
        print(columns)

    def test_removeOldFile(self):
        db = SUDBConnect(destination='filesystem')
        user = 'Kya'
        website = 'KyasTestWebsite'
        url = 'www.kyastestwebsite.com'
        date = '20150000'
        columns = ['animal', 'name']
        values = ['kitty', 'guen']
        db.writeFile(columns, values, user, website, url, date)

        db.removeOldFile(user, website, url)

    def test_stringSearch(self):
        nameToCheck = 'KyasTestWebsite-www((dot))kyastestwebsite((dot))com'
        fileToCheck = 'KyasTestWebsite-www((dot))kyastestwebsite((dot))com-20150000.txt'
        if nameToCheck in fileToCheck:
            print('match')

    def test_CGRLLFileCreationWhyDoesItSuck(self):
        db = SUDBConnect(destination='filesystem')
        columns = ['sponsor']
        values = ['BMI Foundation, Inc']
        user = 'Kya'
        website = 'CollegeGreenLight'
        url = 'https://www.collegegreenlight.com/scholarship/listings/BMI-Student-Composer-Awards/-s-d-49468/?sortBy=&reverse=false'
        # url = 'https://www.collegegreenlight.com/scholarship/listings/BMI-Student-Composer-Awards/-s-d-49468/?'
        date = '20150000'
        db.writeFile(columns, values, user, website, url, date)

if __name__ == '__main__':
    unittest.main()
