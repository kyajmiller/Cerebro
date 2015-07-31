from Classes.PopulateGrantForwardRequirements import PopulateGrantForwardRequirements
from Classes.GrantForwardItemsGetDatabaseInfo import GrantForwardItemsGetDatabaseInfo


class LoopPopulateGrantForwardRequirementsOverMajorsList(object):
    def __init__(self, majorsToRun='All'):
        self.majorsToRun = majorsToRun

    def getMajorsList(self):
        completeMajorsList = GrantForwardItemsGetDatabaseInfo.getKeywords(tag='Scholarship')

        if self.majorsToRun == 'All':
            majorsList = completeMajorsList[:]
        else:
            majorsList = []
            for major in self.majorsToRun:
                if major in completeMajorsList:
                    majorsList.append(major)

        return majorsList

    def run(self):
        listOfMajors = self.getMajorsList()
        PopulateGrantForwardRequirements(listOfMajors)
