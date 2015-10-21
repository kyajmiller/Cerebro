import unittest
from ClassStandingClassifierStuff.LogisticRegressionClassifyClassStatusFromPretrainedModel import \
    LogisticRegressionClassifyClassStatusFromPretrainedModel
from ClassStandingClassifierStuff.GetDatabaseInfoScholarshipsWithClassStatuses import \
    GetDatabaseInfoScholarshipsWithClassStatuses


class TestStringMethods(unittest.TestCase):
    def test_runModelOnFreshman(self):
        classStatus = 'Freshman'
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % classStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % classStatus

        # test to make sure can open model and fvc save files:
        testModelSaveOpen = open(modelSaveFile, 'rb')
        testModelSaveOpen.close()
        testFVCSaveOpen = open(featuresValueCountsSaveFile, 'rb')
        testFVCSaveOpen.close()

        # now do test
        databaseInfo = GetDatabaseInfoScholarshipsWithClassStatuses()
        dataTextList = databaseInfo.getConcatenatedDescriptionsEligibilities()
        idsList = databaseInfo.getScholarshipsWithClassStatusIdsList()
        testClassify = LogisticRegressionClassifyClassStatusFromPretrainedModel(trainedModelInputFile=modelSaveFile,
                                                              trainedFeaturesValueCountsIndexesFile=featuresValueCountsSaveFile,
                                                              testingDataTextList=dataTextList,
                                                              testingDataIdsList=idsList)
        testClassify.displayResults()


if __name__ == '__main__':
    unittest.main()
