import unittest
from Classes.RunFundingClassifier import RunFundingClassifier
from Classes.CheggLeadsGetDatabaseInfo import CheggLeadsGetDatabaseInfo
from Classes.FastWebLeadsGetDatabaseInfo import FastWebLeadsGetDatabaseInfo
from Classes.FatomeiLeadsGetDatabaseInfo import FatomeiLeadsGetDatabaseInfo
from Classes.IefaLeadsGetDatabaseInfo import IefaLeadsGetDatabaseInfo
from Classes.MastersInEducationLeadsGetDatabaseInfo import MastersInEducationLeadsGetDatabaseInfo
from Classes.Scholarships360GetDatabaseInfo import Scholarship360LeadsGetDatabaseInfo


class TestStringMethods(unittest.TestCase):
    def test_RunFundingClassifierOnCheggLeads(self):
        titleConcatenatedEligibilityApplicationOverviewList = CheggLeadsGetDatabaseInfo().getTitleConcatenatedEligibilityAppplictionOverviewList()
        listCheggLeadsIds = CheggLeadsGetDatabaseInfo().getCheggLeadsIds()
        tableName = 'CheggLeads'
        idColumnName = 'CheggLeadId'

        fundingClassifier = RunFundingClassifier(titleConcatenatedEligibilityApplicationOverviewList)
        fundingClassifier.getPredictedTagsInsertIntoDB(tableName, idColumnName, listCheggLeadsIds)

    def test_RunFundingClassifierOnFastWebLeads(self):
        titleInfoList = FastWebLeadsGetDatabaseInfo().getTitleConcatenatedDescriptionSourceTextList()
        listFastWebLeadsIds = FastWebLeadsGetDatabaseInfo().getFastWebLeadsIds()
        tableName = 'FastWebLeads'
        idColumnName = 'FastWebLeadId'
        fundingClassfier = RunFundingClassifier(titleInfoList)

        fundingClassfier.getPredictedTagsInsertIntoDB(tableName, idColumnName, listFastWebLeadsIds)

    def test_RunFundingClassifierOnFatomeiLeads(self):
        titleDescriptionList = FatomeiLeadsGetDatabaseInfo().getTitleDescriptionList()
        listFatomeiLeadsIds = FatomeiLeadsGetDatabaseInfo().getFatomeiLeadIds()
        tableName = 'FatomeiLeads'
        idColumnName = 'FatomeiLeadId'
        fundingClassifier = RunFundingClassifier(titleDescriptionList)

        fundingClassifier.getPredictedTagsInsertIntoDB(tableName, idColumnName, listFatomeiLeadsIds)

    def test_RunFundingClassiferOnIefaLeads(self):
        titleConcatenatedDescriptionOtherCriteriaList = IefaLeadsGetDatabaseInfo().getTitleConcatenatedDescriptionOtherCriteriaList()
        listIefaLeadsIds = IefaLeadsGetDatabaseInfo().getIefaLeadsIds()
        tableName = 'IefaLeads'
        idColumnName = 'IefaLeadId'
        fundingClassifier = RunFundingClassifier(titleConcatenatedDescriptionOtherCriteriaList)

        fundingClassifier.getPredictedTagsInsertIntoDB(tableName, idColumnName, listIefaLeadsIds)

    def test_RunFundingClassifierOnMastersInEducationLeads(self):
        titleDescriptionList = MastersInEducationLeadsGetDatabaseInfo().getTitleDescriptionList()
        listMIELeadsIds = MastersInEducationLeadsGetDatabaseInfo().getMastersInEducationLeadIds()
        tableName = 'MastersInEducationLeads'
        idColumnName = 'MastersInEducationLeadId'

        fundingClassifier = RunFundingClassifier(titleDescriptionList)

        fundingClassifier.getPredictedTagsInsertIntoDB(tableName, idColumnName, listMIELeadsIds)

    def test_RunFundingClassifierOnScholarships360Leads(self):
        scholarships360Info = Scholarship360LeadsGetDatabaseInfo()

        titleDescriptionsList = scholarships360Info.getTitleDescriptionList()
        listScholarships360LeadsIds = scholarships360Info.getScholarships360LeadsIds()
        tableName = 'Scholarships360Leads'
        idColumnName = 'Scholarship360LeadId'

        fundingClassifier = RunFundingClassifier(titleDescriptionsList)
        fundingClassifier.getPredictedTagsInsertIntoDB(tableName, idColumnName, listScholarships360LeadsIds)

if __name__ == '__main__':
    unittest.main()
