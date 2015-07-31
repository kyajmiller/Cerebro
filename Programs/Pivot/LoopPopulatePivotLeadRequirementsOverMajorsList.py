from PopulatePivotLeadRequirements import PopulatePivotLeadRequirements
from PivotLeadsGetDatabaseInfo import PivotLeadsGetDatabaseInfo


class LoopPopulatePivotLeadRequirementsOverMajorsList(object):
    def __init__(self, numberOfMajors='All'):
        self.numberOfMajors = numberOfMajors

    def getMajorsList(self):
        completeMajorsList = PivotLeadsGetDatabaseInfo.getKeywords(tag='Scholarship')

        if self.numberOfMajors == 'All':
            majorsSlice = completeMajorsList[:]
        else:
            majorsSlice = completeMajorsList[:self.numberOfMajors]

        return majorsSlice

    def run(self):
        listOfMajors = self.getMajorsList()
        PopulatePivotLeadRequirements(listOfMajors)