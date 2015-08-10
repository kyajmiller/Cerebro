from Classes.InsertCollegeGreenLightLeadArrayIntoCollegeGreenLightDB import \
    InsertCollegeGreenLightLeadArrayIntoCollegeGreenLightDB
from Classes.CollegeGreenLightLeads import CollegeGreenLightLeads


class ProcessCollegeGreenLightLeads(object):
    @staticmethod
    def getCollegeGreenLightLeadsAndInsertIntoDB():
        collegeGreenLightLeadsArrays = CollegeGreenLightLeads().getLeads()
        for leadArray in collegeGreenLightLeadsArrays:
            InsertCollegeGreenLightLeadArrayIntoCollegeGreenLightDB(leadArray)


ProcessCollegeGreenLightLeads.getCollegeGreenLightLeadsAndInsertIntoDB()
