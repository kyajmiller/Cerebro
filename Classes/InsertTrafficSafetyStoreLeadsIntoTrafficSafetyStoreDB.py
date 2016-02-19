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

        self.name = trafficSafetyStoreLeadArray[0]
        self.description = trafficSafetyStoreLeadArray[1]
        self.eligibility = trafficSafetyStoreLeadArray[2]
        self.award = trafficSafetyStoreLeadArray[3]
        self.deadline = trafficSafetyStoreLeadArray[4]
        self.sourceWebsite = trafficSafetyStoreLeadArray[5]
        self.sourceText = trafficSafetyStoreLeadArray[6]
