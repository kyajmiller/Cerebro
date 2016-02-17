from Classes.InsertTeacherDotOrgLeadArrayIntoTeacherDotOrgDB import InsertTeacherDotOrgLeadArrayIntoTeacherDotOrgDB
from Classes.TeacherDotOrgLeads import TeacherDotOrgLeads
from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased
from Classes.ClassifyBadScholarships import ClassifyBadScholarships
from Classes.CerebroLogs import CerebroLogs


class ProcessTeacherDotOrgLeads(object):
    @staticmethod
    def getTeacherDotOrgLeadsAndInsertIntoDB():
        teacherDotOrgLeadArrays = TeacherDotOrgLeads().getLeads()
        predictedFundingTypes = ProcessTeacherDotOrgLeads.classifyFunding(teacherDotOrgLeadArrays)
        totalLeads = len(teacherDotOrgLeadArrays)
        numNewEntries = 0
        numUpdates = 0
        for leadArray, fundingClassification in zip(teacherDotOrgLeadArrays, predictedFundingTypes):
            badScholarshipClassification = ProcessTeacherDotOrgLeads.checkBadScholarship(leadArray,
                                                                                         fundingClassification)
            newEntryBoolean = InsertTeacherDotOrgLeadArrayIntoTeacherDotOrgDB(leadArray, fundingClassification,
                                                                              badScholarshipClassification).insertUpdateLead()
            if newEntryBoolean:
                numNewEntries += 1
            else:
                numUpdates += 1
        CerebroLogs('TeacherDotOrg', totalLeads, numNewEntries, numUpdates)

    @staticmethod
    def classifyFunding(leadsArrays):
        titlesList = [leadArray[0] for leadArray in leadsArrays]
        infoTextList = ['%s %s' % (leadArray[1], leadArray[2]) for leadArray in leadsArrays]
        opportunitiesTitlesAndTexts = [[title, infoText] for title, infoText in zip(titlesList, infoTextList)]
        fundingClassifier = ClassifyFundingTypeKeywordBased(opportunitiesTitlesAndTexts)
        predictedFundingTypes = fundingClassifier.returnPredictedTags()
        return predictedFundingTypes

    @staticmethod
    def checkBadScholarship(leadArray, fundingClassification):
        if fundingClassification == 'Scholarship':
            sponsor = ''
            infoText = '%s %s' % (leadArray[1], leadArray[2])
            badScholarshipClassifier = ClassifyBadScholarships()
            badScholarshipPrediction = badScholarshipClassifier.classifyOpportunity(sponsor, infoText)
            return badScholarshipPrediction
        else:
            return ''
