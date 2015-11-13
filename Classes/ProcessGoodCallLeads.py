from Classes.GoodCallLeads import GoodCallLeads
from Classes.InsertGoodCallLeadArrayIntoGoodCallLeadsDB import InsertGoodCallLeadArrayIntoGoodCallLeadsDB


class ProcessGoodCallLeads(object):
    @staticmethod
    def getGoodCallLeadsAndInsertIntoDB():
        goodCallLeadsArrays = GoodCallLeads().getLeads()
        for leadArray in goodCallLeadsArrays:
            InsertGoodCallLeadArrayIntoGoodCallLeadsDB(leadArray)

# ProcessGoodCallLeads.getGoodCallLeadsAndInsertIntoDB()
