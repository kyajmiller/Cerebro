import unittest
from ClassStandingClassifierStuff.GetDatabaseInfoScholarshipsWithClassStatuses import \
    GetDatabaseInfoScholarshipsWithClassStatuses
from Classes.CleanText import CleanText
from sklearn.multiclass import OneVsRestClassifier
from sklearn.datasets import make_multilabel_classification
from sklearn.linear_model import LogisticRegression


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

    def test_CheckLabelsListFormat(self):
        # get the list of labels, 100
        dbinfo = GetDatabaseInfoScholarshipsWithClassStatuses()
        listOLabels = dbinfo.getRequirementNeededList()
        self.assertEqual(type(listOLabels), list)
        self.assertEqual(type(listOLabels[1]), list)
        first100Labels = listOLabels[:100]
        self.assertEqual(len(first100Labels), 100)

        # get fake data
        X, Y = make_multilabel_classification(n_classes=10, n_labels=3, allow_unlabeled=False)

        # test the OVR
        testClassifiier = OneVsRestClassifier(LogisticRegression())
        testClassifiier.fit(X, first100Labels)



if __name__ == '__main__':
    unittest.main()
