import nltk
import re
from Classes.TokenizeOnWhitespacePunctuation import TokenizeOnWhitespacePunctuation
from Classes.TokenizeIntoSentences import TokenizeIntoSentences


class NERTesting(object):
    def __init__(self, sponsorsList, infoTextList, test=None):
        self.test = test
        self.infoTextList = infoTextList
        self.sponsorsList = sponsorsList
        self.predictedBad = []

    def loopThroughLeadsAndDoStuff(self):
        for i in range(len(self.sponsorsList)):
            sponsor = self.sponsorsList[i]
            infoText = self.infoTextList[i]
            predictBad = self.classifyOpportunity(sponsor, infoText)
            self.predictedBad.append(predictBad)

        return self.predictedBad

    def classifyOpportunity(self, sponsor, infoText):
        badScholarship = False

        if self.test == 'sponsorOnly':
            if self.checkBadSponsor(sponsor):
                badScholarship = True
        elif self.test == 'infoTextOnly':
            if self.checkBadText(infoText):
                badScholarship = True
        else:
            if self.checkBadSponsor(sponsor):
                badScholarship = True
            else:
                if self.checkBadText(infoText):
                    badScholarship = True

        if badScholarship:
            badScholarship = 'Yes'
        else:
            badScholarship = 'No'

        return badScholarship

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
        badText = False

        for sentence in infoTextSentences:
            if not badText:
                unigrams = TokenizeOnWhitespacePunctuation(sentence, keepCaps=True).getUnigrams()
                educationKeywords = ['University', 'School', 'Institute', 'College']
                for i in range(len(unigrams) - 1):
                    if unigrams[i] in educationKeywords:
                        if unigrams[i + 1] == 'of':
                            unigrams[i + 1] = unigrams[i + 1].title()

                posTagUnigrams = nltk.pos_tag(unigrams)
                namedEntitiesOrgGPEList = self.parseNamedEntities(posTagUnigrams)
                organizations = namedEntitiesOrgGPEList[0]
                geoPoliticalEntities = namedEntitiesOrgGPEList[1]

                for organization in organizations:
                    educationRegex = '|'.join(educationKeywords)
                    if re.search(educationRegex, str(organization)):
                        if organization != 'University Of Arizona':
                            badText = True

                if badText != True:
                    for gpe in geoPoliticalEntities:
                        allowedLocations = ['United States', 'U.S.', 'America', 'Arizona', 'Tucson']
                        locationsRegex = '|'.join(allowedLocations)
                        if not re.search(locationsRegex, str(gpe)):
                            badText = True
                        else:
                            badText = False

        return badText

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
