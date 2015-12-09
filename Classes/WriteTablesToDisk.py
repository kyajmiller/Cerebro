from Classes.SUDBConnect import SUDBConnect
import re


class WriteTablesToDisk(object):
    def __init__(self, tableName, user='Kya'):
        self.tableName = tableName
        self.user = user
        self.website = re.sub('Leads', '', self.tableName)
        self.sqlDB = SUDBConnect(destination='database')
        self.fileDB = SUDBConnect(destination='filesystem')
        self.columns = self.sqlDB.getColumnNamesFromTable(self.tableName)
        self.rows = self.sqlDB.getRowsDB("select * from dbo.%s" % self.tableName)
        self.urls = self.getUrls()

        for row, url in zip(self.rows, self.urls):
            values = row
            self.fileDB.writeFile(self.columns, values, self.user, self.website, url)

    def getUrls(self):
        urls = []
        for row in self.rows:
            urls.append(row.Url)
        return urls

WriteTablesToDisk('CheggLeads', user='Kya')
WriteTablesToDisk('CollegeGreenLightLeads')
