from Classes.Parser import Parser


class Majors(Parser):
    def __init__(self, stringToScan, scholarshipPackageId, majorOptions):
        self.majorOptions = majorOptions
        self.stringToScan = stringToScan
        Parser.__init__(self, self.stringToScan.lower(), self.majorOptions)
        self.resultList = []
        self.attributeId = '1'
        self.requirementValue = ''
        self.logicGroup = '0'
        self.requirementTypeCode = '>='
        self.scholarshipPackageId = scholarshipPackageId

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        return contextChecker.doesMatchExist()

    def getMajors(self):
        if self.checkContext(
                'enrolled in|majoring in|program|major|concentration|pursuing|student') and self.doesMatchExist():
            for i in self.getResult():
                self.resultList.append(i)

        self.resultList = list(set(self.resultList))

        self.requirementValue = ', '.join(self.resultList)
        return self.requirementValue
