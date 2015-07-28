import re
from Classes.Parser import Parser


class DueDate(Parser):
    def __init__(self, stringToScan):
        self.stringToScan = stringToScan
        self.dateRegex = '(((January|February|March|April|May|June|July|August|September|October|November|December)|([01][0-9]\/))(\s[123]?[0-9](st|nd|rd|th)?[,\/]?(\d{2})?\s)?(\d{4})?)'
        Parser.__init__(self, self.stringToScan, self.dateRegex)

        self.resultList = []
        self.dueDate = ''

    def checkContext(self, contextRegex):
        contextChecker = Parser(self.stringToScan.lower(), contextRegex)
        return contextChecker.doesMatchExist()

    def getDueDate(self):
        if self.checkContext(
                'due\sdate|application\swindow|deadline|dead\sline|close\sdate|close') and self.doesMatchExist():
            for i in self.getResult():
                self.resultList.append(i[0])

        self.resultList = list(set(self.resultList))
        self.dueDate = self.resultList
        return self.dueDate
