from Classes.RunFundingClassifier import RunFundingClassifier
from Classes.FastWebLeadsGetDatabaseInfo import FastWebLeadsGetDatabaseInfo


class RunFundingClassifierOnFastWebLeads(RunFundingClassifier):
    def __init__(self):
        self.titleInfoList = FastWebLeadsGetDatabaseInfo().getTitleConcatenatedDescriptionSourceTextList()
        self.listFastWebLeadsIds = FastWebLeadsGetDatabaseInfo().getFastWebLeadsIds()
        self.tableName = 'FastWebLeads'
        self.idColumnName = 'FastWebLeadId'
        RunFundingClassifier.__init__(self, self.titleInfoList)

        self.getPredictedTagsInsertIntoDB(self.tableName, self.idColumnName, self.listFastWebLeadsIds)


RunFundingClassifierOnFastWebLeads()
