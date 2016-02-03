from Classes.ScholarsiteLeads import ScholarsiteLeads
from Classes.InsertScholarsiteLeadsArrayIntoScholarsiteLeadsDB import InsertScholarsiteLeadsArrayIntoScholarsiteLeadsDB


class ProcessScholarsiteLeads(object):
    @staticmethod
    def getScholarsiteLeadsAndInsertIntoDB():
        scholarsiteLeadsArrays = ScholarsiteLeads().processResultsPages()
        for leadArray in scholarsiteLeadsArrays:
            InsertScholarsiteLeadsArrayIntoScholarsiteLeadsDB(leadArray)


ProcessScholarsiteLeads.getScholarsiteLeadsAndInsertIntoDB()
