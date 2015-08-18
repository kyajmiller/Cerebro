from Classes.RunFundingClassifier import RunFundingClassifier
from Classes.FatomeiLeadsGetDatabaseInfo import FatomeiLeadsGetDatabaseInfo


class RunFundingClassifierOnFatomeiLeads(RunFundingClassifier):
    def __init__(self):
        self.titleDescriptionList = FatomeiLeadsGetDatabaseInfo().getTitleDescriptionList()
        self.listFatomeiLeadsIds = FatomeiLeadsGetDatabaseInfo().getFatomeiLeadIds()
        self.tableName = 'FatomeiLeads'
        self.idColumnName = 'FatomeiLeadId'
        RunFundingClassifier.__init__(self, self.titleDescriptionList)

        self.getPredictedTagsInsertIntoDB(self.tableName, self.idColumnName, self.listFatomeiLeadsIds)


RunFundingClassifierOnFatomeiLeads()
