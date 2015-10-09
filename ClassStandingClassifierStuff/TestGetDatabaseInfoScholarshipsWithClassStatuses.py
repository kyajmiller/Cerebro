import unittest
from ClassStandingClassifierStuff.GetDatabaseInfoScholarshipsWithClassStatuses import \
    GetDatabaseInfoScholarshipsWithClassStatuses
from Classes.CleanText import CleanText


class TestStringMethods(unittest.TestCase):
    def test_scholarshipsDescriptionsList(self):
        dbinfo = GetDatabaseInfoScholarshipsWithClassStatuses('Junior')
        self.assertIsNotNone(dbinfo)
        descriptionsList = dbinfo.getScholarshipDescriptionsList()
        self.assertIsNotNone(descriptionsList)
        testDescription = descriptionsList[0]
        testCleanText = CleanText.cleanALLtheText(testDescription)
        self.assertIsNotNone(testCleanText)

    def test_eligibilitiesList(self):
        dbinfo = GetDatabaseInfoScholarshipsWithClassStatuses('Senior')
        self.assertIsNotNone(dbinfo)
        eligibilitesList = dbinfo.getEligibilitiesList()
        self.assertIsNotNone(eligibilitesList)
        testEligibility = eligibilitesList[0]
        testCleanText = CleanText.cleanALLtheText(testEligibility)
        self.assertIsNotNone(testCleanText)

    def test_CheckIfSameLength(self):
        dbinfo = GetDatabaseInfoScholarshipsWithClassStatuses('Junior')
        descriptionsList = dbinfo.getScholarshipDescriptionsList()
        eligibilitiesList = dbinfo.getEligibilitiesList()
        self.assertIsNotNone(descriptionsList)
        self.assertIsNotNone(eligibilitiesList)
        self.assertEqual(len(descriptionsList), len(eligibilitiesList))


if __name__ == '__main__':
    unittest.main()
