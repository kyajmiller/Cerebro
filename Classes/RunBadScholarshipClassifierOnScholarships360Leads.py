from Classes.RunBadScholarshipClassifier import RunBadScholarshipClassifier
from Classes.Scholarships360GetDatabaseInfo import Scholarship360LeadsGetDatabaseInfo


class RunBadScholarshipClassifierOnScholarships360Leads(RunBadScholarshipClassifier):
    def __init__(self):
        scholarships360Info = Scholarship360LeadsGetDatabaseInfo(tag='Scholarship')

        self.sponsorList = []
        self.descriptions = scholarships360Info.getDescriptions()
        self.listScholarships360LeadsIds = scholarships360Info.getScholarships360LeadsIds()
        self.tableName = 'Scholarships360Leads'
        self.idColumnName = 'Scholarship360LeadId'

        RunBadScholarshipClassifier.__init__(self, self.sponsorList, self.descriptions)
        self.getPredictedBadInsertIntoDatabase(self.tableName, self.idColumnName, self.listScholarships360LeadsIds)


RunBadScholarshipClassifierOnScholarships360Leads()
