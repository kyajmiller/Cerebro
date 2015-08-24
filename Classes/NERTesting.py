import nltk
from Classes.IefaLeadsGetDatabaseInfo import IefaLeadsGetDatabaseInfo
from Classes.TokenizeOnWhitespacePunctuation import TokenizeOnWhitespacePunctuation
from Classes.TokenizeIntoSentences import TokenizeIntoSentences


class NERTesting(object):
    def __init__(self):
        iefaLeadsInfo = IefaLeadsGetDatabaseInfo(tag='Scholarship')
        self.sponsorsList = iefaLeadsInfo.getSponsors()
        self.descriptionOCList = iefaLeadsInfo.getConcatenatedDescriptionOtherCriteria()
        self.iefaLeadsIds = iefaLeadsInfo.getIefaLeadsIds()

    def loopThroughLeadsAndDoStuff(self):
        for i in range(len(self.sponsorsList)):
            sponsor = self.sponsorsList[i]
            infoText = self.descriptionOCList[i]
            leadId = self.iefaLeadsIds[i]

            self.classifyOpportunity(sponsor, infoText)

    def classifyOpportunity(self, sponsor, infoText):
        pass

    def checkSponsorForBadInstitutions(self, sponsor):
        sponsorUnigrams = TokenizeOnWhitespacePunctuation(sponsor).getUnigrams()
        educationKeywords = ['university', 'school', 'institute', 'college']
        badSponsor = False

        for keyword in educationKeywords:
            if keyword in sponsorUnigrams:
                if sponsor != 'University of Arizona':
                    badSponsor = True

        return badSponsor

    def prepTextForNER(self):
        pass
