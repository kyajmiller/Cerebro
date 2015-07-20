from Classes.InsertPivotLeadsArrayIntoPivotLeadsDB import InsertPivotLeadsArrayIntoPivotLeadsDB


class ProcessPivotLeads(object):
    def __init__(self, arrayOfPivotLeads):
        self.arrayOfPivotLeads = arrayOfPivotLeads

        for pivotLeadArray in self.arrayOfPivotLeads:
            InsertPivotLeadsArrayIntoPivotLeadsDB(pivotLeadArray)
