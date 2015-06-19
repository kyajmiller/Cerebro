from Classes.Parser import Parser

class HighSchoolCity(Parser):
    def __init__(self, stringToScan, cities):
        self.cities = cities
        self.stringToScan = stringToScan
        Parser.__init__(self, self.stringToScan, self.cities)
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        return contextChecker.doesMatchExist()

    def getHighSchoolCity(self):
        if self.checkContext('high\sschool|highschool|hs') and self.doesMatchExist():
            for i in self.getResult():
                self.resultList.append(i)

        self.resultList = list(set(self.resultList))
        return self.resultList
