from Classes.GoodCallLeads import GoodCallLeads
from Classes.InsertGoodCallLeadArrayIntoGoodCallLeadsDB import InsertGoodCallLeadArrayIntoGoodCallLeadsDB
from Classes.ClassifyBadScholarships import ClassifyBadScholarships
from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased


class ProcessGoodCallLeads(object):
    @staticmethod
    def getGoodCallLeadsAndInsertIntoDB():
        goodCallLeadsArrays = GoodCallLeads().getLeads()
        for leadArray in goodCallLeadsArrays:
            InsertGoodCallLeadArrayIntoGoodCallLeadsDB(leadArray)

    @staticmethod
    def classifyFunding(leadsArrays):
        titlesList = [leadArray[0] for leadArray in leadsArrays]
        infoTextList = [leadArray[4] for leadArray in leadsArrays]
        opportunitiesTitlesAndTexts = [[title, infoText] for title, infoText in zip(titlesList, infoTextList)]
        fundingClassifier = ClassifyFundingTypeKeywordBased(opportunitiesTitlesAndTexts)
        predictedFundingTypes = fundingClassifier.returnPredictedTags()
        return predictedFundingTypes

    @staticmethod
    def checkBadScholarship(leadArray, fundingClassification):
        if fundingClassification == 'Scholarship':
            sponsor = leadArray[5]
            infoText = leadArray[4]
            badScholarshipClassifier = ClassifyBadScholarships()
            badScholarshipPrediction = badScholarshipClassifier.classifyOpportunity(sponsor, infoText)
            return badScholarshipPrediction
        else:
            return ''


ProcessGoodCallLeads.getGoodCallLeadsAndInsertIntoDB()
