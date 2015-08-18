from Classes.Parser import Parser


class Gender(Parser):
    def __init__(self, stringToScan):
        Parser.stringToScan = stringToScan
        Parser.__init__(self, self.stringToScan, '(?:\s|\>)[mM]ale|(?:\s|\>)+[Ff]emale|(?:\s|\>)+[Ww]omen|(?:\s|\>)+[Mm]en')
        self.resultList = []

    def checkContext(self, contextCriteria):
        return Parser(self.stringToScan.lower(), contextCriteria).doesMatchExist()

    def getRequiredGender(self):
        if self.doesMatchExist():
            for i in self.getResult():
                self.resultList.append(i.strip())

        self.resultList = list(set(self.resultList))
        return self.resultList

