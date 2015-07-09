from Classes.InsertGoogleLeadArrayToGoogleLeadsDatabase import InsertGoogleLeadArrayToGoogleLeadsDatabase


class ProcessGoogleLeads(object):
    def __init__(self, arrayOfGoogleLeadsArrays):
        self.arrayOfGoogleLeadsArrays = arrayOfGoogleLeadsArrays

        for googleLeadArray in self.arrayOfGoogleLeadsArrays:
            InsertGoogleLeadArrayToGoogleLeadsDatabase.doInsert(googleLeadArray)
