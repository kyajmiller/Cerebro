from Classes.ScholarsiteLeads import ScholarsiteLeads
from Classes.InsertScholarsiteLeadsArrayIntoScholarsiteLeadsDB import InsertScholarsiteLeadsArrayIntoScholarsiteLeadsDB
from Classes.ClassifyBadScholarships import ClassifyBadScholarships
from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased


class ProcessScholarsiteLeads(object):
    @staticmethod
    def getScholarsiteLeadsAndInsertIntoDB():
        scholarsiteLeadsArrays = ScholarsiteLeads().processResultsPages()
        predictedFundingTypes = ProcessScholarsiteLeads.classifyFunding(scholarsiteLeadsArrays)
        for leadArray, fundingClassification in zip(scholarsiteLeadsArrays, predictedFundingTypes):
            badScholarshipClassification = ProcessScholarsiteLeads.checkBadScholarship(leadArray, fundingClassification)
            InsertScholarsiteLeadsArrayIntoScholarsiteLeadsDB(leadArray, fundingClassification,
                                                              badScholarshipClassification)

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
