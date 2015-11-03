import unittest
import math
from ClassStandingClassifierStuff.MakeDataSetClassifyClassStatus import MakeDataSetClassifyClassStatus
from ClassStandingClassifierStuff.GetDatabaseInfoScholarshipsWithClassStatuses import \
    GetDatabaseInfoScholarshipsWithClassStatuses


class TestStringMethods(unittest.TestCase):
    def test_makeTrainingTestingSets(self):
        desiredClassStatus = 'Junior'
        goodClassStatusDB = GetDatabaseInfoScholarshipsWithClassStatuses(requirementNeeded=desiredClassStatus)
        badClassStatusDB = GetDatabaseInfoScholarshipsWithClassStatuses(requirementNeeded=desiredClassStatus,
                                                                        useNot=True)

        goodClassStatusIds = goodClassStatusDB.getScholarshipsWithClassStatusIdsList()
        goodClassStatusDataTextList = goodClassStatusDB.getConcatenatedDescriptionsEligibilities()
        badClassStatusIds = badClassStatusDB.getScholarshipsWithClassStatusIdsList()
        badClassStatusDataTextList = badClassStatusDB.getConcatenatedDescriptionsEligibilities()

        trainingPercentage = 0.9
        trainingSetAndTestingSet = MakeDataSetClassifyClassStatus.makeBinaryLabelTrainingAndTestingSet(
            firstLabel=desiredClassStatus, secondLabel='Other', firstLabelTextList=goodClassStatusDataTextList,
            secondLabelTextList=badClassStatusDataTextList, firstLabelIdsList=goodClassStatusIds,
            secondLabelIdsList=badClassStatusIds, trainingPercentage=trainingPercentage)
        training = trainingSetAndTestingSet[0]
        testing = trainingSetAndTestingSet[1]
        totalSetSize = len(training) + len(testing)
        self.assertEqual(math.ceil(totalSetSize * trainingPercentage), len(training))
        self.assertEqual((len(goodClassStatusDataTextList) + len(badClassStatusDataTextList)), totalSetSize)

    def test_makeTrainingTestingSetBadPercentage(self):
        desiredClassStatus = 'Senior'
        goodClassStatusDB = GetDatabaseInfoScholarshipsWithClassStatuses(requirementNeeded=desiredClassStatus)
        badClassStatusDB = GetDatabaseInfoScholarshipsWithClassStatuses(requirementNeeded=desiredClassStatus,
                                                                        useNot=True)

        goodClassStatusIds = goodClassStatusDB.getScholarshipsWithClassStatusIdsList()
        goodClassStatusDataTextList = goodClassStatusDB.getConcatenatedDescriptionsEligibilities()
        badClassStatusIds = badClassStatusDB.getScholarshipsWithClassStatusIdsList()
        badClassStatusDataTextList = badClassStatusDB.getConcatenatedDescriptionsEligibilities()

        trainingPercentage = 2
        trainingSetAndTestingSet = MakeDataSetClassifyClassStatus.makeBinaryLabelTrainingAndTestingSet(
            firstLabel=desiredClassStatus, secondLabel='Other', firstLabelTextList=goodClassStatusDataTextList,
            secondLabelTextList=badClassStatusDataTextList, firstLabelIdsList=goodClassStatusIds,
            secondLabelIdsList=badClassStatusIds, trainingPercentage=trainingPercentage)

        self.assertIsNone(trainingSetAndTestingSet)

    def test_makeMultilabelTrainingAndTestingSets(self):
        dataTextList = GetDatabaseInfoScholarshipsWithClassStatuses().getConcatenatedDescriptionsEligibilities()
        labelsList = GetDatabaseInfoScholarshipsWithClassStatuses().getRequirementNeededList()
        idsList = GetDatabaseInfoScholarshipsWithClassStatuses().getScholarshipsWithClassStatusIdsList()
        trainingPercentage = 0.9

        trainingSet, testingSet = MakeDataSetClassifyClassStatus.makeMultilabelTrainingAndTestingSet(dataTextList,
                                                                                                     labelsList,
                                                                                                     idsList,
                                                                                                     trainingPercentage)
        totalSetSize = len(trainingSet) + len(testingSet)

        self.assertEqual(math.ceil(totalSetSize * trainingPercentage), len(trainingSet))

    def test_SeeWhatTheMultilabelTrainingSetIsActuallyPassingAsLabels(self):
        dataTextList = GetDatabaseInfoScholarshipsWithClassStatuses().getConcatenatedDescriptionsEligibilities()
        labelsList = GetDatabaseInfoScholarshipsWithClassStatuses().getRequirementNeededList()
        idsList = GetDatabaseInfoScholarshipsWithClassStatuses().getScholarshipsWithClassStatusIdsList()
        trainingPercentage = 0.9

        trainingSet, testingSet = MakeDataSetClassifyClassStatus.makeMultilabelTrainingAndTestingSet(dataTextList,
                                                                                                     labelsList,
                                                                                                     idsList,
                                                                                                     trainingPercentage)

        trainingLabels = [trainingInstance['label'] for trainingInstance in trainingSet]
        self.assertEqual(type(trainingLabels[1]), list)
        self.assertEqual(type(trainingLabels[1][0]), str)


if __name__ == '__main__':
    unittest.main()
