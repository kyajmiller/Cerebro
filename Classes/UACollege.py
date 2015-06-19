from Classes.Parser import Parser

class UACollege(Parser):
    def __init__(self, stringToScan, uaColleges):
        self.uaColleges = uaColleges
        self.stringToScan = stringToScan
        Parser.__init__(self, self.stringToScan, self.uaColleges)
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        return contextChecker.doesMatchExist()

    def getUACollege(self):
        if self.checkContext('college|college\sof|school\sof') and self.doesMatchExist():
            for i in self.getResult():
                self.resultList.append(i)

        self.resultList = list(set(self.resultList))
        return self.resultList