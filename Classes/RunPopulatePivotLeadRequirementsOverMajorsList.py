import random
from Classes.PopulatePivotLeadRequirements import PopulatePivotLeadRequirements
from Classes.PivotLeadsGetDatabaseInfo import PivotLeadsGetDatabaseInfo


class RunPopulatePivotLeadRequirementsOverMajorsList(object):
    def __init__(self, numberOfMajors='All', randomSliceStart=False):
        self.randomSliceStart = randomSliceStart
        self.numberOfMajors = numberOfMajors

        self.listOfMajors = self.getMajorsList()

    def getMajorsList(self):
        completeMajorsList = PivotLeadsGetDatabaseInfo.getKeywords(tag='Scholarship')
        majorsSlice = []

        if self.numberOfMajors == 'All':
            majorsSlice = completeMajorsList[:]
        else:
            majorsSlice = completeMajorsList[:self.numberOfMajors]

        return majorsSlice

    def runPopulatePivotLeadRequirements(self):
