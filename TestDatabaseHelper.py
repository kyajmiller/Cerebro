import unittest
from Classes.DatabaseHelper import DatabaseHelper


class TestStringMethods(unittest.TestCase):
    def test_DatabaseHelperOnlyOneRegex(self):
        testdatabasehelper = DatabaseHelper.getOnlyOneRegex(417)
        self.assertIsNotNone(testdatabasehelper)
        self.assertEqual('Engineering', DatabaseHelper.getOnlyOneRegex(417))

    def test_DatabaseHelperOnlyOneRegexHelper(self):
        self.assertEqual('Aerospace', DatabaseHelper.getOnlyOneRegexHelper(417))

    def test_DatabaseHelperOnlyOneRegexandRegexHelper(self):
        self.assertEqual(('Engineering', 'Aerospace'), DatabaseHelper.getOnlyOneRegexAndRegexHelper(417))

    def test_DatabaseHelperAllRegex(self):
        self.assertEqual(['Engineering', 'Engineering'], DatabaseHelper.getAllRegex(417))

    def test_DatabaseHelperAllRegexHelper(self):
        self.assertEqual(['Aerospace', 'Biomedical'], DatabaseHelper.getAllRegexHelper(417))

    def test_DatabaseHelperAllRegexAndRegexHelper(self):
        self.assertEqual((['Engineering', 'Engineering'], ['Aerospace', 'Biomedical']),
                         DatabaseHelper.getAllRegexAndRegexHelper(417))


if __name__ == '__main__':
    unittest.main()
