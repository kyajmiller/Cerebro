from Classes.Parser import Parser

class Citizenship(Parser):
    def __init__(self, stringToScan, countriesNationalities):
        self.countriesNationalities = countriesNationalities
        self.stringToScan = stringToScan
        Parser.__init__(self, self.stringToScan, self.countriesNationalities)
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        return contextChecker.doesMatchExist()

    def getCitizenship(self):
        if self.checkContext('citizen') and self.doesMatchExist():
            for i in self.getResult():
                self.resultList.append('%s Citizen' % i)
        
        if self.checkContext('\snational') and self.doesMatchExist():
            for i in self.getResult():
                self.resultList.append('%s National' % i)

        self.resultList = list(set(self.resultList))
        return self.resultList
