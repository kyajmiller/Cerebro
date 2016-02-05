from Classes.InsertUnigoLeadArrayIntoUnigoLeadsDB import InsertUnigoLeadArrayIntoUnigoLeadsDB
from Classes.UnigoLeads import UnigoLeads
from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased
from Classes.ClassifyBadScholarships import ClassifyBadScholarships


class ProcessUnigoLeads(object):
    @staticmethod
    def getUnigoLeadsAndInsertIntoDB():
        unigoLeadsArrays = UnigoLeads().getLeads()
        predictedFundingTypes = ProcessUnigoLeads.classifyFunding(unigoLeadsArrays)
        for leadArray, fundingClassification in zip(unigoLeadsArrays, predictedFundingTypes):
            badScholarshipClassification = ProcessUnigoLeads.checkBadScholarship(leadArray, fundingClassification)
            InsertUnigoLeadArrayIntoUnigoLeadsDB(leadArray, fundingClassification, badScholarshipClassification)

    @staticmethod
    def classifyFunding(leadsArrays):
        titlesList = [leadArray[0] for leadArray in leadsArrays]
        infoTextList = ['%s %s' % (leadArray[6], leadArray[7]) for leadArray in leadsArrays]
        opportunitiesTitlesAndTexts = [[title, infoText] for title, infoText in zip(titlesList, infoTextList)]
        fundingClassifier = ClassifyFundingTypeKeywordBased(opportunitiesTitlesAndTexts)
        predictedFundingTypes = fundingClassifier.returnPredictedTags()
        return predictedFundingTypes

    @staticmethod
    def checkBadScholarship(leadArray, fundingClassification):
        if fundingClassification == 'Scholarship':
            sponsor = leadArray[3]
            infoText = '%s %s' % (leadArray[6], leadArray[7])
            badScholarshipClassifier = ClassifyBadScholarships()
            badScholarshipPrediction = badScholarshipClassifier.classifyOpportunity(sponsor, infoText)
            return badScholarshipPrediction
        else:
            return ''


ProcessUnigoLeads.getUnigoLeadsAndInsertIntoDB()
