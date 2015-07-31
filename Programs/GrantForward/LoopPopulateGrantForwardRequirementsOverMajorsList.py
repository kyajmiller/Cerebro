from PopulateGrantForwardRequirements import PopulateGrantForwardRequirements
from GrantForwardItemsGetDatabaseInfo import GrantForwardItemsGetDatabaseInfo


class LoopPopulateGrantForwardRequirementsOverMajorsList(object):
    def __init__(self, numberOfMajors='All'):
        self.numberOfMajors = numberOfMajors

    def getMajorsList(self):
        completeMajorsList = GrantForwardItemsGetDatabaseInfo.getKeywords(tag='Scholarship')

        if self.numberOfMajors == 'All':
            majorsSlice = completeMajorsList[:]
        else:
            majorsSlice = completeMajorsList[:self.numberOfMajors]

        return majorsSlice

    def run(self):
        listOfMajors = self.getMajorsList()
        PopulateGrantForwardRequirements(listOfMajors)
