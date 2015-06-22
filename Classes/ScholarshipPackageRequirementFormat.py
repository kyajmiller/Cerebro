class ScholarshipPackageRequirement(object):
    def __init__(self, scholarshipPackageId, attributeId, requirementType, requirementValue, logicGroup):
        self.attributeId = attributeId
        self.logicGroup = logicGroup
        self.requirementValue = requirementValue
        self.requirementType = requirementType
        self.scholarshipPackageId = scholarshipPackageId