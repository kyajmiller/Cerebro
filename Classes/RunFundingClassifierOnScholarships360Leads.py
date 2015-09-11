from Classes.RunFundingClassifier import RunFundingClassifier
from Classes.Scholarships360GetDatabaseInfo import Scholarship360LeadsGetDatabaseInfo


class RunFundingClassifierOnScholarships360Leads(RunFundingClassifier):
    def __init__(self):
        scholarships360Info = Scholarship360LeadsGetDatabaseInfo()

        self.titleDescriptionsList = scholarships360Info.getTitleDescriptionList()
        self.listScholarships360LeadsIds = scholarships360Info.getScholarships360LeadsIds()
        self.tableName = 'Scholarships360Leads'
        self.idColumnName = 'Scholarship360LeadId'

        RunFundingClassifier.__init__(self, self.titleDescriptionsList)
        self.getPredictedTagsInsertIntoDB(self.tableName, self.idColumnName, self.listScholarships360LeadsIds)


RunFundingClassifierOnScholarships360Leads()
