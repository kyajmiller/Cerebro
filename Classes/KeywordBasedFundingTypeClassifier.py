from Classes.TokenizeOnWhitespacePunctuation import TokenizeOnWhitespacePunctuation
from Classes.GetPivotTagsTitleAbstractEligibility import GetPivotTagsTitleAbstractEligibility


class KeywordBasedFundingTypeClassifier(object):
    def __init__(self, listOfOpportunitiesToBeClassified):
        self.listOfOpportunitiesToBeClassified = listOfOpportunitiesToBeClassified
        self.predictedTags = []

    def loopThroughOpportunitiesAndClassify(self):
        for opportunity in self.listOfOpportunitiesToBeClassified:
            tag = self.classifyOpportunity(opportunity)
            self.predictedTags.append(tag)

    def classifyOpportunity(self, opportunity):
        unigrams = TokenizeOnWhitespacePunctuation.getUnigrams(opportunity)

        if self.checkScholarshipKeywords(unigrams):
            tag = 'scholarship'
        elif self.checkFellowshipKeywords(unigrams):
            tag = 'fellowship'
        elif self.checkInternshipKeywords(unigrams):
            tag = 'internship'
        elif self.checkGrantKeywords(unigrams):
            tag = 'grant'
        elif self.checkAwardKeywords(unigrams):
            tag = 'award'
        elif self.checkResearchKeywords(unigrams):
            tag = 'research'
        else:
            tag = 'other'

        return tag

    def checkScholarshipKeywords(self, unigrams):
        scholarshipKeywords = ['scholarship', 'scholarships']
        keywordExists = False

        while keywordExists == False:
            for keyword in scholarshipKeywords:
                if keyword in unigrams:
                    keywordExists = True

        return keywordExists

    def checkFellowshipKeywords(self, unigrams):
        fellowshipKeywords = ['fellowship', 'fellowships', 'fellow', 'fellows']
        keywordExists = False

        while keywordExists == False:
            for keyword in fellowshipKeywords:
                if keyword in unigrams:
                    keywordExists = True

        return keywordExists

    def checkInternshipKeywords(self, unigrams):
        internshipKeywords = ['internship', 'internships', 'intern', 'interns']
        keywordExists = False

        while keywordExists == False:
            for keyword in internshipKeywords:
                if keyword in unigrams:
                    keywordExists = True

        return keywordExists

    def checkGrantKeywords(self, unigrams):
        grantKeywords = ['grant', 'grants', 'grantee', 'grantees']
        keywordExists = False

        while keywordExists == False:
            for keyword in grantKeywords:
                if keyword in unigrams:
                    keywordExists = True

        return keywordExists

    def checkAwardKeywords(self, unigrams):
        awardKeywords = ['award', 'awards', 'prize', 'prizes', 'awarded']
        keywordExists = False

        while keywordExists == False:
            for keyword in awardKeywords:
                if keyword in unigrams:
                    keywordExists = True

        return keywordExists

    def checkResearchKeywords(self, unigrams):
        researchKeywords = ['research', 'researcher', 'researchers', 'study', 'studying']
        keywordExists = False

        while keywordExists == False:
            for keyword in researchKeywords:
                if keyword in unigrams:
                    keywordExists = True

        return keywordExists


testclass = GetPivotTagsTitleAbstractEligibility.getListConcatenatedItems()
testclasstags = GetPivotTagsTitleAbstractEligibility.getTitles()
