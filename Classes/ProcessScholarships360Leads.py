from Classes.InsertScholarships360LeadArrayIntoScholarships360DB import \
    InsertScholarships360LeadArrayIntoScholarships360DB
from Classes.Scholarships360Leads import Scholarships360Leads
from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased
from Classes.ClassifyBadScholarships import ClassifyBadScholarships


class ProcessScholarships360Leads(object):
    @staticmethod
    def getScholarships360LeadsAndInsertIntoDatabase():
        arrayOfScholarship360Leads = Scholarships360Leads().getLeads()
        for leadArray in arrayOfScholarship360Leads:
            InsertScholarships360LeadArrayIntoScholarships360DB(leadArray)

    @staticmethod
    def classifyFunding(leadsArrays):
        titlesList = [leadArray[0] for leadArray in leadsArrays]
        infoTextList = ['%s %s' % (leadArray[2], leadArray[3]) for leadArray in leadsArrays]
        opportunitiesTitlesAndTexts = [[title, infoText] for title, infoText in zip(titlesList, infoTextList)]
        fundingClassifier = ClassifyFundingTypeKeywordBased(opportunitiesTitlesAndTexts)
        predictedFundingTypes = fundingClassifier.returnPredictedTags()
        return predictedFundingTypes

    @staticmethod
    def checkBadScholarship(leadArray, fundingClassification):
        if fundingClassification == 'Scholarship':
            sponsor = ''
            infoText = '%s %s' % (leadArray[2], leadArray[3])
            badScholarshipClassifier = ClassifyBadScholarships()
            badScholarshipPrediction = badScholarshipClassifier.classifyOpportunity(sponsor, infoText)
            return badScholarshipPrediction
        else:
            return ''


ProcessScholarships360Leads.getScholarships360LeadsAndInsertIntoDatabase()
