from Classes.SUDBConnect import SUDBConnect


class ScholarsiteLeadsGetDatabaseInfo(object):
    def __init__(self):
        self.db = SUDBConnect()

    def getScholarsiteLeadsIds(self):
        scholarsiteLeadsIds = []

        rows = self.db.getRows("select * from dbo.ScholarsiteLeads")
        for row in rows:
            scholarsiteLeadsIds.append(row.ScholarsiteLeadId)

        return scholarsiteLeadsIds

    def getNames(self):
        names = []

        rows = self.db.getRows("select * from dbo.ScholarsiteLeads")
        for row in rows:
            names.append(row.Name)

        return names

    def getRequirements(self):
        requirements = []

        rows = self.db.getRows("select * from dbo.ScholarsiteLeads")
        for row in rows:
            requirements.append(row.Requirements)

        return requirements
