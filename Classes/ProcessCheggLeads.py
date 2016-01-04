from Classes.InsertCheggLeadArrayIntoCheggLeadsDB import InsertCheggLeadArrayIntoCheggLeadsDB
from Classes.CheggLeads import CheggLeads
from Classes.ClassifyFundingTypeKeywordBased import ClassifyFundingTypeKeywordBased


class ProcessCheggLeads(object):
    @staticmethod
    def getCheggLeadsAndInsertIntoDB():
        cheggLeadsArrays = CheggLeads().loopOverResultsPagesAndDoStuff()
        predictedFundingTypes = ProcessCheggLeads.classifyFunding(cheggLeadsArrays)
        for leadArray, fundingClassification in zip(cheggLeadsArrays, predictedFundingTypes):
            InsertCheggLeadArrayIntoCheggLeadsDB(leadArray, fundingClassification)

    @staticmethod
    def classifyFunding(leadsArrays):
        titlesList = [cheggLeadsArray[0] for cheggLeadsArray in leadsArrays]
        infoTextList = ['%s %s' % (cheggLeadsArray[4], cheggLeadsArray[5]) for cheggLeadsArray in leadsArrays]
        opportunitiesTitlesAndTexts = [[title, infoText] for title, infoText in zip(titlesList, infoTextList)]
        fundingClassifier = ClassifyFundingTypeKeywordBased(opportunitiesTitlesAndTexts)
        predictedFundingTypes = fundingClassifier.returnPredictedTags()
        return predictedFundingTypes


ProcessCheggLeads.getCheggLeadsAndInsertIntoDB()

'''
self.name = self.cheggLeadArray[0]
        self.url = self.cheggLeadArray[1]
        self.deadline = self.cheggLeadArray[2]
        self.amount = self.cheggLeadArray[3]
        self.eligibility = self.cheggLeadArray[4]
        self.applicationOverview = self.cheggLeadArray[5]
        self.description = self.cheggLeadArray[6]
        self.sponsor = self.cheggLeadArray[7]
        self.sourceWebsite = self.cheggLeadArray[8]
        self.sourceText = self.cheggLeadArray[9]
        '''
