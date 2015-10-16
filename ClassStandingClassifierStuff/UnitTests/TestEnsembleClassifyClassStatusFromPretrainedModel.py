import unittest
from ClassStandingClassifierStuff.EnsembleClassifyClassStatusFromPretrainedModels import \
    EnsembleClassifyClassStatusFromPretrainedModels
from ClassStandingClassifierStuff.GetDatabaseInfoScholarshipsWithClassStatuses import \
    GetDatabaseInfoScholarshipsWithClassStatuses


class TestStringMethods(unittest.TestCase):
    def test_runModelOnFreshman(self):
        databaseInfo = GetDatabaseInfoScholarshipsWithClassStatuses()
        dataTextList = databaseInfo.getConcatenatedDescriptionsEligibilities()
        idsList = databaseInfo.getScholarshipsWithClassStatusIdsList()
        ensembleClassifyTest = EnsembleClassifyClassStatusFromPretrainedModels(dataTextList, idsList)
        ensembleClassifyTest.displayResults()


if __name__ == '__main__':
    unittest.main()
