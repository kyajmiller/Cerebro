from Classes.Parser import Parser

class EnrollmentStatus(Parser):
    def __init__(self, stringToScan):
        self.stringToScan = stringToScan
        Parser.__init__(self, self.stringToScan.lower(), 'full\-time|part\-time|full\stime|part\stime')
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        return contextChecker.doesMatchExist()

    def getEnrollmentStatus(self):
        if self.checkContext('enroll|study') and self.doesMatchExist():
            for i in self.getResult():
                self.resultList.append(i)
        elif not self.checkContext('work|employ|job') and self.doesMatchExist():
            for i in self.getResult():
                self.resultList.append(i)

        self.resultList = list(set(self.resultList))
        return self.resultList