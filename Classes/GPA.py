from Classes.Parser import Parser

class GPA(Parser):
    def __init__(self, stringToScan):
        self.stringToScan = stringToScan
        Parser.__init__(self, self.stringToScan, '[1234]\.\d+')
        self.resultList = []
        self.attributeId = '1'
        self.requirementValue = ''
        self.logicGroup = '0'
        self.requirementTypeCode = '>='
        self.scholarshipPackageRequirementFormat = ''

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        return contextChecker.doesMatchExist()

    def getGPA(self):
        if self.checkContext('gpa|grade\spoint\saverage|maintain') and self.doesMatchExist():
            for i in self.getResult():
                self.resultList.append(i)

        self.resultList = list(set(self.resultList))

        self.requirementValue = self.resultList
        self.requirementValue = ', '.join(self.requirementValue)
        return self.requirementValue

    def getScholarshipPackageRequirementFormat(self):
        if self.getGPA() != '':
            self.scholarshipPackageRequirementFormat = 'AttributeId = %s, RequirementTypeCode = %s, RequirementValue = %s, LogicGroup = %s' % (self.attributeId, self.requirementTypeCode, self.getGPA(), self.logicGroup)

        return self.scholarshipPackageRequirementFormat