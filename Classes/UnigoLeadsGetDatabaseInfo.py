from Classes.SUDBConnect import SUDBConnect


class UnigoLeadsGetDatabaseInfo(object):
    def __init__(self):
        self.db = SUDBConnect()

    def getUnigoLeadsIds(self):
        unigoLeadsIds = []

        rows = self.db.getRowsDB("select UnigoLeadId from dbo.UnigoLeads")
        for row in rows:
            unigoLeadsIds.append(row.UnigoLeadId)

        return unigoLeadsIds

    def getRequirements(self):
        requirements = []

        rows = self.db.getRowsDB("select Requirements from dbo.UnigoLeads")
        for row in rows:
            requirements.append(row.Requirements)

        return requirements

    def getSponsors(self):
        sponsors = []

        rows = self.db.getRowsDB("select * from dbo.UnigoLeads")
        for row in rows:
            sponsors.append(row.Sponsor)

        return sponsors

    def getAdditionalInfo(self):
        additionalInfo = []

        rows = self.db.getRowsDB("select * from dbo.UnigoLeads")
        for row in rows:
            additionalInfo.append(row.AdditionalInfo)

        return additionalInfo
