from Classes.RunBadScholarshipClassifier import RunBadScholarshipClassifier
from Classes.UnigoLeadsGetDatabaseInfo import UnigoLeadsGetDatabaseInfo


class RunBadScholarshipClassifierOnUnigoLeads(RunBadScholarshipClassifier):
    def __init__(self):
        unigoLeadsInfo = UnigoLeadsGetDatabaseInfo()

        self.sponsorList = unigoLeadsInfo.getSponsors()
        self.infoText = []

        self.requirements = unigoLeadsInfo.getRequirements()
        self.additionalInfo = unigoLeadsInfo.getAdditionalInfo()
        for i in range(len(self.requirements)):
            requirements = self.requirements[i]
            additionalInfo = self.additionalInfo[i]
            concatenatedItem = '%s %s' % (requirements, additionalInfo)
            self.infoText.append(concatenatedItem)

        self.listUnigoLeadsIds = unigoLeadsInfo.getUnigoLeadsIds()
        self.tableName = 'UnigoLeads'
        self.idColumnName = 'UnigoLeadId'

        RunBadScholarshipClassifier.__init__(self, self.sponsorList, self.infoText)
        self.getPredictedBadInsertIntoDatabase(self.tableName, self.idColumnName, self.listUnigoLeadsIds)


RunBadScholarshipClassifierOnUnigoLeads()
