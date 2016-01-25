from Classes.InsertCheggLeadArrayIntoCheggLeadsDB import InsertCheggLeadArrayIntoCheggLeadsDB
from Classes.CheggLeads import CheggLeads
from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased
from Classes.ClassifyBadScholarships import ClassifyBadScholarships
from Classes.CerebroLogs import CerebroLogs


class ProcessCheggLeads(object):
    @staticmethod
    def getCheggLeadsAndInsertIntoDB():
        cheggLeadsArrays = CheggLeads().loopOverResultsPagesAndDoStuff()
        predictedFundingTypes = ProcessCheggLeads.classifyFunding(cheggLeadsArrays)
        totalLeads = len(cheggLeadsArrays)
        numNewEntries = 0
        numUpdates = 0
        for leadArray, fundingClassification in zip(cheggLeadsArrays, predictedFundingTypes):
            badScholarshipClassification = ProcessCheggLeads.checkBadScholarship(leadArray, fundingClassification)
            newEntryBoolean = InsertCheggLeadArrayIntoCheggLeadsDB(leadArray, fundingClassification,
                                                                   badScholarshipClassification).insertUpdateLead()
            if newEntryBoolean:
                numNewEntries += 1
            else:
                numUpdates += 1
        CerebroLogs('Chegg', totalLeads, numNewEntries, numUpdates)


    @staticmethod
    def classifyFunding(leadsArrays):
        titlesList = [leadArray[0] for leadArray in leadsArrays]
        infoTextList = ['%s %s' % (leadArray[4], leadArray[5]) for leadArray in leadsArrays]
        opportunitiesTitlesAndTexts = [[title, infoText] for title, infoText in zip(titlesList, infoTextList)]
        fundingClassifier = ClassifyFundingTypeKeywordBased(opportunitiesTitlesAndTexts)
        predictedFundingTypes = fundingClassifier.returnPredictedTags()
        return predictedFundingTypes

    @staticmethod
    def checkBadScholarship(leadArray, fundingClassification):
        if fundingClassification == 'Scholarship':
            sponsor = leadArray[7]
            infoText = '%s %s' % (leadArray[4], leadArray[5])
            badScholarshipClassifier = ClassifyBadScholarships()
            badScholarshipPrediction = badScholarshipClassifier.classifyOpportunity(sponsor, infoText)
            return badScholarshipPrediction
        else:
            return ''


ProcessCheggLeads.getCheggLeadsAndInsertIntoDB()

