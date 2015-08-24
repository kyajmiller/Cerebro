import unittest
from Classes.NERTesting import NERTesting


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
        '''
        infoText1 = 'I like cheese. Cheese tastes good.'
        posTags = nertest.checkBadText(infoText1)

        infoText2 = 'They refuse to permit us to obtain the refuse permit.'
        posTags = nertest.checkBadText(infoText2)

        infoText3 = "I don't know why they make cheese into an adjective."
        posTags = nertest.checkBadText(infoText3)
        '''
        infoText4 = 'I go to the University of Arizona in Tucson, Arizona'
        neChunks = nertest.checkBadText(infoText4)

        infoText5 = 'That guy teaches at the Arizona University'
        neChunks = nertest.checkBadText(infoText5)


if __name__ == '__main__':
    unittest.main()
