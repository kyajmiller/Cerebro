class ScholarshipPackageRequirement(object):
    def __init__(self, scholarshipPackageId, attributeId, requirementType, requirementValue, logicGroup):
        self.attributeId = attributeId
        self.logicGroup = logicGroup
        self.requirementValue = requirementValue
        self.requirementType = requirementType
        self.scholarshipPackageId = scholarshipPackageId

    def getStringValue(self):
        stringValue = 'AttributeId = %s, RequirementTypeCode = %s, RequirementValue = %s, LogicGroup = %s' % (
        self.attributeId, self.requirementType, self.requirementValue, self.logicGroup)

        return stringValue
