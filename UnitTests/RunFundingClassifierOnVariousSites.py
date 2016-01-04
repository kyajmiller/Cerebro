import unittest
from Classes.RunFundingClassifier import RunFundingClassifier
from Classes.CheggLeadsGetDatabaseInfo import CheggLeadsGetDatabaseInfo
from Classes.FastWebLeadsGetDatabaseInfo import FastWebLeadsGetDatabaseInfo


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


if __name__ == '__main__':
    unittest.main()
