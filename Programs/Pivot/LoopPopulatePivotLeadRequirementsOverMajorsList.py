from PopulatePivotLeadRequirements import PopulatePivotLeadRequirements
from PivotLeadsGetDatabaseInfo import PivotLeadsGetDatabaseInfo


class LoopPopulatePivotLeadRequirementsOverMajorsList(object):
    def __init__(self, majorsToRun):
        self.majorsToRun = majorsToRun

    def getMajorsList(self):
        completeMajorsList = PivotLeadsGetDatabaseInfo.getKeywords(tag='Scholarship')

        if self.majorsToRun == 'All':
            majorsList = completeMajorsList[:]
        else:
            majorsList = self.majorsToRun

        return majorsList

    def run(self):
        listOfMajors = self.getMajorsList()
        PopulatePivotLeadRequirements(listOfMajors)