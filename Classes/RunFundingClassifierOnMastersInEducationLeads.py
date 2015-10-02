from Classes.RunFundingClassifier import RunFundingClassifier
from Classes.MastersInEducationLeadsGetDatabaseInfo import MastersInEducationLeadsGetDatabaseInfo


class RunFundingClassifierOnMastersInEducationLeads(RunFundingClassifier):
    def __init__(self):
        self.titleDescriptionList = MastersInEducationLeadsGetDatabaseInfo().getTitleDescriptionList()
