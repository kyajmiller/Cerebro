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
        self.identityCounterDelimiter = chr(3)

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

    def createHeaderLine(self, columns):
        headerLine = self.columnsDelimiter.join(columns)
        headerLine = '%s%s%s' % (self.entriesDelimiter, headerLine, self.entriesDelimiter)
        return headerLine

    def createEntryLine(self, values):
        entryLine = self.columnsDelimiter.join(values)
        entryLine = '%s%s%s' % (self.entriesDelimiter, entryLine, self.entriesDelimiter)
        return entryLine

    def convertURL(self, url):
        url = re.sub('\.', '((dot))', url)
        url = re.sub('<', '((less))', url)
        url = re.sub('>', '((great))', url)
        url = re.sub(':', '((col))', url)
        url = re.sub('"', '((dq))', url)
        url = re.sub('/', '((fs))', url)
        # url = re.sub('\\\\', '((bs))', url)
        url = re.sub('\|', '((pipe))', url)
        url = re.sub('\?', '((ques))', url)
        url = re.sub('\*', '((ast))', url)
        url = re.sub('-', '((dash))', url)

        return url

    '''
    def appendToFile(self, fileName, value):
        fileOut = self.openFile(fileName, 'a')
        fileOut.write(value)
        fileOut.close()

    def writeToFile(self, fileName, value):
        fileOut = self.openFile(fileName, 'w')
        fileOut.write(value)
        fileOut.close()

    def readFile(self, fileName):
        fileIn = self.openFile(fileName)
        fileData = fileIn.read()
        fileIn.close()
        return fileData

    def clearFile(self, fileName):
        self.writeToFile(fileName, '')

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

    def getColumnsEntriesAndIdentityCounter(self, fileName):
        fileData = self.readFile(fileName)
        fileLines = fileData.split(self.entriesDelimiter)

        headerLine = fileLines[0]
        identyCounterLine = None

        if fileLines[-1] == '':
            del fileLines[-1]
            entryLines = fileLines[1:]
        else:
            entryLines = fileLines[1:-1]
            identyCounterLine = fileLines[-1]

        columns = self.getColumnsFromHeaderLine(headerLine)
        entryValueLists = [self.getEntryValuesListFromEntry(entryLine) for entryLine in entryLines]
        return columns, entryValueLists, identyCounterLine

    def getJustEntries(self, fileName):
        columns, entriesLists, identityCounter = self.getColumnsEntriesAndIdentityCounter(fileName)
        return entriesLists

    def insertSingleEntry(self, fileName, columns, values):
        values = [str(value) for value in values]

        currentContents = self.readFile(fileName)
        if len(currentContents) == 0:
            headerLine = self.createHeaderLine(columns)
            self.appendToFile(fileName, headerLine)

        entry = self.createEntry(values)
        self.appendToFile(fileName, entry)

    def getRowsFS(self, fileName, columns='*', whereValues=None):
        pass

    def insertIdentityCounter(self, fileName, currentIdentityCounter=0):
        identityCounterString = '%sIdentityCounter:%s%s' % (
            self.identityCounterDelimiter, currentIdentityCounter, self.identityCounterDelimiter)
        self.appendToFile(fileName, identityCounterString)

    def getIdentityCounter(self, fileName):
        columns, entryValuesLists, identityCounterLine = self.getColumnsEntriesAndIdentityCounter(fileName)
        identityCounterString = identityCounterLine.strip(chr(3))
        identityCounter = identityCounterString.split(':', 1)[1]
        return identityCounter

    def incrementIdentityCounter(self, identityCounter, incrementationValue=1):
        if identityCounter >= 1:
            identityCounter += incrementationValue
        return identityCounter

    def updateIdentityCounter(self, fileName):
        identityCounter = self.getIdentityCounter(fileName)
        identityCounter = self.incrementIdentityCounter(identityCounter)
        return identityCounter
    '''

    def getAllTestCases(self):
        return self.getRowsDB("Select * from DepartmentTestCases")

    def getNumberOfTestCases(self, numberToGet):
        return self.getRowsDB("Select top " + str(numberToGet) + " * from DepartmentTestCases")

    def getNumberOfRandomTestCases(self, numberToGet):
        return self.getRowsDB("Select top " + str(numberToGet) + " * from DepartmentTestCases order by newid()")

    def insertIntoJustTests(self, valToInsert):
        self.insertUpdateOrDeleteDB("insert into justtests(testvalue) values ('" + str(valToInsert) + "')")
