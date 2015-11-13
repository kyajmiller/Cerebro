from Classes.InsertScholarships360LeadArrayIntoScholarships360DB import \
    InsertScholarships360LeadArrayIntoScholarships360DB
from Classes.Scholarships360Leads import Scholarships360Leads


class ProcessScholarships360Leads(object):
    @staticmethod
    def getScholarships360LeadsAndInsertIntoDatabase():
        arrayOfScholarship360Leads = Scholarships360Leads().getLeads()
        for leadArray in arrayOfScholarship360Leads:
            InsertScholarships360LeadArrayIntoScholarships360DB(leadArray)

# ProcessScholarships360Leads.getScholarships360LeadsAndInsertIntoDatabase()
