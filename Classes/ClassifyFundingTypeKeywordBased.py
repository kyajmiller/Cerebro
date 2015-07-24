from Classes.TokenizeOnWhitespacePunctuation import TokenizeOnWhitespacePunctuation


class ClassifyFundingTypeKeywordBased(object):
    def __init__(self, listOfOpportunitiesToBeClassified):
        self.listOfOpportunitiesToBeClassified = listOfOpportunitiesToBeClassified
        self.predictedTags = []

    def returnPredictedTags(self):
        self.loopThroughOpportunitiesAndClassify()
        return self.predictedTags

    def loopThroughOpportunitiesAndClassify(self):
        for opportunity in self.listOfOpportunitiesToBeClassified:
            tag = self.classifyOpportunity(opportunity)
            self.predictedTags.append(tag)

    def classifyOpportunity(self, opportunity):
        unigrams = TokenizeOnWhitespacePunctuation(opportunity, applyStopwords=True).getUnigrams()

        if self.checkScholarshipKeywords(unigrams):
            tag = 'Scholarship'
        elif self.checkFellowshipKeywords(unigrams):
            tag = 'Fellowship'
        elif self.checkInternshipKeywords(unigrams):
            tag = 'Internship'
        elif self.checkGrantKeywords(unigrams):
            tag = 'Grant'
        elif self.checkAwardKeywords(unigrams):
            tag = 'Award'
        elif self.checkResearchKeywords(unigrams):
            tag = 'Research'
        else:
            tag = 'Other'

        return tag

    def checkScholarshipKeywords(self, unigrams):
        scholarshipKeywords = ['scholarship', 'scholarships']
        keywordExists = False

        for keyword in scholarshipKeywords:
            if keyword in unigrams:
                keywordExists = True

        return keywordExists

    def checkFellowshipKeywords(self, unigrams):
        fellowshipKeywords = ['fellowship', 'fellowships', 'fellow', 'fellows']
        keywordExists = False

        for keyword in fellowshipKeywords:
            if keyword in unigrams:
                keywordExists = True

        return keywordExists

    def checkInternshipKeywords(self, unigrams):
        internshipKeywords = ['internship', 'internships', 'intern', 'interns']
        keywordExists = False

        for keyword in internshipKeywords:
            if keyword in unigrams:
                keywordExists = True

        return keywordExists

    def checkGrantKeywords(self, unigrams):
        grantKeywords = ['grant', 'grants', 'grantee', 'grantees']
        keywordExists = False

        for keyword in grantKeywords:
            if keyword in unigrams:
                keywordExists = True

        return keywordExists

    def checkAwardKeywords(self, unigrams):
        awardKeywords = ['award', 'awards', 'prize', 'prizes', 'awarded']
        keywordExists = False

        for keyword in awardKeywords:
            if keyword in unigrams:
                keywordExists = True

        return keywordExists

    def checkResearchKeywords(self, unigrams):
        researchKeywords = ['research', 'researcher', 'researchers', 'study', 'studying']
        keywordExists = False

        for keyword in researchKeywords:
            if keyword in unigrams:
                keywordExists = True

        return keywordExists