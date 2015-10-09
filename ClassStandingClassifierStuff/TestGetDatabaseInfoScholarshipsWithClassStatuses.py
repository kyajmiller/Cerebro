import unittest
from ClassStandingClassifierStuff.GetDatabaseInfoScholarshipsWithClassStatuses import \
    GetDatabaseInfoScholarshipsWithClassStatuses
from Classes.CleanText import CleanText


class TestStringMethods(unittest.TestCase):
    def test_scholarshipsDescriptionsList(self):
        dbinfo = GetDatabaseInfoScholarshipsWithClassStatuses('Junior')
        self.assertIsNotNone(dbinfo)
        descriptionsList = dbinfo.getScholarshipDescriptionsList()
        self.assertIsNotNone(descriptionsList)
        testDescription = descriptionsList[0]
        print('Original: %s' % testDescription)
        testCleanText = CleanText.cleanALLtheText(testDescription)
        print('Cleaned: %s' % testCleanText)
        self.assertIsNotNone(testCleanText)


if __name__ == '__main__':
    unittest.main()
