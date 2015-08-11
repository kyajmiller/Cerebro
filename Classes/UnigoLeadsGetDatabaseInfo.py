from Classes.SUDBConnect import SUDBConnect


class UnigoLeadsGetDatabaseInfo(object):
    def __init__(self):
        self.db = SUDBConnect()

    def getUnigoLeadsIds(self):
        unigoLeadsIds = []

        rows = self.db.getRows("select UnigoLeadId from dbo.UnigoLeads")
        for row in rows:
            unigoLeadsIds.append(row.UnigoLeadId)

        return unigoLeadsIds

    def getRequirements(self):
        requirements = []

        rows = self.db.getRows("select Requirements from dbo.UnigoLeads")
        for row in rows:
            requirements.append(row.Requirements)

        return requirements
