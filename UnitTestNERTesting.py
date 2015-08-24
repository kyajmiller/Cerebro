import unittest
from Classes.NERTesting import NERTesting


class TestStringMethods(unittest.TestCase):
    def test_checkSponsorBadInstitutions(self):
        nertest = NERTesting()
        sponsor1 = 'University of Arizona'
        testSponsor1 = nertest.checkSponsorForBadInstitutions(sponsor1)
        self.assertFalse(testSponsor1)

        sponsor2 = 'University of Colorado'
        testSponsor2 = nertest.checkSponsorForBadInstitutions(sponsor2)
        self.assertTrue(testSponsor2)

        sponsor3 = 'Chicken and Egg Group'
        testSponsor3 = nertest.checkSponsorForBadInstitutions(sponsor3)
        self.assertFalse(testSponsor3)

        sponsor4 = 'School of Bacon'
        testSponsor4 = nertest.checkSponsorForBadInstitutions(sponsor4)
        self.assertTrue(testSponsor4)


if __name__ == '__main__':
    unittest.main()
