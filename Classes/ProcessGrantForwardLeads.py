from Classes.InsertGrantForwardLeadsArrayIntoGrantForwardItems import InsertGrantForwardLeadsArrayIntoGrantForwardItems
from Classes.GrantForwardLeads import GrantForwardLeads
from Classes.GetFastFindMajorsList import GetFastFindMajorsList
from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased
from Classes.ClassifyBadScholarships import ClassifyBadScholarships
from Classes.CerebroLogs import CerebroLogs


class ProcessGrantForwardLeads(object):
    def __init__(self, arrayOfGrantForwardLeads):
        self.arrayOfGrantForwardLeads = arrayOfGrantForwardLeads

        for grantForwardLeadArray in self.arrayOfGrantForwardLeads:
            InsertGrantForwardLeadsArrayIntoGrantForwardItems(grantForwardLeadArray)

    @staticmethod
    def getGrantForwardLeadsInsertIntoDB():
        majorsList = GetFastFindMajorsList.getGrantForwardItemsList()
        for major in majorsList:
            grantForwardLeadsArrays = GrantForwardLeads(major).processSearchResultsAndMakeLeadArray()

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
