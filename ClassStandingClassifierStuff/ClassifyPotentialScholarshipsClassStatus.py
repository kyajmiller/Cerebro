from Classes.SUDBConnect import SUDBConnect
from ClassStandingClassifierStuff.OneVsRestClassifyFromPretrainedModel import \
    OneVsRestClassifyFromPretrainedModel


class ClassifyPotentialScholarshipsClassStatus(object):
    def __init__(self):
        self.db = SUDBConnect()
        self.rows = self.db.getRows("select * from dbo.ClassifiedPotentialScholarships")

        self.oneVsRestPretrainedModelFile = 'OneVsRestLRTrainedClassifiers/OneVsRestLRTrainedModel'
        self.oneVsRestPretrainedFeaturesValueCountsFile = 'OneVsRestLRTrainedClassifiers/OneVsRestLRTrainedFeaturesValueCounts'

        self.dataTextList = self.getDataTextList()
        self.potentialScholarshipIdsList = self.getScholarshipIdsList()

        self.OneVsRestClassifier = OneVsRestClassifyFromPretrainedModel(self.oneVsRestPretrainedModelFile,
                                                                        self.oneVsRestPretrainedFeaturesValueCountsFile,
                                                                        self.dataTextList,
                                                                        self.potentialScholarshipIdsList)

        self.predictedClassStatuses = self.OneVsRestClassifier.getPredictions()
        self.insertResultsIntoDB()

    def getDataTextList(self):
        dataTextList = []

        for row in self.rows:
            dataTextList.append(row.Description)

        return dataTextList

    def getScholarshipIdsList(self):
        scholarshipIdsList = []

        for row in self.rows:
            scholarshipIdsList.append(row.PotentialScholarshipId)

        return scholarshipIdsList

    def insertResultsIntoDB(self):
        pass
