from Classes.InsertScholarships360LeadArrayIntoScholarships360DB import \
    InsertScholarships360LeadArrayIntoScholarships360DB
from Classes.Scholarships360Leads import Scholarships360Leads
from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased
from Classes.ClassifyBadScholarships import ClassifyBadScholarships
from Classes.CerebroLogs import CerebroLogs


class ProcessScholarships360Leads(object):
    @staticmethod
    def getScholarships360LeadsAndInsertIntoDatabase():
        arrayOfScholarship360Leads = Scholarships360Leads().getLeads()
        predictedFundingTypes = ProcessScholarships360Leads.classifyFunding(arrayOfScholarship360Leads)
        totalLeads = len(arrayOfScholarship360Leads)
        numNewEntries = 0
        numUpdates = 0
        for leadArray, fundingClassification in zip(arrayOfScholarship360Leads, predictedFundingTypes):
            badScholarshipClassification = ProcessScholarships360Leads.checkBadScholarship(leadArray,
                                                                                           fundingClassification)
            newEntryBoolean = InsertScholarships360LeadArrayIntoScholarships360DB(leadArray, fundingClassification,
                                                                                  badScholarshipClassification).insertUpdateLead()
            if newEntryBoolean:
                numNewEntries += 1
            else:
                numUpdates += 1
        CerebroLogs('Scholarships360', totalLeads, numNewEntries, numUpdates)

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
