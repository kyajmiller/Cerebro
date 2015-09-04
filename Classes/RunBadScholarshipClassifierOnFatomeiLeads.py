from Classes.RunBadScholarshipClassifier import RunBadScholarshipClassifier
from Classes.FatomeiLeadsGetDatabaseInfo import FatomeiLeadsGetDatabaseInfo


class RunBadScholarshipClassifierOnFatomeiLeads(RunBadScholarshipClassifier):
    def __init__(self):
        fatomeiInfo = FatomeiLeadsGetDatabaseInfo()

        self.sponsorList = []
        self.descriptions = fatomeiInfo.getDescriptions()
        self.listFatomeiLeadIds = fatomeiInfo.getFatomeiLeadIds()
        self.tableName = 'FatomeiLeads'
        self.idColumnName = 'FatomeiLeadId'

        RunBadScholarshipClassifier.__init__(self, self.sponsorList, self.descriptions)
        self.getPredictedBadInsertIntoDatabase(self.tableName, self.idColumnName, self.listFatomeiLeadIds)


RunBadScholarshipClassifierOnFatomeiLeads()
