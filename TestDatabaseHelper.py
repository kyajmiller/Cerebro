import unittest
from Classes.DatabaseHelper import DatabaseHelper


class TestStringMethods(unittest.TestCase):
    def test_DatabaseHelperOnlyFirstRegex(self):
        testdatabasehelper = DatabaseHelper.UseOnlyFirstRegex(417, 'Aerospace Engineering')
        self.assertIsNotNone(testdatabasehelper)
        self.assertEqual(True, DatabaseHelper.UseOnlyFirstRegex(417, 'Aerospace Engineering'))
        self.assertEqual(False, DatabaseHelper.UseOnlyFirstRegex(417, 'Cats'))

    def test_DatabaseHelperOnlyFirstRegexHelper(self):
        self.assertEqual(True, DatabaseHelper.getOnlyOneRegexHelper(417, 'Aerospace Engineering'))
        self.assertEqual(False, DatabaseHelper.getOnlyOneRegexHelper(417, 'Cats'))


'''
    def test_DatabaseHelperOnlyOneRegexandRegexHelper(self):
        self.assertEqual(('Engineering', 'Aerospace'), DatabaseHelper.getOnlyOneRegexAndRegexHelper(417))

    def test_DatabaseHelperAllRegex(self):
        self.assertEqual(['Engineering', 'Engineering'], DatabaseHelper.getAllRegex(417))

    def test_DatabaseHelperAllRegexHelper(self):
        self.assertEqual(['Aerospace', 'Biomedical'], DatabaseHelper.getAllRegexHelper(417))

    def test_DatabaseHelperAllRegexAndRegexHelper(self):
        self.assertEqual((['Engineering', 'Engineering'], ['Aerospace', 'Biomedical']),
                         DatabaseHelper.getAllRegexAndRegexHelper(417))
'''

if __name__ == '__main__':
    unittest.main()
