from Classes.RunFundingClassifier import RunFundingClassifier
from Classes.CheggLeadsGetDatabaseInfo import CheggLeadsGetDatabaseInfo


class RunFundingClassiferOnCheggLeads(RunFundingClassifier):
    def __init__(self):
        self.titleConcatenatedEligibilityApplicationOverviewList = CheggLeadsGetDatabaseInfo().getTitleConcatenatedEligibilityAppplictionOverviewList()
        self.listCheggLeadsIds = CheggLeadsGetDatabaseInfo().getCheggLeadsIds()
        self.tableName = 'CheggLeads'
        self.idColumnName = 'CheggLeadId'
        RunFundingClassifier.__init__(self, self.titleConcatenatedEligibilityApplicationOverviewList)

        self.getPredictedTagsInsertIntoDB(self.tableName, self.idColumnName, self.listCheggLeadsIds)


RunFundingClassiferOnCheggLeads()
