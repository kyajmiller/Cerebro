from Classes.Parser import Parser

class GPA(Parser):
    def __init__(self, stringToScan):
        self.stringToScan = stringToScan
        Parser.__init__(self, self.stringToScan, '[1234]\.\d+')
        self.resultList = []
        self.attributeId = '1'
        self.requirementValue = ''
        self.logicGroup = '0'

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        return contextChecker.doesMatchExist()

    def getGPA(self):
        if self.checkContext('gpa|grade\spoint\saverage|maintain') and self.doesMatchExist():
            for i in self.getResult():
                self.resultList.append(i)

        self.resultList = list(set(self.resultList))
        self.requirementValue = self.resultList
        return self.requirementValue

    #def getScholarshipPackageRequirementDetails(self):
