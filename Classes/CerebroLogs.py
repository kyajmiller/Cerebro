from Classes.SUDBConnect import SUDBConnect
import time


class CerebroLogs(object):
    def __init__(self, website, entryType='New'):
        self.website = website
        self.entryType = entryType
        self.date = time.strftime('%Y%m%d')
