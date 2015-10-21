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
            secondLabelIdsList=badClassStatusIds, trainingPercentage=0.8)

        self.assertIsNone(trainingSetAndTestingSet)


if __name__ == '__main__':
    unittest.main()
