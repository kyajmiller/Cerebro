import pyodbc
import re


class SUDBConnect(object):
    def __init__(self, server='SUDB-DEV', database='Spiderman', destination='database',
                 filesystemPath='C:\crawlyjones'):
        self.fileSystemPath = filesystemPath
        self.destination = destination
        self.server = server
        self.database = database
        self.okayToRunDatabase = False
        self.okayToRunFilesystem = False

        if self.destination == 'database':
            connectionString = r'Driver={SQL Server};Server=%s;Database=%s;Trusted_Connection=yes;' % (
                self.server, self.database)
            self.cnxn = pyodbc.connect(connectionString)
            self.okayToRunDatabase = True
        elif self.destination == 'filesystem':
            self.okayToRunFilesystem = True

    def getRowsDB(self, sql):
        if self.okayToRunDatabase:
            cursor = self.cnxn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows

    def insertUpdateOrDeleteDB(self, sql):
        if self.okayToRunDatabase:
            cursor = self.cnxn.cursor()
            cursor.execute(sql)
            cursor.commit()
            pass

    def openFile(self, fileName, mode='r'):
        filePath = '%s\%s' % (self.fileSystemPath, fileName)
        fileIn = open(filePath, mode)
        return fileIn

    def writeFile(self, fileName, value):
        fileOut = self.openFile(fileName, 'w')
        fileOut.write(value)
        fileOut.close()

    def readFile(self, fileName, mode='read'):
        fileIn = self.openFile(fileName)

        fileData = None

        if mode == 'read':
            fileData = fileIn.read()
            fileIn.close()
        elif mode == 'readlines':
            fileData = fileIn.readlines()
            fileIn.close()

        return fileData

    '''
    def openFileReturnAllLines(self, fileName):
        filePath = self.filesystemPath + ('\%s' % fileName)
        filein = open(filePath, 'r')
        lines = filein.readlines()
        lines = [line.strip() for line in lines]
        filein.close()
        return lines

    def openFileReturnEntriesNoHeader(self, fileName):
        allLines = self.openFileReturnAllLines(fileName)
        entriesOnly = allLines[1:]
        return entriesOnly

    def openOutputFile(self, fileName):
        filePath = self.filesystemPath + ('\%s' % fileName)
        fileout = open(filePath, 'a')
        return fileout

    def getColumns(self, fileInLines):
        headerRow = fileInLines[0]
        removeEndEntryDelimiter = re.sub(chr(2), '', headerRow)
        headerRow = removeEndEntryDelimiter
        columns = headerRow.split(chr(1))
        return columns

    def insertEntry(self, fileName, columns, values):
        outputFile = self.openOutputFile(fileName)
        allExistingLinesWithHeader = self.openFileReturnAllLines(fileName)

        if len(columns) == len(values):
            if len(allExistingLinesWithHeader) == 0:
                headerRow = chr(1).join(columns)
                headerRow = '%s%s' % (headerRow, chr(2))
                outputFile.write(headerRow)
            elif len(allExistingLinesWithHeader) > 1:
                valuesRow = chr(1).join(values)
                valuesRow = '%s%s' % (valuesRow, chr(2))
                outputFile.write(valuesRow)

    '''
    def getAllTestCases(self):
        return self.getRowsDB("Select * from DepartmentTestCases")

    def getNumberOfTestCases(self, numberToGet):
        return self.getRowsDB("Select top " + str(numberToGet) + " * from DepartmentTestCases")

    def getNumberOfRandomTestCases(self, numberToGet):
        return self.getRowsDB("Select top " + str(numberToGet) + " * from DepartmentTestCases order by newid()")

    def insertIntoJustTests(self, valToInsert):
        self.insertUpdateOrDeleteDB("insert into justtests(testvalue) values ('" + str(valToInsert) + "')")
