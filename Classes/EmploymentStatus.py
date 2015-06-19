from Classes.Parser import Parser

class EmploymentStatus(Parser):
    def __init__(self, stringToScan):
        self.stringToScan = stringToScan
        Parser.__init__(self, self.stringToScan, 'full\-time|part\-time|full\stime|part\stime')
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        return contextChecker.doesMatchExist()

    def getEmploymentStatus(self):
        if self.checkContext('work|employ|job'):
            if self.doesMatchExist():
                for i in self.getResult():
                    self.resultList.append(i)
            elif self.checkContext('hour'):
                findHours = Parser(self.stringToScan, '\d{1,2}')
                if findHours.doesMatchExist():
                    for i in findHours.getResult():
                        self.resultList.append('%s Hours' % i)

        self.resultList = list(set(self.resultList))
        return self.resultList