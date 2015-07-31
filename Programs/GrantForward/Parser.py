import re


class Parser(object):
    def __init__(self, stringToScan, searchCriteria):
        self.searchCriteria = searchCriteria
        self.stringToScan = stringToScan
        self.result = []
        self.IsMatch = self.doesMatchExist()
        self.getResult()

    def doesMatchExist(self):
        findMatch = re.findall(self.searchCriteria, self.stringToScan)
        if findMatch:
            return True
        else:
            return False

    def getResult(self):
        if self.doesMatchExist():
            findMatch = re.findall(self.searchCriteria, self.stringToScan)
            if findMatch:
                self.result = findMatch
        return self.result
