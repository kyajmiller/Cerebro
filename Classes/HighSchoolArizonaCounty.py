from Classes.Parser import Parser


class HighSchoolArizonaCounty(Parser):
    def __init__(self, stringToScan, arizonaCounties):
        self.arizonaCounties = arizonaCounties
        self.stringToScan = stringToScan
        Parser.__init__(self, self.stringToScan, self.arizonaCounties)
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        return contextChecker.doesMatchExist()

    def getHighSchoolArizonaCounty(self):
        if self.checkContext('high\sschool|highschool|hs') and self.checkContext(
                'county|counties') and self.doesMatchExist():
            for i in self.getResult():
                self.resultList.append(i)

        self.resultList = list(set(self.resultList))
        return self.resultList
