from Classes.IefaLeads import IefaLeads
from Classes.InsertIefaLeadArrayIntoIefaLeadsDB import InsertIefaLeadArrayIntoIefaLeadsDB


class ProcessIefaLeads(object):
    @staticmethod
    def getIefaLeadsAndInsertIntoDB():
        iefaLeadsArrays = IefaLeads().loopOverResultsPagesAndDoStuff()
        for leadArray in iefaLeadsArrays:
            InsertIefaLeadArrayIntoIefaLeadsDB(leadArray)

# ProcessIefaLeads.getIefaLeadsAndInsertIntoDB()
