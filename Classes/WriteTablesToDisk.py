from Classes.SUDBConnect import SUDBConnect
import re


class WriteTablesToDisk(object):
    def __init__(self, tableName, user):
        self.tableName = tableName
        self.user = user
        self.website = re.sub('Leads', '', self.tableName)
        self.sqlDB = SUDBConnect(destination='database')
        self.fileDB = SUDBConnect(destination='filesystem')
        self.columns = self.sqlDB.getColumnNamesFromTable(self.tableName)
        self.rows = self.sqlDB.getRowsDB("select * from dbo.%s" % self.tableName)
        self.urls = self.sqlDB.getRowsDB("select Url from dbo.%s" % self.tableName)

        for row, url in zip(self.rows, self.urls):
            values = row
            self.fileDB.writeFile(self.columns, values, self.user, self.website, url)


WriteTablesToDisk('CheggLeads', user='Kya')
