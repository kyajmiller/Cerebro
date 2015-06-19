from Classes.Parser import Parser


class HighSchoolState(Parser):
    def __init__(self, stringToScan, states):
        self.states = states
        self.stringToScan = stringToScan
        Parser.__init__(self, self.stringToScan, self.states)
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        return contextChecker.doesMatchExist()

    def getHighSchoolState(self):
        if self.checkContext('high\sschool|highschool|hs') and self.doesMatchExist():
            for i in self.getResult():
                self.resultList.append(i.strip())

        self.resultList = list(set(self.resultList))
        return self.resultList
