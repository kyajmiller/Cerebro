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
        predictedFundingTypes = ProcessTrafficSafetyStoreLeads.classifyFunding(trafficSafetyStoreLeadArrays)
        totalLeads = len(trafficSafetyStoreLeadArrays)
        numNewEntries = 0
        numUpdates = 0
        for leadArray, fundingClassification in zip(trafficSafetyStoreLeadArrays, predictedFundingTypes):
            badScholarshipClassification = ProcessTrafficSafetyStoreLeads.checkBadScholarship(leadArray,
                                                                                              fundingClassification)
            newEntryBoolean = InsertTrafficSafetyStoreLeadsIntoTrafficSafetyStoreDB(leadArray, fundingClassification,
                                                                                    badScholarshipClassification).insertUpdateLead()
            if newEntryBoolean:
                numNewEntries += 1
            else:
                numUpdates += 1
        CerebroLogs('TrafficSafetyStore', totalLeads, numNewEntries, numUpdates)


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
            sponsor = ''
            infoText = '%s %s' % (leadArray[1], leadArray[2])
            badScholarshipClassifier = ClassifyBadScholarships()
            badScholarshipPrediction = badScholarshipClassifier.classifyOpportunity(sponsor, infoText)
            return badScholarshipPrediction
        else:
            return ''


ProcessTrafficSafetyStoreLeads.getTrafficSafetyStoreLeadsAndInsertIntoDB()
