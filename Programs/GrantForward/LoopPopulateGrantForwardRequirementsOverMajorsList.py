from PopulateGrantForwardRequirements import PopulateGrantForwardRequirements
from GrantForwardItemsGetDatabaseInfo import GrantForwardItemsGetDatabaseInfo


class LoopPopulateGrantForwardRequirementsOverMajorsList(object):
    def __init__(self, majorsToRun):
        self.majorsToRun = majorsToRun

    def getMajorsList(self):
        completeMajorsList = GrantForwardItemsGetDatabaseInfo.getKeywords(tag='Scholarship')

        if self.majorsToRun == 'All':
            majorsList = completeMajorsList[:]
        else:
            majorsList = self.majorsToRun

        return majorsList

    def run(self):
        listOfMajors = self.getMajorsList()
        PopulateGrantForwardRequirements(listOfMajors)


LoopPopulateGrantForwardRequirementsOverMajorsList(['Chemistry']).run()
