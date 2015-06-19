from Classes.Parser import Parser


class Majors(Parser):
    def __init__(self, stringToScan, majorOptions):
        self.majorOptions = majorOptions
        self.stringToScan = stringToScan
        Parser.__init__(self, self.stringToScan.lower(), self.majorOptions)
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        return contextChecker.doesMatchExist()

    def getMajors(self):
        if self.checkContext(
                'enrolled in|majoring in|program|major|concentration|pursuing|student') and self.doesMatchExist():
            for i in self.getResult():
                self.resultList.append(i)

        self.resultList = list(set(self.resultList))
        return self.resultList
