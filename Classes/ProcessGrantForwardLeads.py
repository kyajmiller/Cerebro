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
            predictedFundingTypes = ProcessGrantForwardLeads.classifyFunding(grantForwardLeadsArrays)

    @staticmethod
    def classifyFunding(leadsArrays):
        titlesList = [leadArray[2] for leadArray in leadsArrays]
        infoTextList = ['%s %s %s' % (leadArray[3], leadArray[6], leadArray[7]) for leadArray in leadsArrays]
        opportunitiesTitlesAndTexts = [[title, infoText] for title, infoText in zip(titlesList, infoTextList)]
        fundingClassifier = ClassifyFundingTypeKeywordBased(opportunitiesTitlesAndTexts)
        predictedFundingTypes = fundingClassifier.returnPredictedTags()
        return predictedFundingTypes

    @staticmethod
    def checkBadScholarship(leadArray, fundingClassification):
        if fundingClassification == 'Scholarship':
            sponsor = leadArray[4]
            infoText = '%s %s %s' % (leadArray[3], leadArray[6], leadArray[7])
            badScholarshipClassifier = ClassifyBadScholarships()
            badScholarshipPrediction = badScholarshipClassifier.classifyOpportunity(sponsor, infoText)
            return badScholarshipPrediction
        else:
            return ''
