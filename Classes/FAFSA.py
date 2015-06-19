from Classes.Parser import Parser

class FAFSA(Parser):
    def __init__(self, stringToScan):
        self.stringToScan = stringToScan
        Parser.__init__(self, self.stringToScan.lower(), 'fafsa')
        self.resultList = []

    def getFAFSA(self):
        if self.doesMatchExist():
            self.resultList.append('yes')

        return self.resultList
