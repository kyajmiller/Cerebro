from Classes.Parser import Parser


class ResidencyArizonaCounty(Parser):
    def __init__(self, stringToScan, arizonaCounties):
        self.arizonaCounties = arizonaCounties
        self.stringToScan = stringToScan
        Parser.__init__(self, self.stringToScan, self.arizonaCounties)
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        return contextChecker.doesMatchExist()

    def getResidencyArizonaCounty(self):
        if self.checkContext('resident|reside|residency|live|live\sin') and self.checkContext(
                'county|counties') and self.doesMatchExist():
            for i in self.getResult():
                self.resultList.append(i)

        self.resultList = list(set(self.resultList))
        return self.resultList
