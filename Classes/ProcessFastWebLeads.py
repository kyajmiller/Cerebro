from Classes.InsertFastWebLeadsIntoFastWebLeadsDB import InsertFastWebLeadIntoFastWebLeadsDB
from Classes.FastWebLeads import FastWebLeads


class ProcessFastWebLeads(object):
    @staticmethod
    def getFastWebLeadsAndInsertIntoDB():
        fastWebLeadsArrays = FastWebLeads().getLeads()
        for leadArray in fastWebLeadsArrays:
            InsertFastWebLeadIntoFastWebLeadsDB(leadArray)


ProcessFastWebLeads.getFastWebLeadsAndInsertIntoDB()
