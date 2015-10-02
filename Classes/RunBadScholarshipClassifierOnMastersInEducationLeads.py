from Classes.RunBadScholarshipClassifier import RunBadScholarshipClassifier
from Classes.MastersInEducationLeadsGetDatabaseInfo import MastersInEducationLeadsGetDatabaseInfo


class RunBadScholarshipClassifierOnMastersInEducationLeads(RunBadScholarshipClassifier):
    def __init__(self):
        mastersInEducationInfo = MastersInEducationLeadsGetDatabaseInfo()

        self.sponsorList = []
        self.descriptionsList = mastersInEducationInfo.getDescriptions()
        self.listMastersInEducationLeadIds = mastersInEducationInfo.getMastersInEducationLeadIds()
        self.tableName = 'MastersInEducationLeads'
        self.idColumnName = 'MastersInEducationLeadId'

        RunBadScholarshipClassifier.__init__(self, self.sponsorList, self.descriptionsList)
        self.getPredictedBadInsertIntoDatabase(self.tableName, self.idColumnName, self.listMastersInEducationLeadIds)


RunBadScholarshipClassifierOnMastersInEducationLeads()
