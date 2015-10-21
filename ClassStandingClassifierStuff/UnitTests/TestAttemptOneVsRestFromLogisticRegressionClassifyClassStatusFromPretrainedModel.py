import unittest
from ClassStandingClassifierStuff.AttemptOneVsRestFromLogisticRegressionClassifyClassStatusFromPretrainedModels import \
    EnsembleClassifyClassStatusFromPretrainedModels
from ClassStandingClassifierStuff.GetDatabaseInfoScholarshipsWithClassStatuses import \
    GetDatabaseInfoScholarshipsWithClassStatuses
from Classes.SUDBConnect import SUDBConnect


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

    def test_RunEnsembleClassifierInsertResultsIntoDB(self):
        # get data from db
        databaseInfoExtract = GetDatabaseInfoScholarshipsWithClassStatuses()
        dataTextList = databaseInfoExtract.getConcatenatedDescriptionsEligibilities()
        idsList = databaseInfoExtract.getScholarshipsWithClassStatusIdsList()

        # run classifier, return results
        ensembleClassifyTest = EnsembleClassifyClassStatusFromPretrainedModels(dataTextList, idsList)
        idsAndPredictionsList = ensembleClassifyTest.doAllClassificationsAndReturnFilteredPredictionsListsById()

        # insert results into db
        db = SUDBConnect()
        ids = [prediction[0] for prediction in idsAndPredictionsList]
        predictions = [prediction[1] for prediction in idsAndPredictionsList]
        for scholarshipWithClassStatusID, prediction in zip(ids, predictions):
            prediction = ', '.join(prediction)
            db.insertUpdateOrDelete(
                "update dbo.ScholarshipsWithClassStatuses set EnsembleClassifierPrediction='" + prediction + "' where ScholarshipsWithClassStatusId = '" + str(
                    scholarshipWithClassStatusID) + "'")


if __name__ == '__main__':
    unittest.main()
