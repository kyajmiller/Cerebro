from Classes.RunFundingClassifier import RunFundingClassifier
from Classes.MastersInEducationLeadsGetDatabaseInfo import MastersInEducationLeadsGetDatabaseInfo


class RunFundingClassifierOnMastersInEducationLeads(RunFundingClassifier):
    def __init__(self):
        self.titleDescriptionList = MastersInEducationLeadsGetDatabaseInfo().getTitleDescriptionList()
        self.listMIELeadsIds = MastersInEducationLeadsGetDatabaseInfo().getMastersInEducationLeadIds()
        self.tableName = 'MastersInEducationLeads'
        self.idColumnName = 'MastersInEducationLeadId'

        RunFundingClassifier.__init__(self, self.titleDescriptionList)

        self.getPredictedTagsInsertIntoDB(self.tableName, self.idColumnName, self.listMIELeadsIds)


RunFundingClassifierOnMastersInEducationLeads()
