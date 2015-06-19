from Classes.Parser import Parser

class SATScore(Parser):
    def __init__(self, stringToScan):
        self.stringToScan = stringToScan
        Parser.__init__(self, self.stringToScan, '\s\d{3,4}\s')
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        return contextChecker.doesMatchExist()

    def getSATScore(self):
        if self.checkContext('sat|sat\sscore') and self.doesMatchExist():
            for i in self.getResult():
                self.resultList.append(i.strip())

        return self.resultList
