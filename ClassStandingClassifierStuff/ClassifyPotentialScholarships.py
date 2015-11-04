from Classes.SUDBConnect import SUDBConnect
from ClassStandingClassifierStuff.OneVsRestClassifyClassStatusFromPretrainedModel import \
    OneVsRestClassifyClassStatusFromPretrainedModel


class ClassifyPotentialScholarships(object):
    def __init__(self):
        self.db = SUDBConnect()
        self.oneVsRestPretrainedModelFile = 'OneVsRestLRTrainedClassifiers/OneVsRestLRTrainedModel'
        self.oneVsRestPretrainedFeaturesValueCountsFile = 'OneVsRestLRTrainedClassifiers/OneVsRestLRTrainedFeaturesValueCounts'

        self.dataTextList = self.getDataText()
        self.potentialScholarshipIdsList = self.getScholarshipIds()

    def getDataText(self):
        pass

    def getScholarshipIds(self):
        pass
