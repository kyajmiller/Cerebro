from Classes.InsertUnigoLeadArrayIntoUnigoLeadsDB import InsertUnigoLeadArrayIntoUnigoLeadsDB
from Classes.UnigoLeads import UnigoLeads


class ProcessUnigoLeads(object):
    @staticmethod
    def getUnigoLeadsAndInsertIntoDB():
        unigoLeadsArrays = UnigoLeads().getLeads()
        for leadArray in unigoLeadsArrays:
            InsertUnigoLeadArrayIntoUnigoLeadsDB(leadArray)


ProcessUnigoLeads.getUnigoLeadsAndInsertIntoDB()
