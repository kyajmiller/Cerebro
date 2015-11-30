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

        self.columnsDelimiter = chr(1)
        self.entriesDelimiter = chr(2)

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

    def appendToFile(self, fileName, value):
        fileOut = self.openFile(fileName, 'a')
        fileOut.write(value)
        fileOut.close()

    def writeToFile(self, fileName, value):
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

    def clearFile(self, fileName):


    def createHeaderLine(self, columns):
        headerLine = self.columnsDelimiter.join(columns)
        headerLine = '%s%s' % (headerLine, self.entriesDelimiter)
        return headerLine

    def getColumnsFromHeaderLine(self, headerLine):
        headerLine = re.sub(self.entriesDelimiter, '', headerLine)
        columns = headerLine.split(self.columnsDelimiter)
        return columns

    def createEntry(self, values):
        entry = self.columnsDelimiter.join(values)
        entry = '%s%s' % (entry, self.entriesDelimiter)
        return entry

    def getEntryValuesListFromEntry(self, entry):
        entry = re.sub(self.entriesDelimiter, '', entry)
        valuesList = entry.split(self.columnsDelimiter)
        return valuesList

    def insertSingleEntry(self, fileName, columns, values):
        currentContents = self.readFile(fileName, 'read')
        if len(currentContents) == 0:
            headerLine = self.createHeaderLine(columns)
            self.appendToFile(fileName, headerLine)

        entry = self.createEntry(values)
        self.appendToFile(fileName, entry)


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
