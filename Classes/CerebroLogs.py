from Classes.SUDBConnect import SUDBConnect
import time


class CerebroLogs(object):
    def __init__(self, website, totalNewUpdated, numNewEntries, numUpdates, useDifferentWebsiteName=False):
        self.website = website
        self.totalEntriesStr = str(totalNewUpdated)
        self.numNew = str(numNewEntries)
        self.numUpdates = str(numUpdates)
        self.useDifferentWebsiteName = useDifferentWebsiteName
        self.date = time.strftime('%Y%m%d')
        self.db = SUDBConnect()

        totalLeadsInTable = self.getTotalLeadsInTable()

        if totalNewUpdated > 0:
            if not self.useDifferentWebsiteName:
                self.db.insertUpdateOrDeleteDB(
                        "insert into dbo.CerebroLogs (Website, Date, New, Updated, TotalNewUpdated, TotalLeads) values ('" + self.website + "', '" + self.date + "', '" + self.numNew + "', '" + self.numUpdates + "', '" + self.totalEntriesStr + "', '" + totalLeadsInTable + "')")
            else:
                self.db.insertUpdateOrDeleteDB(
                        "insert into dbo.CerebroLogs (Website, Date, New, Updated, TotalNewUpdated, TotalLeads) values ('" + self.useDifferentWebsiteName + "', '" + self.date + "', '" + self.numNew + "', '" + self.numUpdates + "', '" + self.totalEntriesStr + "', '" + totalLeadsInTable + "')")

    def getTotalLeadsInTable(self):
        tableName = '%sLeads' % self.website
        rows = self.db.getRowsDB("select * from dbo.%s" % tableName)
        return str(len(rows))
