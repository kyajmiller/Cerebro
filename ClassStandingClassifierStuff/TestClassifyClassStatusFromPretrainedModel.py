import unittest
from ClassStandingClassifierStuff.ClassifyClassStatusFromPretrainedModel import ClassifyClassStatusFromPretrainedModel
from ClassStandingClassifierStuff.GetDatabaseInfoScholarshipsWithClassStatuses import \
    GetDatabaseInfoScholarshipsWithClassStatuses


class TestStringMethods(unittest.TestCase):
    def test_runModelOnFreshman(self):
        trainedModel = 'ClassifierTrainedModels\FreshmanClassStatusTrainedLRModel'
        trainedFeaturesValueCounts = 'ClassifierTrainedModels\FreshmanClassStatusTrainedFeaturesValueCounts'
        databaseInfo = GetDatabaseInfoScholarshipsWithClassStatuses('Freshman')
        dataTextList = databaseInfo.getConcatenatedDescriptionsEligibilities()
        idsList = databaseInfo.getScholarshipsWithClassStatusIdsList()
        testClassify = ClassifyClassStatusFromPretrainedModel(trainedModelInputFile=trainedModel,
                                                              trainedFeaturesValueCountsIndexesFile=trainedFeaturesValueCounts,
                                                              testingDataTextList=dataTextList,
                                                              testingDataIdsList=idsList)
        testClassify.displayResults()


if __name__ == '__main__':
    unittest.main()
