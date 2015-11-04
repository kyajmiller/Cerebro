from Classes.SUDBConnect import SUDBConnect
from ClassStandingClassifierStuff.OneVsRestClassifyClassStatusFromPretrainedModel import \
    OneVsRestClassifyClassStatusFromPretrainedModel


class ClassifyPotentialScholarships(object):
    def __init__(self):
        self.db = SUDBConnect()
        self.rows = self.db.getRows("select * from dbo.ClassifiedPotentialScholarships")

        self.oneVsRestPretrainedModelFile = 'OneVsRestLRTrainedClassifiers/OneVsRestLRTrainedModel'
        self.oneVsRestPretrainedFeaturesValueCountsFile = 'OneVsRestLRTrainedClassifiers/OneVsRestLRTrainedFeaturesValueCounts'

        self.dataTextList = self.getDataTextList()
        self.potentialScholarshipIdsList = self.getScholarshipIds()

    def getDataTextList(self):
        dataTextList = []

        for row in self.rows:
            dataTextList.append(row.Description)

        return dataTextList

    def getScholarshipIds(self):
        pass
