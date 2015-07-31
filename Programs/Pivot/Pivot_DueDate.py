import re
from Pivot_Parser import Parser


class DueDate(object):
    def __init__(self, stringToScan):
        self.stringToScan = stringToScan
        self.regexMonthDayYear = '(January|February|March|April|May|June|July|August|September|October|November|December)\s[0-3]?[0-9],?\s\d{4}'
        self.regexMonthYear = '(January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4}'
        self.regexMMDDYYYY = '[01][0-9]\/[0-3][0-9]\/[12]\d{3}'

        self.resultList = []
        self.dueDate = ''

    def checkDueDateContext(self):
        contextRegex = 'due\sdate|application\swindow|deadline|dead\sline|close\sdate|close|closing\sdate'
        contextChecker = Parser(self.stringToScan.lower(), contextRegex)
        return contextChecker.doesMatchExist()

    def checkMonthDayYearFormat(self):
        checkMonthDayYear = re.search(self.regexMonthDayYear, self.stringToScan)
        if checkMonthDayYear:
            rawDate = checkMonthDayYear.group()
            formattedDate = self.formatDateMonthDayYear(rawDate)
            return formattedDate

    def checkMonthYearFormat(self):
        checkMonthYear = re.search(self.regexMonthYear, self.stringToScan)
        if checkMonthYear:
            return checkMonthYear.group()

    def checkNumbersFormat(self):
        checkNumbers = re.search(self.regexMMDDYYYY, self.stringToScan)
        if checkNumbers:
            rawDate = checkNumbers.group()
            formattedDate = self.formatDateNumbers(rawDate)
            return formattedDate

    def formatDateMonthDayYear(self, monthDayYearDate):
        pattern = '(January|February|March|April|May|June|July|August|September|October|November|December)\s([0-3]?[0-9]),?\s(\d{4})'
        findMonthDayYear = re.search(pattern, monthDayYearDate)
        if findMonthDayYear:
            month = findMonthDayYear.group(1)
            day = findMonthDayYear.group(2)
            year = findMonthDayYear.group(3)

            formattedDate = '%s %s %s' % (day, month, year)

            return formattedDate

    def formatDateNumbers(self, numbersDate):
        pattern = '([01][0-9])\/([0-3][0-9])\/([12]\d{3})'
        findMonthDayYear = re.search(pattern, numbersDate)
        if findMonthDayYear:
            month = findMonthDayYear.group(1)
            day = findMonthDayYear.group(2)
            year = findMonthDayYear.group(3)

            if month == '01':
                month = 'January'
            elif month == '02':
                month = 'February'
            elif month == '03':
                month = 'March'
            elif month == '04':
                month = 'April'
            elif month == '05':
                month = 'May'
            elif month == '06':
                month = 'June'
            elif month == '07':
                month = 'July'
            elif month == '08':
                month = 'August'
            elif month == '09':
                month = 'September'
            elif month == '10':
                month = 'October'
            elif month == '11':
                month = 'November'
            elif month == '12':
                month = 'December'

            day = re.sub('^0', '', day)

            formattedDate = '%s %s %s' % (day, month, year)

            return formattedDate

    def getDueDate(self):
        self.resultList = []
        if self.checkDueDateContext():
            if self.checkMonthDayYearFormat():
                self.dueDate = self.checkMonthDayYearFormat()
            elif self.checkNumbersFormat():
                self.dueDate = self.checkNumbersFormat()
            elif self.checkMonthYearFormat():
                self.dueDate = self.checkMonthYearFormat()
        return self.dueDate
