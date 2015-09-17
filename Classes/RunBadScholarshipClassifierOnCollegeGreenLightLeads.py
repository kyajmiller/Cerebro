from Classes.RunBadScholarshipClassifier import RunBadScholarshipClassifier
from Classes.CollegeGreenLightLeadsGetDatabaseInfo import CollegeGreenLightLeadsGetDatabaseInfo


class RunBadScholarshipClassifierOnCollegeGreenLightLeads(RunBadScholarshipClassifier):
    def __init__(self):
        collegeGreenLightInfo = CollegeGreenLightLeadsGetDatabaseInfo()

        self.sponsorList = collegeGreenLightInfo.getSponsors()
        self.descriptions = collegeGreenLightInfo.getDescriptions()
        self.listCollegeGreenLightLeadsIds = collegeGreenLightInfo.getCollegeGreenLightLeadsIds()
        self.tableName = 'CollegeGreenLightLeads'
        self.idColumnName = 'CollegeGreenLightLeadId'

        RunBadScholarshipClassifier.__init__(self, self.sponsorList, self.descriptions)
        self.getPredictedBadInsertIntoDatabase(self.tableName, self.idColumnName, self.listCollegeGreenLightLeadsIds)


RunBadScholarshipClassifierOnCollegeGreenLightLeads()
