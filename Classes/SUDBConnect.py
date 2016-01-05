# -*- coding: utf-8 -*-
import pyodbc
import re
import os
import sys


class SUDBConnect(object):
    def __init__(self, server='SUDB-DEV', database='Spiderman', destination='database',
                 filesystemPath='c:\Cerebro'):
        self.fileSystemPath = filesystemPath
        self.destination = destination
        self.server = server
        self.database = database
        self.okayToRunDatabase = False
        self.okayToRunFilesystem = False

        self.columnsDelimiter = chr(1)
        self.entriesDelimiter = '%s%s' % (chr(2), chr(10))
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
        openFile = open(fileName, mode)
        return openFile

    def readFileGetColumnsAndData(self, filePath):
        fileIn = self.openFile(filePath)
        fileData = fileIn.read()
        splitFile = fileData.split(self.entriesDelimiter)
        headerLine = splitFile[0]
        entryLine = splitFile[1]
        columns = self.getColumns(headerLine)
        values = self.getValues(entryLine)
        return columns, values

    def getColumns(self, headerLine):
        columns = headerLine.split(self.columnsDelimiter)
        return columns

    def getValues(self, entryLine):
        values = entryLine.split(self.columnsDelimiter)
        return values

    def createHeaderLine(self, columns):
        headerLine = self.columnsDelimiter.join(columns)
        return headerLine

    def createEntryLine(self, values):
        values = [str(str(value).encode(sys.stdout.encoding, errors='replace')) for value in values]
        entryLine = self.columnsDelimiter.join(values)
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
        url = re.sub('&', '((amp))', url)
        url = re.sub('=', '((eq))', url)

        return url

    def createFileName(self, website, url, date):
        url = self.convertURL(url)
        fileName = '-'.join([website, url, date])
        fileName = '%s.txt' % fileName
        return fileName

    def createFilePath(self, user, website, url, date):
        fileName = self.createFileName(website, url, date)
        filePath = '\\'.join([self.fileSystemPath, user, website, fileName])
        return filePath

    def getColumnNamesFromTable(self, tableName):
        db = SUDBConnect(destination='database')
        tableName = 'dbo.%s' % tableName
        rows = db.getRowsDB("select name from sys.columns where object_id = object_id('" + tableName + "')")
        columnNames = [row.name for row in rows]
        return columnNames

    def writeFile(self, columns, values, user, website, url, date='20151201'):
        headerLine = self.createHeaderLine(columns)
        entryLine = self.createEntryLine(values)
        fileData = self.entriesDelimiter.join([headerLine, entryLine])
        filePath = self.createFilePath(user, website, url, date)
        self.removeOldFile(user, website, url)
        os.makedirs(os.path.dirname(filePath), exist_ok=True)
        try:
            with open(filePath, 'w') as fileOut:
                fileOut.write(fileData)
                fileOut.close()
        except:
            pass

    def removeOldFile(self, user, website, url):
        url = self.convertURL(url)
        nameToCheck = '-'.join([website, url])
        filePath = '\\'.join([self.fileSystemPath, user, website])

        for filename in os.listdir(filePath):
            if nameToCheck in filename:
                os.remove(os.path.join(filePath, filename))


    def getAllTestCases(self):
        return self.getRowsDB("Select * from DepartmentTestCases")

    def getNumberOfTestCases(self, numberToGet):
        return self.getRowsDB("Select top " + str(numberToGet) + " * from DepartmentTestCases")

    def getNumberOfRandomTestCases(self, numberToGet):
        return self.getRowsDB("Select top " + str(numberToGet) + " * from DepartmentTestCases order by newid()")

    def insertIntoJustTests(self, valToInsert):
        self.insertUpdateOrDeleteDB("insert into justtests(testvalue) values ('" + str(valToInsert) + "')")
