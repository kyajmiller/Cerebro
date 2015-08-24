import nltk
import re
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
        badScholarship = False
        if self.checkBadSponsor(sponsor):
            badScholarship = True
        else:
            pass

    def checkBadSponsor(self, sponsor):
        sponsorUnigrams = TokenizeOnWhitespacePunctuation(sponsor).getUnigrams()
        educationKeywords = ['university', 'school', 'institute', 'college']
        badSponsor = False

        for keyword in educationKeywords:
            if keyword in sponsorUnigrams:
                if sponsor != 'University of Arizona':
                    badSponsor = True

        return badSponsor

    def checkBadText(self, infoText):
        infoTextSentences = TokenizeIntoSentences.doTokenize(infoText)
        for sentence in infoTextSentences:
            unigrams = TokenizeOnWhitespacePunctuation(sentence, keepCaps=True).getUnigrams()
            educationKeywords = ['University', 'School', 'Institute', 'College']
            for i in range(len(unigrams) - 1):
                if unigrams[i] in educationKeywords:
                    if unigrams[i + 1] == 'of':
                        unigrams[i + 1] = unigrams[i + 1].title()

            posTagUnigrams = nltk.pos_tag(unigrams)
            namedEntitiesOrgGPEList = self.parseNamedEntities(posTagUnigrams)
            organizations = namedEntitiesOrgGPEList[0]
            gpes = namedEntitiesOrgGPEList[1]

    def parseNamedEntities(self, posTagUnigrams):
        chunkNamedEntities = nltk.ne_chunk(posTagUnigrams)

        organizations = []
        for treeBranch in chunkNamedEntities:
            if hasattr(treeBranch, 'label') and treeBranch.label() == 'ORGANIZATION':
                organizations.append(str(treeBranch))
        organizations = self.formatNamedEntities(organizations)

        geoPoliticalEntities = []
        for treeBranch in chunkNamedEntities:
            if hasattr(treeBranch, 'label') and treeBranch.label() == 'GPE':
                geoPoliticalEntities.append(str(treeBranch))
        geoPoliticalEntities = self.formatNamedEntities(geoPoliticalEntities)

        namedEntitiesOrgGPEList = [organizations, geoPoliticalEntities]
        return namedEntitiesOrgGPEList

    def formatNamedEntities(self, namedEntityList):
        formattedStrings = []

        for namedEntity in namedEntityList:
            result = re.sub('ORGANIZATION\s', '', namedEntity)
            result = re.sub('GPE\s', '', result)
            result = re.sub('/[A-Z]+', '', result)
            result = re.sub('\(', '', result)
            result = re.sub('\)', '', result)

            formattedStrings.append(result)

        return formattedStrings
