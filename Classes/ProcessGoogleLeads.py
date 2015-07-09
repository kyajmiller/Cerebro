from Classes.InsertGoogleLeadArrayIntoGoogleLeadsDatabase import InsertGoogleLeadArrayIntoGoogleLeadsDatabase


class ProcessGoogleLeads(object):
    def __init__(self, arrayOfGoogleLeadsArrays):
        self.arrayOfGoogleLeadsArrays = arrayOfGoogleLeadsArrays

        for googleLeadArray in self.arrayOfGoogleLeadsArrays:
            InsertGoogleLeadArrayIntoGoogleLeadsDatabase(googleLeadArray)
