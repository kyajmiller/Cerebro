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


if __name__ == '__main__':
    unittest.main()
