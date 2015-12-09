from Classes.InsertCheggLeadArrayIntoCheggLeadsDB import InsertCheggLeadArrayIntoCheggLeadsDB
from Classes.CheggLeads import CheggLeads


class ProcessCheggLeads(object):
    @staticmethod
    def getCheggLeadsAndInsertIntoDB():
        cheggLeadsArrays = CheggLeads().loopOverResultsPagesAndDoStuff()
        for leadArray in cheggLeadsArrays:
            InsertCheggLeadArrayIntoCheggLeadsDB(leadArray)


ProcessCheggLeads.getCheggLeadsAndInsertIntoDB()
