import time
import re
from Classes.SUDBConnect import SUDBConnect


class InsertTrafficSafetyStoreLeadsIntoTrafficSafetyStoreDB(object):
    def __init__(self, trafficSafetyStoreLeadArray, fundingClassification, badScholarshipClassification):
        self.trafficSafetyStoreLeadArray = trafficSafetyStoreLeadArray
        self.fundingClassification = fundingClassification
        self.badScholarshipClassification = badScholarshipClassification
        self.db = SUDBConnect()
        self.fileSystemDB = SUDBConnect(destination='filesystem')
