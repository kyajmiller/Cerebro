from Classes.GetFastFindMajorsList import GetFastFindMajorsList
from Classes.PivotLeads import PivotLeads
from Classes.ProcessPivotLeads import ProcessPivotLeads


class PivotLeadsRunMajorsList(object):
    def __init__(self, isTest=False):
        self.isTest = isTest
        self.fastFindMajorsList = GetFastFindMajorsList.getPivotLeadsList()

        if self.isTest:
            for major in self.fastFindMajorsList[:5]:
                majorSpecificPivotLeads = PivotLeads(major).processSearchResultsAndMakeLeadArray()
                ProcessPivotLeads(majorSpecificPivotLeads)
        else:
            for major in self.fastFindMajorsList:
                majorSpecificPivotLeads = PivotLeads(major).processSearchResultsAndMakeLeadArray()
                ProcessPivotLeads(majorSpecificPivotLeads)
