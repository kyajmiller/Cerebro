from Classes.Parser import Parser
from Classes.ScholarshipPackageRequirementFormat import ScholarshipPackageRequirement


class Majors(Parser):
    def __init__(self, stringToScan, scholarshipPackageId, majorOptions):
        self.majorOptions = majorOptions
        self.stringToScan = stringToScan
        Parser.__init__(self, self.stringToScan.lower(), self.majorOptions)
        self.resultList = []
        self.attributeId = '417'
        self.requirementValue = ''
        self.logicGroup = '0'
        self.requirementTypeCode = '*'
        self.scholarshipPackageId = scholarshipPackageId

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        return contextChecker.doesMatchExist()

    def getMajors(self):
        if self.checkContext(
                'enrolled in|majoring in|program|major|concentration|pursuing|student') and self.doesMatchExist():
            for i in self.getResult():
                self.resultList.append(i)

        if self.checkContext('of\sscience|of\sarts|of\smedicine') and self.doesMatchExist():
            if 'science' in self.resultList:
                self.resultList.remove('science')
            if 'arts' in self.resultList:
                self.resultList.remove('arts')
            if 'medicine' in self.resultList:
                self.resultList.remove('medicine')

        self.resultList = list(set(self.resultList))

        self.requirementValue = ', '.join(self.resultList)
        return self.requirementValue

    def getScholarshipPackageRequirementFormat(self):
        if self.getMajors() != '':
            Majors_SPRF = ScholarshipPackageRequirement(self.scholarshipPackageId, self.attributeId,
                                                        self.requirementTypeCode, self.getMajors(), self.logicGroup)

            return Majors_SPRF
