from Classes.InsertGrantForwardLeadsArrayIntoGrantForwardItems import InsertGrantForwardLeadsArrayIntoGrantForwardItems


class ProcessGrantForwardLeads(object):
    def __init__(self, arrayOfGrantForwardLeads):
        self.arrayOfGrantForwardLeads = arrayOfGrantForwardLeads

        for grantForwardLeadArray in self.arrayOfGrantForwardLeads:
            InsertGrantForwardLeadsArrayIntoGrantForwardItems(grantForwardLeadArray)
