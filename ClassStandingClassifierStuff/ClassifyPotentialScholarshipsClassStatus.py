from Classes.SUDBConnect import SUDBConnect
from ClassStandingClassifierStuff.OneVsRestClassifyFromPretrainedModel import \
    OneVsRestClassifyFromPretrainedModel
import math


class ClassifyPotentialScholarshipsClassStatus(object):
    def __init__(self, whichHalfToDo):
        self.whichHalfToDo = whichHalfToDo
        self.db = SUDBConnect()
        self.rows = self.db.getRows("select * from dbo.ClassifiedPotentialScholarships")

        self.oneVsRestPretrainedModelFile = 'OneVsRestLRTrainedClassifiers/OneVsRestLRTrainedModel'
        self.oneVsRestPretrainedFeaturesValueCountsFile = 'OneVsRestLRTrainedClassifiers/OneVsRestLRTrainedFeaturesValueCounts'

        self.dataTextList = self.getDataTextList()
        self.potentialScholarshipIdsList = self.getScholarshipIdsList()

        halfOfRows = math.ceil(len(self.dataTextList) * 0.5)
        if self.whichHalfToDo == 1:
            self.dataTextList = self.dataTextList[:halfOfRows]
            self.potentialScholarshipIdsList = self.potentialScholarshipIdsList[:halfOfRows]
        elif self.whichHalfToDo == 2:
            self.dataTextList = self.dataTextList[-halfOfRows:]
            self.potentialScholarshipIdsList = self.potentialScholarshipIdsList[-halfOfRows:]

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
        for prediction, potentialScholarshipId in zip(self.predictedClassStatuses, self.potentialScholarshipIdsList):
            prediction = ', '.join(prediction)
            self.db.insertUpdateOrDelete(
                "update dbo.ClassifiedPotentialScholarships set ClassStatusPrediction='" + prediction + "' where PotentialScholarshipId='" + potentialScholarshipId + "'")


ClassifyPotentialScholarshipsClassStatus(1)
ClassifyPotentialScholarshipsClassStatus(2)
