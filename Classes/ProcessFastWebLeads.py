from Classes.InsertFastWebLeadsIntoFastWebLeadsDB import InsertFastWebLeadIntoFastWebLeadsDB
from Classes.FastWebLeads import FastWebLeads
from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased
from Classes.ClassifyBadScholarships import ClassifyBadScholarships


class ProcessFastWebLeads(object):
    @staticmethod
    def getFastWebLeadsAndInsertIntoDB():
        fastWebLeadsArrays = FastWebLeads().getLeads()
        predictedFundingTypes = ProcessFastWebLeads.classifyFunding(fastWebLeadsArrays)
        for leadArray, fundingClassification in zip(fastWebLeadsArrays, predictedFundingTypes):
            badScholarshipClassification = ProcessFastWebLeads.checkBadScholarship(leadArray, fundingClassification)
            InsertFastWebLeadIntoFastWebLeadsDB(leadArray, fundingClassification, badScholarshipClassification)

    @staticmethod
    def classifyFunding(leadsArrays):
        titlesList = [leadArray[0] for leadArray in leadsArrays]
        infoTextList = [leadArray[5] for leadArray in leadsArrays]
        opportunitiesTitlesAndTexts = [[title, infoText] for title, infoText in zip(titlesList, infoTextList)]
        fundingClassifier = ClassifyFundingTypeKeywordBased(opportunitiesTitlesAndTexts)
        predictedFundingTypes = fundingClassifier.returnPredictedTags()
        return predictedFundingTypes

    @staticmethod
    def checkBadScholarship(leadArray, fundingClassification):
        if fundingClassification == 'Scholarship':
            sponsor = leadArray[2]
            infoText = leadArray[5]
            badScholarshipClassifier = ClassifyBadScholarships()
            badScholarshipPrediction = badScholarshipClassifier.classifyOpportunity(sponsor, infoText)
            return badScholarshipPrediction
        else:
            return ''


ProcessFastWebLeads.getFastWebLeadsAndInsertIntoDB()
