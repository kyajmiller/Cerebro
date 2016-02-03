from Classes.ScholarsiteLeads import ScholarsiteLeads
from Classes.InsertScholarsiteLeadsArrayIntoScholarsiteLeadsDB import InsertScholarsiteLeadsArrayIntoScholarsiteLeadsDB
from Classes.ClassifyBadScholarships import ClassifyBadScholarships
from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased
from Classes.CerebroLogs import CerebroLogs


class ProcessScholarsiteLeads(object):
    @staticmethod
    def getScholarsiteLeadsAndInsertIntoDB():
        scholarsiteLeadsArrays = ScholarsiteLeads().processResultsPages()
        predictedFundingTypes = ProcessScholarsiteLeads.classifyFunding(scholarsiteLeadsArrays)
        totalLeads = len(scholarsiteLeadsArrays)
        numNewEntries = 0
        numUpdates = 0
        for leadArray, fundingClassification in zip(scholarsiteLeadsArrays, predictedFundingTypes):
            badScholarshipClassification = ProcessScholarsiteLeads.checkBadScholarship(leadArray, fundingClassification)
            newEntryBoolean = InsertScholarsiteLeadsArrayIntoScholarsiteLeadsDB(leadArray, fundingClassification,
                                                                                badScholarshipClassification).insertUpdateLead()
            if newEntryBoolean:
                numNewEntries += 1
            else:
                numUpdates += 1
        CerebroLogs('Scholarsite', totalLeads, numNewEntries, numUpdates)

    @staticmethod
    def classifyFunding(leadsArrays):
        titlesList = [leadArray[0] for leadArray in leadsArrays]
        infoTextList = [leadArray[3] for leadArray in leadsArrays]
        opportunitiesTitlesAndTexts = [[title, infoText] for title, infoText in zip(titlesList, infoTextList)]
        fundingClassifier = ClassifyFundingTypeKeywordBased(opportunitiesTitlesAndTexts)
        predictedFundingTypes = fundingClassifier.returnPredictedTags()
        return predictedFundingTypes

    @staticmethod
    def checkBadScholarship(leadArray, fundingClassification):
        if fundingClassification == 'Scholarship':
            sponsor = ''
            infoText = leadArray[3]
            badScholarshipClassifier = ClassifyBadScholarships()
            badScholarshipPrediction = badScholarshipClassifier.classifyOpportunity(sponsor, infoText)
            return badScholarshipPrediction
        else:
            return ''

ProcessScholarsiteLeads.getScholarsiteLeadsAndInsertIntoDB()
