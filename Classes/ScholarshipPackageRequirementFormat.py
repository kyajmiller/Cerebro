class ScholarshipPackageRequirement(object):
    def __init__(self,scholarshipPackageId,requirementType,requirementValue):
        self.requirementValue = requirementValue
        self.requirementType = requirementType
        self.scholarshipPackageId = scholarshipPackageId