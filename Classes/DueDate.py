import re
from Classes.Parser import Parser


class DueDate(object):
    def __init__(self, stringToScan):
        self.stringToScan = stringToScan
        self.regexMonthDayYear = '(January|February|March|April|May|June|July|August|September|October|November|December)\s[0-3]?[0-9],?\s\d{4}'
        self.regexMonthYear = '(January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4}'
        self.regexMMDDYYYY = '[01][0-9]\/[0-3][0-9]\/[12]\d{3}'

        self.resultList = []
        self.dueDate = ''

    def checkDueDateContext(self):
        contextRegex = 'due\sdate|application\swindow|deadline|dead\sline|close\sdate|close'
        contextChecker = Parser(self.stringToScan.lower(), contextRegex)
        return contextChecker.doesMatchExist()

    def checkMonthDayYearFormat(self):
        checkMonthDayYear = re.search(self.regexMonthDayYear, self.stringToScan)
        if checkMonthDayYear:
            self.resultList.append(checkMonthDayYear.group())

    def checkMonthYearFormat(self):
        checkMonthYear = re.search(self.regexMonthYear, self.stringToScan)
        if checkMonthYear:
            self.resultList.append(checkMonthYear.group())

    def checkNumbersFormat(self):
        checkNumbers = re.search(self.regexMMDDYYYY, self.stringToScan)
        if checkNumbers:
            self.resultList.append(checkNumbers.group())

    def getDueDate(self):
        self.resultList = []
        if self.checkDueDateContext():
            self.checkMonthDayYearFormat()
            self.checkMonthYearFormat()
            self.checkNumbersFormat()

        self.dueDate = ', '.join(self.resultList)
        return self.dueDate
