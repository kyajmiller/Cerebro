import unittest
from Classes.PivotLeadsRunFundingClassifier import PivotLeadsRunFundingClassifier


class TestStringMethods(unittest.TestCase):
    def test_RunPivotLeadsFundingClassifier(self):
        # this isn't actually a unit test, this will run the classifier over all of the rows in the PivotLeads database
        PivotLeadsRunFundingClassifier.getPredictedTagsInsertIntoDatabase()
        print('done')


if __name__ == '__main__':
    unittest.main()
