from Classes.FatomeiLeads import FatomeiLeads
from Classes.InsertFatomeiLeadsArrayIntoFatomeiLeadsDB import InsertFatomeiLeadsArrayIntoFatomeiLeadsDB


class ProcessFatomeiLeads(object):
    @staticmethod
    def getFatomeiLeadsAndInsertIntoDB():
        fatomeiLeadsArrays = FatomeiLeads().getFatomeiLeadsArrays()
        for leadArray in fatomeiLeadsArrays:
            InsertFatomeiLeadsArrayIntoFatomeiLeadsDB(leadArray)


ProcessFatomeiLeads.getFatomeiLeadsAndInsertIntoDB()
