import unittest
from ClassStandingClassifierStuff.OneVsRestClassifyPreviouslyUntrained import \
    OneVsRestClassifyPreviouslyUntrained
from ClassStandingClassifierStuff.GetDatabaseInfoScholarshipsWithClassStatuses import \
    GetDatabaseInfoScholarshipsWithClassStatuses


class TestStringMethods(unittest.TestCase):
    def test_trainOVRLRModel(self):
        modelSaveFile = 'OneVsRestLRTrainedClassifiers\OneVsRestLRTrainedModel'
        featuresValueCountsSaveFile = 'OneVsRestLRTrainedClassifiers\OneVsRestLRTrainedFeaturesValueCounts'

        # first check to see if can open files:
        testOpenModelSaveFile = open(modelSaveFile, 'rb')
        testOpenModelSaveFile.close()
        testOpenFVCSaveFile = open(featuresValueCountsSaveFile, 'rb')
        testOpenFVCSaveFile.close()

        # do training and save to files
        dataTextList = GetDatabaseInfoScholarshipsWithClassStatuses().getConcatenatedDescriptionsEligibilities()
        labelsList = GetDatabaseInfoScholarshipsWithClassStatuses().getRequirementNeededList()
        idsList = GetDatabaseInfoScholarshipsWithClassStatuses().getScholarshipsWithClassStatusIdsList()
        testClassify = OneVsRestClassifyPreviouslyUntrained(dataTextList, labelsList, idsList,
                                                            trainingPercentage=0.99)
        testClassify.trainAndSaveOVRModel(modelSaveFile, featuresValueCountsSaveFile)


if __name__ == '__main__':
    unittest.main()
