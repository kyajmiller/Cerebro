from Classes.TokenizeOnWhitespacePunctuation import TokenizeOnWhitespacePunctuation


class ClassifyFundingTypeKeywordBased(object):
    def __init__(self, listOfOpportunitiesToBeClassified):
        self.listOfOpportunitiesToBeClassified = listOfOpportunitiesToBeClassified
        self.predictedTags = []

    def returnPredictedTags(self):
        self.loopThroughOpportunitiesAndClassify()
        return self.predictedTags

    def loopThroughOpportunitiesAndClassify(self):
        for titleInfo in self.listOfOpportunitiesToBeClassified:
            title = titleInfo[0]
            info = titleInfo[1]
            tag = self.classifyOpportunity(title, info)
            self.predictedTags.append(tag)

    def classifyOpportunity(self, title, info):
        unigramsTitle = TokenizeOnWhitespacePunctuation(title, applyStopwords=True).getUnigrams()
        unigramsInfo = TokenizeOnWhitespacePunctuation(info, applyStopwords=True).getUnigrams()

        if self.checkFellowshipKeywordsTitle(unigramsTitle):
            tag = 'Fellowship'
        elif self.checkInternshipKeywords(unigramsTitle):
            tag = 'Internship'
        elif self.checkScholarshipKeywords(unigramsTitle):
            tag = 'Scholarship'
        elif self.checkGrantKeywords(unigramsTitle):
            tag = 'Grant'
        elif self.checkFellowshipKeywordsInfo(unigramsInfo):
            tag = 'Fellowship'
        elif self.checkInternshipKeywords(unigramsInfo):
            tag = 'Internship'
        elif self.checkGrantKeywords(unigramsInfo):
            tag = 'Grant'
        elif self.checkAwardKeywords(unigramsTitle):
            tag = 'Award'
        elif self.checkScholarshipKeywords(unigramsInfo):
            tag = 'Scholarship'
        elif self.checkResearchKeywords(unigramsTitle):
            tag = 'Research'
        elif self.checkResearchKeywords(unigramsInfo):
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

    def checkFellowshipKeywordsInfo(self, unigrams):
        fellowshipKeywords = ['fellowship', 'fellowships', 'fellow']
        keywordExists = False

        for keyword in fellowshipKeywords:
            if keyword in unigrams:
                keywordExists = True

        return keywordExists

    def checkFellowshipKeywordsTitle(self, unigrams):
        fellowshipKeywords = ['fellowship', 'fellowships', 'fellow', 'fellows']
        keywordExists = False

        for keyword in fellowshipKeywords:
            if keyword in unigrams:
                keywordExists = True

        return keywordExists

    def checkInternshipKeywords(self, unigrams):
        internshipKeywords = ['internship', 'internships', 'intern', 'interns', 'apprenticeship', 'extern',
                              'externship', 'externships', 'externs']
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
        awardKeywords = ['award', 'awards', 'prize', 'prizes', 'medal']
        keywordExists = False

        for keyword in awardKeywords:
            if keyword in unigrams:
                keywordExists = True

        return keywordExists

    def checkResearchKeywords(self, unigrams):
        researchKeywords = ['research', 'researcher', 'researchers', 'study', 'studying', 'studies']
        keywordExists = False

        for keyword in researchKeywords:
            if keyword in unigrams:
                keywordExists = True

        return keywordExists