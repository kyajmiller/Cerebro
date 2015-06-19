from Classes.Parser import Parser


class ResidencyState(Parser):
    def __init__(self, stringToScan, states):
        self.states = states
        self.stringToScan = stringToScan
        Parser.__init__(self, self.stringToScan, self.states)
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        return contextChecker.doesMatchExist()

    def getResidencyState(self):
        if self.checkContext('resident|reside|residency|live|live\sin') and self.doesMatchExist():
            for i in self.getResult():
                self.resultList.append(i.strip())

        self.resultList = list(set(self.resultList))
        return self.resultList
