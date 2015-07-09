from Classes.InsertGoogleLeadArrayToDatabase import InsertGoogleLeadArrayToDatabase


class ProcessGoogleLeads(object):
    def __init__(self, arrayOfGoogleLeadsArrays):
        self.arrayOfGoogleLeadsArrays = arrayOfGoogleLeadsArrays

        for googleLeadArray in self.arrayOfGoogleLeadsArrays:
            InsertGoogleLeadArrayToDatabase.doInsert(googleLeadArray)
