from Classes.UnigoLeadsGetDatabaseInfo import UnigoLeadsGetDatabaseInfo
from Classes.PopulateRequirements import PopulateRequirements


class PopulateUnigoRequirements(PopulateRequirements):
    def __init__(self):
        self.requirementsTableName = 'UnigoRequirements'
        self.requirementsTableColumns = ['UnigoLeadId', 'AttributeId', 'AttributeValue']
        PopulateRequirements.__init__(self, self.requirementsTableName, self.requirementsTableColumns)

    def loopThroughLeadsAndDoStuff(self):
        unigoDataInfo = UnigoLeadsGetDatabaseInfo()
        listOfUnigoLeadsIds = unigoDataInfo.getUnigoLeadsIds()
        listOfRequirements = unigoDataInfo.getRequirements()

        for i in range(len(listOfUnigoLeadsIds)):
            unigoLeadId = listOfUnigoLeadsIds[i]
            requirements = listOfRequirements[i]
            requirementsSentences = self.tokenizeIntoSentences(requirements)

            gpa = self.getGPAFromSentences(requirementsSentences)
            majors = self.getMajorFromSentences(requirementsSentences)

            self.doDatabaseInsertsGPAMajor(unigoLeadId, gpa, majors)


PopulateUnigoRequirements().loopThroughLeadsAndDoStuff()
