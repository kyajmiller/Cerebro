from Classes.TokenizeOnWhitespacePunctuation import TokenizeOnWhitespacePunctuation


class ClassifyFundingTypeKeywordBased(object):
    def __init__(self, listOfOpportunitiesToBeClassified):
        self.listOfOpportunitiesToBeClassified = listOfOpportunitiesToBeClassified
        self.predictedTags = []

    def returnPredictedTags(self):
        self.loopThroughOpportunitiesAndClassify()
        return self.predictedTags

    def loopThroughOpportunitiesAndClassify(self):
        for titleAbstract in self.listOfOpportunitiesToBeClassified:
            title = titleAbstract[0]
            abstract = titleAbstract[1]
            tag = self.classifyOpportunity(title, abstract)
            self.predictedTags.append(tag)

    def classifyOpportunity(self, title, abstract):
        unigramsTitle = TokenizeOnWhitespacePunctuation(title, applyStopwords=True).getUnigrams()
        unigramsAbstract = TokenizeOnWhitespacePunctuation(abstract, applyStopwords=True).getUnigrams()

        if self.checkFellowshipKeywords(unigramsTitle):
            tag = 'Fellowship'
        elif self.checkInternshipKeywords(unigramsTitle):
            tag = 'Internship'
        elif self.checkScholarshipKeywords(unigramsTitle):
            tag = 'Scholarship'
        elif self.checkGrantKeywords(unigramsTitle):
            tag = 'Grant'
        elif self.checkFellowshipKeywords(unigramsAbstract):
            tag = 'Fellowship'
        elif self.checkInternshipKeywords(unigramsAbstract):
            tag = 'Internship'
        elif self.checkScholarshipKeywords(unigramsAbstract):
            tag = 'Scholarship'
        elif self.checkGrantKeywords(unigramsAbstract):
            tag = 'Grant'
        elif self.checkAwardKeywords(unigramsTitle):
            tag = 'Award'
        elif self.checkAwardKeywords(unigramsAbstract):
            tag = 'Award'
        elif self.checkResearchKeywords(unigramsTitle):
            tag = 'Research'
        elif self.checkResearchKeywords(unigramsAbstract):
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
        internshipKeywords = ['internship', 'internships', 'intern', 'interns', 'apprenticeship']
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