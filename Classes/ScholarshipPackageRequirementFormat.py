class ScholarshipPackageRequirement(object):
    def __init__(self,scholarshipPackageId,requirementType,requirementValue,logicGroup):
        self.logicGroup = logicGroup
        self.requirementValue = requirementValue
        self.requirementType = requirementType
        self.scholarshipPackageId = scholarshipPackageId