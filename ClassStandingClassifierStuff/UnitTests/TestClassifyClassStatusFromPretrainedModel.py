import unittest
from ClassStandingClassifierStuff.ClassifyClassStatusFromPretrainedModel import ClassifyClassStatusFromPretrainedModel
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
        testClassify = ClassifyClassStatusFromPretrainedModel(trainedModelInputFile=modelSaveFile,
                                                              trainedFeaturesValueCountsIndexesFile=featuresValueCountsSaveFile,
                                                              testingDataTextList=dataTextList,
                                                              testingDataIdsList=idsList)
        testClassify.displayResults()

    def test_seeIfCanReadFile(self):
        classStatus = 'Freshman'
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % classStatus
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % classStatus
        inputFile1 = open(featuresValueCountsSaveFile, 'rb')
        data = inputFile1.read()
        print(len(data))
        inputFile1.close()

        inputFile2 = open(modelSaveFile, 'rb')
        data = inputFile2.read()
        print(len(data))
        inputFile2.close()


if __name__ == '__main__':
    unittest.main()
