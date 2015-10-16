import unittest
from ClassStandingClassifierStuff.EnsembleClassifyClassStatusFromPretrainedModels import \
    EnsembleClassifyClassStatusFromPretrainedModels
from ClassStandingClassifierStuff.GetDatabaseInfoScholarshipsWithClassStatuses import \
    GetDatabaseInfoScholarshipsWithClassStatuses


class TestStringMethods(unittest.TestCase):
    def test_runEnsembleClassifier(self):
        databaseInfo = GetDatabaseInfoScholarshipsWithClassStatuses()
        dataTextList = databaseInfo.getConcatenatedDescriptionsEligibilities()
        idsList = databaseInfo.getScholarshipsWithClassStatusIdsList()
        ensembleClassifyTest = EnsembleClassifyClassStatusFromPretrainedModels(dataTextList, idsList)

        ensembleClassifyTest.displayResults()

    def test_CheckIfCanReachRelativeFilePaths(self):
        # this is here to check if the relative file paths are right
        ensembleClassifyTest = EnsembleClassifyClassStatusFromPretrainedModels('blah', 'blah')
        ensembleClassifyTest.testToCheckRelativeFilePaths()


if __name__ == '__main__':
    unittest.main()
