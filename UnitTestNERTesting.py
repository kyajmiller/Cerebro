import unittest
import nltk
from Classes.TokenizeOnWhitespacePunctuation import TokenizeOnWhitespacePunctuation
from Classes.NERTesting import NERTesting
from Classes.ComputeAccuracy import ComputeAccuracy
from Classes.SUDBConnect import SUDBConnect


class TestStringMethods(unittest.TestCase):
    def test_checkSponsorBadInstitutions(self):
        nertest = NERTesting(['blah'], ['blah'])

        sponsor1 = 'University of Arizona'
        testSponsor1 = nertest.checkBadSponsor(sponsor1)
        self.assertFalse(testSponsor1)

        sponsor2 = 'University of Colorado'
        testSponsor2 = nertest.checkBadSponsor(sponsor2)
        self.assertTrue(testSponsor2)

        sponsor3 = 'Chicken and Egg Group'
        testSponsor3 = nertest.checkBadSponsor(sponsor3)
        self.assertFalse(testSponsor3)

        sponsor4 = 'School of Bacon'
        testSponsor4 = nertest.checkBadSponsor(sponsor4)
        self.assertTrue(testSponsor4)

    def test_CheckBadText(self):
        nertest = NERTesting(['blah'], ['blah'])

        infoText = 'I go to the University of Arizona in Tucson, Arizona'
        testText = nertest.checkBadText(infoText)
        self.assertFalse(testText)

        # infoText = 'You must go to a university in Albania'
        # testText = nertest.checkBadText(infoText)
        # self.assertTrue(testText)

    def test_CheckBadTextRewrite(self):
        nertest = NERTesting(['blah'], ['blah'])

        infoText = 'CollegeWeekLive gives away $1,000 per month just for viewing and visiting US colleges online. Winning is easy - all you need to do is login to CollegeWeekLive and visit 3 colleges that interest you. One lucky winner will be awarded a $1,000 scholarship every month. And many other winners may find the college of their dreams.'
        testText = nertest.checkBadText(infoText)
        self.assertFalse(testText)

    def test_nltkNERParsing(self):
        testString = 'Natural Sciences and Engineering Research Council of Canada'
        unigrams = TokenizeOnWhitespacePunctuation(testString, keepCaps=True).getUnigrams()
        posTagged = nltk.pos_tag(unigrams)
        chunked = nltk.ne_chunk(posTagged)
        getGPEs = []

        for treeBranch in chunked:
            if hasattr(treeBranch, 'label') and treeBranch.label() == 'GPE':
                getGPEs.append(str(treeBranch))

        self.assertEqual(1, len(getGPEs))

        testString = 'Milwaukee Foundation'
        unigrams = TokenizeOnWhitespacePunctuation(testString, keepCaps=True).getUnigrams()
        posTagged = nltk.pos_tag(unigrams)
        chunked = nltk.ne_chunk(posTagged)
        # returns (S (PERSON Milwaukee/NNP) (ORGANIZATION Foundation/NNP))

        testString = 'New England Board of Higher Education'
        unigrams = TokenizeOnWhitespacePunctuation(testString, keepCaps=True).getUnigrams()
        posTagged = nltk.pos_tag(unigrams)
        chunked = nltk.ne_chunk(posTagged)
        # returns (S (GPE New/NNP)(ORGANIZATION England/NNP Board/NNP) of/IN (PERSON Higher/NNP Education/NNP))

        testString = 'New England Board of Higher Education'
        unigrams = TokenizeOnWhitespacePunctuation(testString).getUnigrams()
        posTagged = nltk.pos_tag(unigrams)
        chunked = nltk.ne_chunk(posTagged)
        # returns (S new/JJ england/NN board/NN of/IN higher/JJR education/NN)
        # shows that ntlk ne_chunk relies on capitalization to work

    def test_normalRun(self):
        # set up
        db = SUDBConnect()
        sponsorsList = []
        descriptionList = []
        ocList = []
        iefaLeadTrainingIdList = []
        actualBad = []
        concatenatedDescriptionOCList = []
        rows = db.getRows("select * from dbo.IefaLeadsTrainingItems")
        for row in rows:
            sponsorsList.append(row.Sponsor)
            descriptionList.append(row.Description)
            ocList.append(row.OtherCriteria)
            actualBad.append(row.BadScholarship)
            iefaLeadTrainingIdList.append(str(row.IefaLeadTrainingId))

        for i in range(len(descriptionList)):
            conatenatedItem = '%s %s' % (descriptionList[i], ocList[i])
            concatenatedDescriptionOCList.append(conatenatedItem)

        # test
        testNER = NERTesting(sponsorsList, concatenatedDescriptionOCList)
        predictedBad = testNER.loopThroughLeadsAndDoStuff()

        accuracy = ComputeAccuracy(actualBad, predictedBad).calculateAccuracy()
        print(accuracy)

        # put result in db
        for i in range(len(predictedBad)):
            iefaLeadTrainingId = iefaLeadTrainingIdList[i]
            predicted = predictedBad[i]
            db.insertUpdateOrDelete(
                "update dbo.IefaLeadsTrainingItems set NormalTestPredictedTag='" + predicted + "' where IefaLeadTrainingId='" + iefaLeadTrainingId + "'")

    def test_SponsorOnly(self):
        # set up
        db = SUDBConnect()
        sponsorsList = []
        descriptionList = []
        ocList = []
        iefaLeadTrainingIdList = []
        actualBad = []
        concatenatedDescriptionOCList = []
        rows = db.getRows("select * from dbo.IefaLeadsTrainingItems where BadScholarship!='Maybe'")
        for row in rows:
            sponsorsList.append(row.Sponsor)
            descriptionList.append(row.Description)
            ocList.append(row.OtherCriteria)
            actualBad.append(row.BadScholarship)
            iefaLeadTrainingIdList.append(str(row.IefaLeadTrainingId))

        for i in range(len(descriptionList)):
            conatenatedItem = '%s %s' % (descriptionList[i], ocList[i])
            concatenatedDescriptionOCList.append(conatenatedItem)

        # test
        testNER = NERTesting(sponsorsList, concatenatedDescriptionOCList, test='sponsorOnly')
        sponsorPredictedBad = testNER.loopThroughLeadsAndDoStuff()

        accuracy = ComputeAccuracy(actualBad, sponsorPredictedBad).calculateAccuracy()
        print(accuracy)

        # put result in db
        for i in range(len(sponsorPredictedBad)):
            iefaLeadTrainingId = iefaLeadTrainingIdList[i]
            predicted = sponsorPredictedBad[i]
            db.insertUpdateOrDelete(
                "update dbo.IefaLeadsTrainingItems set SponsorTestPredictedTag='" + predicted + "' where IefaLeadTrainingId='" + iefaLeadTrainingId + "'")

    def test_infoTextOnly(self):
        # set up
        db = SUDBConnect()
        sponsorsList = []
        descriptionList = []
        ocList = []
        iefaLeadTrainingIdList = []
        actualBad = []
        concatenatedDescriptionOCList = []
        rows = db.getRows("select * from dbo.IefaLeadsTrainingItems")
        for row in rows:
            sponsorsList.append(row.Sponsor)
            descriptionList.append(row.Description)
            ocList.append(row.OtherCriteria)
            actualBad.append(row.BadScholarship)
            iefaLeadTrainingIdList.append(str(row.IefaLeadTrainingId))

        for i in range(len(descriptionList)):
            conatenatedItem = '%s %s' % (descriptionList[i], ocList[i])
            concatenatedDescriptionOCList.append(conatenatedItem)

        # test
        testNER = NERTesting(sponsorsList, concatenatedDescriptionOCList, test='infoTextOnly')
        infoTextPredictedBad = testNER.loopThroughLeadsAndDoStuff()

        accuracy = ComputeAccuracy(actualBad, infoTextPredictedBad).calculateAccuracy()
        print(accuracy)

        # put result in db
        for i in range(len(infoTextPredictedBad)):
            iefaLeadTrainingId = iefaLeadTrainingIdList[i]
            predicted = infoTextPredictedBad[i]
            db.insertUpdateOrDelete(
                "update dbo.IefaLeadsTrainingItems set InfoTestPredictedTag='" + predicted + "' where IefaLeadTrainingId='" + iefaLeadTrainingId + "'")

if __name__ == '__main__':
    unittest.main()
