import unittest
from ClassStandingClassifierStuff.OneVsRestClassifyClassStatusPreviouslyUntrained import \
    OneVsRestClassifyClassStatusPreviouslyUntrained
from ClassStandingClassifierStuff.GetDatabaseInfoScholarshipsWithClassStatuses import \
    GetDatabaseInfoScholarshipsWithClassStatuses


class TestStringMethods(unittest.TestCase):
    def test_OVRClassifier(self):
        dataTextList = GetDatabaseInfoScholarshipsWithClassStatuses().getConcatenatedDescriptionsEligibilities()
        labelsList = GetDatabaseInfoScholarshipsWithClassStatuses().getRequirementNeededList()
        idsList = GetDatabaseInfoScholarshipsWithClassStatuses().getScholarshipsWithClassStatusIdsList()
        testClassify = OneVsRestClassifyClassStatusPreviouslyUntrained(dataTextList, labelsList, idsList,
                                                                       trainingPercentage=0.8)
        testClassify.trainTestAndDisplayResults()

    def test_makeSureTheLabelsListIsAListOfListsOfStrings(self):
        dataTextList = GetDatabaseInfoScholarshipsWithClassStatuses().getConcatenatedDescriptionsEligibilities()
        labelsList = GetDatabaseInfoScholarshipsWithClassStatuses().getRequirementNeededList()
        idsList = GetDatabaseInfoScholarshipsWithClassStatuses().getScholarshipsWithClassStatusIdsList()
        testClassify = OneVsRestClassifyClassStatusPreviouslyUntrained(dataTextList, labelsList, idsList,
                                                                       trainingPercentage=0.8)

        trainingSet = testClassify.trainingSet
        trainingLables = [training['label'] for training in trainingSet]
        self.assertEqual(type(trainingLables), list)
        self.assertEqual(type(trainingLables[1]), list)
        self.assertEqual(type(trainingLables[1][0]), str)


if __name__ == '__main__':
    unittest.main()
