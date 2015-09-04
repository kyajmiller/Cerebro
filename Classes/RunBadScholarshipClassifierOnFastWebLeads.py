from Classes.RunBadScholarshipClassifier import RunBadScholarshipClassifier
from Classes.FastWebLeadsGetDatabaseInfo import FastWebLeadsGetDatabaseInfo


class RunBadScholarshipClassifierOnFastWebLeads(RunBadScholarshipClassifier):
    def __init__(self):
        fastWebInfo = FastWebLeadsGetDatabaseInfo()

        self.sponsorList = fastWebInfo.getSponsors()
        self.descriptions = fastWebInfo.getDescriptions()
        self.listFastWebLeadIds = fastWebInfo.getFastWebLeadsIds()
        self.tableName = 'FastWebLeads'
        self.idColumnName = 'FastWebLeadId'

        RunBadScholarshipClassifier.__init__(self, self.sponsorList, self.descriptions)
        self.getPredictedBadInsertIntoDatabase(self.tableName, self.idColumnName, self.listFastWebLeadIds)


RunBadScholarshipClassifierOnFastWebLeads()
