from Classes.GetFastFindMajorsList import GetFastFindMajorsList
from Classes.GrantForwardLeads import GrantForwardLeads
from Classes.ProcessGrantForwardLeads import ProcessGrantForwardLeads


class GrantForwardRunMajorsList(object):
    def __init__(self, isTest=False):
        self.isTest = isTest
        self.fastFindMajorsList = GetFastFindMajorsList.getGrantForwardItemsList()

        if self.isTest:
            for major in self.fastFindMajorsList[:5]:
                majorSpecificGrantForwardLeads = GrantForwardLeads(major).processSearchResultsAndMakeLeadArray()
                ProcessGrantForwardLeads(majorSpecificGrantForwardLeads)
        else:
            for major in self.fastFindMajorsList:
                majorSpecificGrantForwardLeads = GrantForwardLeads(major).processSearchResultsAndMakeLeadArray()
                ProcessGrantForwardLeads(majorSpecificGrantForwardLeads)