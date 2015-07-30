from Classes.PopulatePivotLeadRequirements import PopulatePivotLeadRequirements
from Classes.PivotLeadsGetDatabaseInfo import PivotLeadsGetDatabaseInfo


class RunPopulatePivotLeadRequirementsOverMajorsList(object):
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
