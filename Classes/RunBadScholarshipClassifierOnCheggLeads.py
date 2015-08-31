from Classes.RunBadScholarshipClassifier import RunBadScholarshipClassifier
from Classes.CheggLeadsGetDatabaseInfo import CheggLeadsGetDatabaseInfo


class RunBadScholarshipClassifierOnCheggLeads(RunBadScholarshipClassifier):
    def __init__(self):
        cheggDBInfo = CheggLeadsGetDatabaseInfo(tag='Scholarship')

        self.sponsorList = cheggDBInfo.getSponsors()

        self.descriptions = cheggDBInfo.getDescriptions()
        self.eligibility = cheggDBInfo.getEligibilities()
        self.applicationOverview = cheggDBInfo.getApplicationOverviews()
        self.textList = []

        for i in range(len(self.descriptions)):
            description = self.descriptions[i]
            eligibility = self.eligibility[i]
            applicationOverview = self.applicationOverview[i]

            infoText = '%s %s %s' % (eligibility, applicationOverview, description)
            self.textList.append(infoText)

        self.listCheggLeadsIds = cheggDBInfo.getCheggLeadsIds()
        self.tableName = 'CheggLeads'
        self.idColumnName = 'CheggLeadId'

        RunBadScholarshipClassifier.__init__(self, self.sponsorList, self.textList)
        self.getPredictedBadInsertIntoDatabase(self.tableName, self.idColumnName, self.listCheggLeadsIds)


RunBadScholarshipClassifierOnCheggLeads()
