from Classes.SUDBConnect import SUDBConnect
import re


class WriteTablesToDisk(object):
    def __init__(self, tableName):
        self.tableName = tableName
        self.website = re.sub('Leads', '', self.tableName)
