import unittest
from ClassStandingClassifierStuff.OneVsRestClassifyFromPretrainedModel import \
    OneVsRestClassifyFromPretrainedModel
from ClassStandingClassifierStuff.GetDatabaseInfoScholarshipsWithClassStatuses import \
    GetDatabaseInfoScholarshipsWithClassStatuses
from Classes.SUDBConnect import SUDBConnect


class TestStringMethods(unittest.TestCase):
    def test_RunEnsembleClassifierInsertResultsIntoDB(self):
        # get data from db
        dataTextList = GetDatabaseInfoScholarshipsWithClassStatuses().getConcatenatedDescriptionsEligibilities()
        idsList = GetDatabaseInfoScholarshipsWithClassStatuses().getScholarshipsWithClassStatusIdsList()

        # run classifier, return results
        pretrainedOVRLRModelFilePath = '..\OneVsRestLRTrainedClassifiers\OneVsRestLRTrainedModel'
        pretrainedOVRLRFeaturesValueCountsIndexesFilePath = '..\OneVsRestLRTrainedClassifiers\OneVsRestLRTrainedFeaturesValueCounts'
        testClassifier = OneVsRestClassifyFromPretrainedModel(pretrainedOVRLRModelFilePath,
                                                              pretrainedOVRLRFeaturesValueCountsIndexesFilePath,
                                                              dataTextList, idsList)
        predictions = testClassifier.getPredictions()

        # insert results into db
        db = SUDBConnect()
        for scholarshipWithClassStatusID, prediction in zip(idsList, predictions):
            prediction = ', '.join(prediction)
            db.insertUpdateOrDelete(
                "update dbo.ScholarshipsWithClassStatuses set OneVsRestClassifierPrediction='" + prediction + "' where ScholarshipsWithClassStatusId = '" + str(
                    scholarshipWithClassStatusID) + "'")


if __name__ == '__main__':
    unittest.main()
