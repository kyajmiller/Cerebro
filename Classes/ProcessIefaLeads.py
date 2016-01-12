from Classes.IefaLeads import IefaLeads
from Classes.InsertIefaLeadArrayIntoIefaLeadsDB import InsertIefaLeadArrayIntoIefaLeadsDB
from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased
from Classes.ClassifyBadScholarships import ClassifyBadScholarships


class ProcessIefaLeads(object):
    @staticmethod
    def getIefaLeadsAndInsertIntoDB():
        iefaLeadsArrays = IefaLeads().loopOverResultsPagesAndDoStuff()
        predictedFundingTypes = ProcessIefaLeads.classifyFunding(iefaLeadsArrays)
        for leadArray, fundingClassification in zip(iefaLeadsArrays, predictedFundingTypes):
            badScholarshipClassification = ProcessIefaLeads.checkBadScholarship(leadArray, fundingClassification)
            InsertIefaLeadArrayIntoIefaLeadsDB(leadArray, fundingClassification, badScholarshipClassification)

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
            sponsor = leadArray[2]
            infoText = '%s %s' % (leadArray[6], leadArray[7])
            badScholarshipClassifier = ClassifyBadScholarships()
            badScholarshipPrediction = badScholarshipClassifier.classifyOpportunity(sponsor, infoText)
            return badScholarshipPrediction
        else:
            return ''


ProcessIefaLeads.getIefaLeadsAndInsertIntoDB()
