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

    def test_DoesTheDamnThingActuallyTrainProperlyJesusChrist(self):
        dataTextList = GetDatabaseInfoScholarshipsWithClassStatuses().getConcatenatedDescriptionsEligibilities()
        labelsList = GetDatabaseInfoScholarshipsWithClassStatuses().getRequirementNeededList()
        idsList = GetDatabaseInfoScholarshipsWithClassStatuses().getScholarshipsWithClassStatusIdsList()
        testClassify = OneVsRestClassifyClassStatusPreviouslyUntrained(dataTextList, labelsList, idsList,
                                                                       trainingPercentage=0.8)

        trainingSet = testClassify.trainingSet
        trainingLables = [training['label'] for training in trainingSet]
        print(trainingLables[1])
        print(trainingLables[2])


if __name__ == '__main__':
    unittest.main()
