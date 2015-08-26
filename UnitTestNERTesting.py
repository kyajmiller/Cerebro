import unittest
from Classes.NERTesting import NERTesting
from Classes.ComputeAccuracy import ComputeAccuracy
from Classes.SUDBConnect import SUDBConnect


class TestStringMethods(unittest.TestCase):
    def test_checkSponsorBadInstitutions(self):
        nertest = NERTesting()

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
        nertest = NERTesting()

        infoText = 'I go to the University of Arizona in Tucson, Arizona'
        testText = nertest.checkBadText(infoText)
        self.assertFalse(testText)

        infoText = 'You must go to a university in Albania'
        testText = nertest.checkBadText(infoText)
        self.assertTrue(testText)

    def test_loopThroughLeadsAndDoStuff(self):
        # set up
        db = SUDBConnect()
        sponsorsList = []
        descriptionList = []
        ocList = []
        iefaLeadIdList = []
        actualBad = []
        concatenatedDescriptionOCList = []
        rows = db.getRows("select * from dbo.IefaLeads where Tag='Scholarship' and BadScholarship!=''")
        for row in rows:
            sponsorsList.append(row.Sponsor)
            descriptionList.append(row.Description)
            ocList.append(row.OtherCriteria)
            actualBad.append(row.BadScholarship)
            iefaLeadIdList.append(row.IefaLeadId)

        for i in range(len(descriptionList)):
            conatenatedItem = '%s %s' % (descriptionList[i], ocList[i])
            concatenatedDescriptionOCList.append(conatenatedItem)

        # test
        testNER = NERTesting(sponsorsList, concatenatedDescriptionOCList)
        predictedBad = testNER.loopThroughLeadsAndDoStuff()

        accuracy = ComputeAccuracy(actualBad, predictedBad).calculateAccuracy()
        print(accuracy)





if __name__ == '__main__':
    unittest.main()
