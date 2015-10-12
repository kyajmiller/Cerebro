import unittest
from ClassStandingClassifierStuff.ClassifyClassStatusFromPretrainedModel import ClassifyClassStatusFromPretrainedModel
from ClassStandingClassifierStuff.GetDatabaseInfoScholarshipsWithClassStatuses import \
    GetDatabaseInfoScholarshipsWithClassStatuses


class TestStringMethods(unittest.TestCase):
    def test_runModelOnFreshman(self):
        trainedModel = 'ClassifierTrainedModels\FreshmanClassStatusTrainedLRModel'
        databaseInfo = GetDatabaseInfoScholarshipsWithClassStatuses('Freshman')
        dataTextList = databaseInfo.getConcatenatedDescriptionsEligibilities()
        idsList = databaseInfo.getScholarshipsWithClassStatusIdsList()
        testClassify = ClassifyClassStatusFromPretrainedModel(trainedModelInputFile=trainedModel,
                                                              testingDataTextList=dataTextList,
                                                              testingDataIdsList=idsList)
        testClassify.displayResults()


if __name__ == '__main__':
    unittest.main()
