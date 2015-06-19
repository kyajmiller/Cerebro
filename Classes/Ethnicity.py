from Classes.Parser import Parser


class Ethnicity(Parser):
    def __init__(self, stringToScan, demographics):
        self.demographics = demographics
        self.stringToScan = stringToScan
        Parser.__init__(self, self.stringToScan, self.demographics)
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        return contextChecker.doesMatchExist()

    def getEthnicity(self):
        if self.checkContext('ethnicity|descent|lineage|ancestry|be\sa') and self.doesMatchExist():
            for i in self.getResult():
                self.resultList.append(i)
        elif not self.checkContext('major|department|studies|language') and self.doesMatchExist():
            for i in self.getResult():
                self.resultList.append(i)

        self.resultList = list(set(self.resultList))
        return self.resultList