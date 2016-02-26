from Classes.SUDBConnect import SUDBConnect
import time


class CerebroLogs(object):
    def __init__(self, website, totalNewUpdated, numNewEntries, numUpdates, useDifferentWebsiteName=False):
        self.website = website
        self.totalEntries = str(totalNewUpdated)
        self.numNew = str(numNewEntries)
        self.numUpdates = str(numUpdates)
        self.useDifferentWebsiteName = useDifferentWebsiteName
        self.date = time.strftime('%Y%m%d')
        self.db = SUDBConnect()

        totalLeadsInTable = self.getTotalLeadsInTable()

        self.db.insertUpdateOrDeleteDB(
                "insert into dbo.CerebroLogs (Website, Date, New, Updated, TotalNewUpdated, TotalLeads) values ('" + self.website + "', '" + self.date + "', '" + self.numNew + "', '" + self.numUpdates + "', '" + self.totalEntries + "', '" + totalLeadsInTable + "')")

    def getTotalLeadsInTable(self):
        tableName = '%sLeads' % self.website
        rows = self.db.getRowsDB("select * from dbo.%s" % tableName)
        return str(len(rows))
