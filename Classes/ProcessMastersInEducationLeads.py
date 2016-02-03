from Classes.MastersInEducationLeads import MastersInEducationLeads
from Classes.InsertMastersInEducationArrayIntoDB import InsertMastersInEducationArrayIntoDB
from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased
from Classes.ClassifyBadScholarships import ClassifyBadScholarships
from Classes.CerebroLogs import CerebroLogs


class ProcessMastersInEducationLeads(object):
    @staticmethod
    def getMastersInEducationLeadsAndInsertIntoDB():
        mastersInEducationLeadsArrays = MastersInEducationLeads().getLeads()
        predictedFundingTypes = ProcessMastersInEducationLeads.classifyFunding(mastersInEducationLeadsArrays)
        totalLeads = len(mastersInEducationLeadsArrays)
        numNewEntries = 0
        numUpdates = 0
        for leadArray, fundingClassification in zip(mastersInEducationLeadsArrays, predictedFundingTypes):
            badScholarshipClassification = ProcessMastersInEducationLeads.checkBadScholarship(leadArray,
                                                                                              fundingClassification)
            newEntryBoolean = InsertMastersInEducationArrayIntoDB(leadArray, fundingClassification,
                                                                  badScholarshipClassification).insertUpdateLead()
            if newEntryBoolean:
                numNewEntries += 1
            else:
                numUpdates += 1
        CerebroLogs('MastersInEducation', totalLeads, numNewEntries, numUpdates)

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


ProcessMastersInEducationLeads.getMastersInEducationLeadsAndInsertIntoDB()
