from Classes.InsertCollegeGreenLightLeadArrayIntoCollegeGreenLightDB import \
    InsertCollegeGreenLightLeadArrayIntoCollegeGreenLightDB
from Classes.CollegeGreenLightLeads import CollegeGreenLightLeads
from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased
from Classes.ClassifyBadScholarships import ClassifyBadScholarships
from Classes.CerebroLogs import CerebroLogs


class ProcessCollegeGreenLightLeads(object):
    @staticmethod
    def getCollegeGreenLightLeadsAndInsertIntoDB():
        collegeGreenLightLeadsArrays = CollegeGreenLightLeads().getLeads()
        predictedFundingTypes = ProcessCollegeGreenLightLeads.classifyFunding(collegeGreenLightLeadsArrays)
        totalLeads = len(collegeGreenLightLeadsArrays)
        numNewEntries = 0
        numUpdates = 0
        for leadArray, fundingClassification in zip(collegeGreenLightLeadsArrays, predictedFundingTypes):
            badScholarshipClassification = ProcessCollegeGreenLightLeads.checkBadScholarship(leadArray,
                                                                                             fundingClassification)
            newEntryBoolean = InsertCollegeGreenLightLeadArrayIntoCollegeGreenLightDB(leadArray, fundingClassification,
                                                                                      badScholarshipClassification).insertUpdateLead()
            if newEntryBoolean:
                numNewEntries += 1
            else:
                numUpdates += 1
        CerebroLogs('CollegeGreenLight', totalLeads, numNewEntries, numUpdates)

    @staticmethod
    def classifyFunding(leadsArrays):
        titlesList = [leadArray[0] for leadArray in leadsArrays]
        infoTextList = ['%s %s' % (leadArray[5], leadArray[6]) for leadArray in leadsArrays]
        opportunitiesTitlesAndTexts = [[title, infoText] for title, infoText in zip(titlesList, infoTextList)]
        fundingClassifier = ClassifyFundingTypeKeywordBased(opportunitiesTitlesAndTexts)
        predictedFundingTypes = fundingClassifier.returnPredictedTags()
        return predictedFundingTypes

    @staticmethod
    def checkBadScholarship(leadArray, fundingClassification):
        if fundingClassification == 'Scholarship':
            sponsor = leadArray[3]
            infoText = '%s %s' % (leadArray[5], leadArray[6])
            badScholarshipClassifier = ClassifyBadScholarships()
            badScholarshipPrediction = badScholarshipClassifier.classifyOpportunity(sponsor, infoText)
            return badScholarshipPrediction
        else:
            return ''

ProcessCollegeGreenLightLeads.getCollegeGreenLightLeadsAndInsertIntoDB()
