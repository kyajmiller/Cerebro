from Classes.RunBadScholarshipClassifier import RunBadScholarshipClassifier
from Classes.IefaLeadsGetDatabaseInfo import IefaLeadsGetDatabaseInfo


class RunBadScholarshipClassifierOnIefaLeads(RunBadScholarshipClassifier):
    def __init__(self):
        iefaLeadInfo = IefaLeadsGetDatabaseInfo()

        self.sponsorList = iefaLeadInfo.getSponsors()

        self.infoText = iefaLeadInfo.getConcatenatedDescriptionOtherCriteria()
        self.listIefaLeadsIds = iefaLeadInfo.getIefaLeadsIds()
        self.tableName = 'IefaLeads'
        self.idColumnName = 'IefaLeadId'

        RunBadScholarshipClassifier.__init__(self, self.sponsorList, self.infoText)
        self.getPredictedBadInsertIntoDatabase(self.tableName, self.idColumnName, self.listIefaLeadsIds)


RunBadScholarshipClassifierOnIefaLeads()
