import unittest
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

        infoText = 'You must go to a university in Albania'
        testText = nertest.checkBadText(infoText)
        self.assertTrue(testText)

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
