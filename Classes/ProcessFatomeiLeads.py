from Classes.FatomeiLeads import FatomeiLeads
from Classes.InsertFatomeiLeadsArrayIntoFatomeiLeadsDB import InsertFatomeiLeadsArrayIntoFatomeiLeadsDB
from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased
from Classes.ClassifyBadScholarships import ClassifyBadScholarships
from Classes.CerebroLogs import CerebroLogs


class ProcessFatomeiLeads(object):
    @staticmethod
    def getFatomeiLeadsAndInsertIntoDB():
        fatomeiLeadsArrays = FatomeiLeads().getFatomeiLeadsArrays()
        predictedFundingTypes = ProcessFatomeiLeads.classifyFunding(fatomeiLeadsArrays)
        totalLeads = len(fatomeiLeadsArrays)
        numNewEntries = 0
        numUpdates = 0
        for leadArray, fundingClassification in zip(fatomeiLeadsArrays, predictedFundingTypes):
            badScholarshipClassification = ProcessFatomeiLeads.checkBadScholarship(leadArray, fundingClassification)
            newEntryBoolean = InsertFatomeiLeadsArrayIntoFatomeiLeadsDB(leadArray, fundingClassification,
                                                                        badScholarshipClassification).insertUpdateLead()
            if newEntryBoolean == True:
                numNewEntries += 1
            else:
                numUpdates += 1
        CerebroLogs('Fatomei', totalLeads, numNewEntries, numUpdates)

    @staticmethod
    def classifyFunding(leadsArrays):
        titlesList = [leadArray[0] for leadArray in leadsArrays]
        infoTextList = [leadArray[1] for leadArray in leadsArrays]
        opportunitiesTitlesAndTexts = [[title, infoText] for title, infoText in zip(titlesList, infoTextList)]
        fundingClassifier = ClassifyFundingTypeKeywordBased(opportunitiesTitlesAndTexts)
        predictedFundingTypes = fundingClassifier.returnPredictedTags()
        return predictedFundingTypes

    @staticmethod
    def checkBadScholarship(leadArray, fundingClassification):
        if fundingClassification == 'Scholarship':
            sponsor = ''
            infoText = leadArray[1]
            badScholarshipClassifier = ClassifyBadScholarships()
            badScholarshipPrediction = badScholarshipClassifier.classifyOpportunity(sponsor, infoText)
            return badScholarshipPrediction
        else:
            return ''

ProcessFatomeiLeads.getFatomeiLeadsAndInsertIntoDB()
