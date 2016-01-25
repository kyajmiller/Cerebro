from Classes.SUDBConnect import SUDBConnect
import time


class CerebroLogs(object):
    def __init__(self, website, totalEntries, numNewEntries, numUpdates):
        self.website = website
        self.totalEntries = str(totalEntries)
        self.numNew = str(numNewEntries)
        self.numUpdates = str(numUpdates)
        self.date = time.strftime('%Y%m%d')
        self.db = SUDBConnect()

        self.db.insertUpdateOrDeleteDB(
            "insert into dbo.CerebroLogs (Website, Date, New, Updated, Total) values ('" + self.website + "', '" + self.date + "', '" + self.numNew + "', '" + self.numUpdates + "', '" + self.totalEntries + "')")
