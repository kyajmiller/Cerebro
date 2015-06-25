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
        if self.checkContext('honors') and self.checkContext('student|program'):
            self.resultList.append('Honors College')

        self.resultList = list(set(self.resultList))

        self.requirementValue = ', '.join(self.resultList)
        return self.requirementValue

    def getScholarshipPackageRequirementFormat(self):
        if self.getUACollege() != '':
            UACollege_SPRF = ScholarshipPackageRequirement(self.scholarshipPackageId, self.attributeId,
                                                           self.requirementTypeCode, self.getUACollege(),
                                                           self.logicGroup)

            return UACollege_SPRF

    @staticmethod
    def uaCollegesListForTesting():
        uaColleges = ['College of Agriculture & Life Sciences', 'College of Agriculture and Life Sciences',
                      'College of Architecture, Planning & Landscape Architecture',
                      'College of Architecture Planning and Landscape Architecture', 'College of Education',
                      'College of Engineering', 'School of Fine Arts', 'College of Humanities',
                      'College of Medicine', 'College of Nursing', 'College of Optical Science', 'College of Pharmacy',
                      'College of Science', 'College of Social and Behavioral Sciences',
                      'College of Letters, Arts and Science',
                      'College of Management', 'Eller College', 'Honors College', 'Law', 'James E. Rogers',
                      'Public Health',
                      'Outreach College',
                      'Graduate College', 'School of Art', 'College of Landscape Architecture', 'SNRE', 'COM']

        uaColleges = '|'.join(uaColleges)
        return uaColleges
