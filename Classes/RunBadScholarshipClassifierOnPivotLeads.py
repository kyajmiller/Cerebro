from Classes.RunBadScholarshipClassifier import RunBadScholarshipClassifier
from Classes.PivotLeadsGetDatabaseInfo import PivotLeadsGetDatabaseInfo


class RunBadScholarshipClassifierOnPivotLeads(RunBadScholarshipClassifier):
    def __init__(self):
        pivotLeadsInfo = PivotLeadsGetDatabaseInfo(tag='Scholarship')

        self.sponsorList = pivotLeadsInfo.getSponsors()
        self.infoText = pivotLeadsInfo.getListStringConcatendatedAbstractEligibility()
        self.listPivotLeadsIds = pivotLeadsInfo.getPivotLeadId()
        self.tableName = 'PivotLeads'
        self.idColumnName = 'PivotLeadId'

        RunBadScholarshipClassifier.__init__(self, self.sponsorList, self.infoText)
        self.getPredictedBadInsertIntoDatabase(self.tableName, self.idColumnName, self.listPivotLeadsIds)


RunBadScholarshipClassifierOnPivotLeads()
