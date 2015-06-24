from Classes.Parser import Parser
from Classes.ScholarshipPackageRequirementFormat import ScholarshipPackageRequirement


class UACollege(Parser):
    def __init__(self, stringToScan, scholarshipPackageId, uaColleges):
        self.uaColleges = uaColleges
        self.stringToScan = stringToScan
        Parser.__init__(self, self.stringToScan, self.uaColleges)
        self.resultList = []
        self.attributeId = '377'
        self.requirementValue = ''
        self.logicGroup = '0'
        self.requirementTypeCode = '*'
        self.scholarshipPackageId = scholarshipPackageId

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        return contextChecker.doesMatchExist()

    def getUACollege(self):
        if self.checkContext('college|college\sof|school\sof') and self.doesMatchExist():
            for i in self.getResult():
                self.resultList.append(i)
        if self.checkContext('ua south'):
            self.resultList.append('UA South')
        if self.checkContext('\scom\s'):
            self.resultList.append('College of Medicine')

        self.resultList = list(set(self.resultList))

        self.requirementValue = ', '.join(self.resultList)
        return self.requirementValue

    def getScholarshipPackageRequirementFormat(self):
        if self.getUACollege() != '':
            UACollege_SPRF = ScholarshipPackageRequirement(self.scholarshipPackageId, self.attributeId,
                                                           self.requirementTypeCode, self.getUACollege(),
                                                           self.logicGroup)

            return UACollege_SPRF
