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




    '''
    def test_ClearFileAppendLineAndReadFile(self):
        file = 'sudbconnecttest.txt'
        db = SUDBConnect(destination='filesystem')
        valueToWrite = 'kitty'
        db.clearFile(file)
        fileData = db.readFile(file)
        self.assertIsNotNone(fileData)
        self.assertEqual(fileData, '')

        db.appendToFile(file, valueToWrite)

        fileData = db.readFile(file)
        self.assertIsNotNone(fileData)
        self.assertEqual(fileData, 'kitty')

    def test_CreateHeaderLineAndCreateColumnsFromHeaderLine(self):
        columns = ['guen', 'alex', 'cassie', 'peter']
        db = SUDBConnect()
        headerLine = db.createHeaderLine(columns)
        testHeader = chr(1).join(columns)
        testHeader = '%s%s' % (testHeader, chr(2))
        self.assertEqual(headerLine, testHeader)

        # break down headerLine to make sure it can be split up right
        testColumns = db.getColumnsFromHeaderLine(headerLine)
        self.assertEqual(columns, testColumns)

    def test_InsertAnEntryAndGetColumnsAndEntriesLists(self):
        file = 'sudbconnecttest.txt'
        db = SUDBConnect(destination='filesystem')
        db.clearFile(file)
        columns = ['cats', 'ages']
        catNamesList = ['guen', 'alex', 'cassie', 'peter']
        catAgesList = [4, 2, 6, 4]

        for i in range(len(catNamesList)):
            valuesToInsert = [catNamesList[i], catAgesList[i]]
            db.insertSingleEntry(file, columns, valuesToInsert)

        testColumns, testEntriesLists = db.getColumnsEntriesAndIdentityCounter(file)
        expectedEntries = [['guen', '4'], ['alex', '2'], ['cassie', '6'], ['peter', '4']]
        self.assertEqual(columns, testColumns)
        self.assertEqual(expectedEntries, testEntriesLists)

    def test_fileSystemGetRows(self):
        # want to build something similar to the .getRows for the database destination, will use this space to test
        # this isn't a real unit test
        # start out by making a file to use, will comment out this next section so it doesn't get overwritten later
        file = 'sudbconnectGetRowsTest.txt'
        db = SUDBConnect(destination='filesystem')
        db.clearFile(file)
        columns = ['testId', 'animals']
    '''





if __name__ == '__main__':
    unittest.main()
