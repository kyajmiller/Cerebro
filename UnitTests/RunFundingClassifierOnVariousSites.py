import unittest
from Classes.RunFundingClassifier import RunFundingClassifier
from Classes.CheggLeadsGetDatabaseInfo import CheggLeadsGetDatabaseInfo


class TestStringMethods(unittest.TestCase):
    def test_RunFundingClassifierOnCheggLeads(self):
        titleConcatenatedEligibilityApplicationOverviewList = CheggLeadsGetDatabaseInfo().getTitleConcatenatedEligibilityAppplictionOverviewList()
        listCheggLeadsIds = CheggLeadsGetDatabaseInfo().getCheggLeadsIds()
        tableName = 'CheggLeads'
        idColumnName = 'CheggLeadId'

        fundingClassifier = RunFundingClassifier(titleConcatenatedEligibilityApplicationOverviewList)
        fundingClassifier.getPredictedTagsInsertIntoDB(tableName, idColumnName, listCheggLeadsIds)


if __name__ == '__main__':
    unittest.main()
