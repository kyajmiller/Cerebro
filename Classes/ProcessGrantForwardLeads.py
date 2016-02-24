from Classes.InsertGrantForwardLeadsArrayIntoGrantForwardItems import InsertGrantForwardLeadsArrayIntoGrantForwardItems
from Classes.GrantForwardLeads import GrantForwardLeads
from Classes.GetFastFindMajorsList import GetFastFindMajorsList
from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased
from Classes.ClassifyBadScholarships import ClassifyBadScholarships
from Classes.CerebroLogs import CerebroLogs


class ProcessGrantForwardLeads(object):
    def __init__(self, arrayOfGrantForwardLeads):
        self.arrayOfGrantForwardLeads = arrayOfGrantForwardLeads

        for grantForwardLeadArray in self.arrayOfGrantForwardLeads:
            InsertGrantForwardLeadsArrayIntoGrantForwardItems(grantForwardLeadArray)
