from Classes.InsertTrafficSafetyStoreLeadsIntoTrafficSafetyStoreDB import \
    InsertTrafficSafetyStoreLeadsIntoTrafficSafetyStoreDB
from Classes.TrafficSafetyStoreLeads import TrafficSafetyStoreLeads
from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased
from Classes.ClassifyBadScholarships import ClassifyBadScholarships
from Classes.CerebroLogs import CerebroLogs


class ProcessTrafficSafetyStoreLeads(object):
    @staticmethod
    def getTrafficSafetyStoreLeadsAndInsertIntoDB():
        trafficSafetyStoreLeadArrays = TrafficSafetyStoreLeads().getLeads()

    @staticmethod
    def classifyFunding(leadsArrays):
        titlesList = [leadArray[0] for leadArray in leadsArrays]
        infoTextList = ['%s %s' % (leadArray[1], leadArray[2]) for leadArray in leadsArrays]
        opportunitiesTitlesAndTexts = [[title, infoText] for title, infoText in zip(titlesList, infoTextList)]
        fundingClassifier = ClassifyFundingTypeKeywordBased(opportunitiesTitlesAndTexts)
        predictedFundingTypes = fundingClassifier.returnPredictedTags()
        return predictedFundingTypes

    @staticmethod
    def checkBadScholarship(leadArray, fundingClassification):
        if fundingClassification == 'Scholarship':
            sponsor = leadArray[7]
            infoText = '%s %s' % (leadArray[1], leadArray[2])
            badScholarshipClassifier = ClassifyBadScholarships()
            badScholarshipPrediction = badScholarshipClassifier.classifyOpportunity(sponsor, infoText)
            return badScholarshipPrediction
        else:
            return ''
