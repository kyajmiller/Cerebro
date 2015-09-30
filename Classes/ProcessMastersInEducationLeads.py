from Classes.MastersInEducationLeads import MastersInEducationLeads
from Classes.InsertMastersInEducationArrayIntoDB import InsertMastersInEducationArrayIntoDB


class ProcessMastersInEducationLeads(object):
    @staticmethod
    def getMastersInEducationLeadsAndInsertIntoDB():
        mastersInEducationLeadsArrays = MastersInEducationLeads().getLeads()
        for leadArray in mastersInEducationLeadsArrays:
            InsertMastersInEducationArrayIntoDB(leadArray)


ProcessMastersInEducationLeads.getMastersInEducationLeadsAndInsertIntoDB()
