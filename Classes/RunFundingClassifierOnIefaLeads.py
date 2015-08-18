from Classes.RunFundingClassifier import RunFundingClassifier
from Classes.IefaLeadsGetDatabaseInfo import IefaLeadsGetDatabaseInfo


class RunFundingClassifierOnIefaLeads(RunFundingClassifier):
    def __init__(self):
        self.titleConcatenatedDescriptionOtherCriteriaList = IefaLeadsGetDatabaseInfo().getTitleConcatenatedDescriptionOtherCriteriaList()
        self.listIefaLeadsIds = IefaLeadsGetDatabaseInfo().getIefaLeadsIds()
        self.tableName = 'IefaLeads'
        self.idColumnName = 'IefaLeadId'
        RunFundingClassifier.__init__(self, self.titleConcatenatedDescriptionOtherCriteriaList)

        self.getPredictedTagsInsertIntoDB(self.tableName, self.idColumnName, self.listIefaLeadsIds)


RunFundingClassifierOnIefaLeads()
