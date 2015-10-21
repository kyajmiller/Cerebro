import unittest
from Classes.DatabaseHelper import DatabaseHelper


class TestStringMethods(unittest.TestCase):
    def test_DatabaseHelperOnlyFirstRegex(self):
        self.assertEqual(True, DatabaseHelper.UseOnlyFirstRegex(417, 'Aerospace Engineering'))
        self.assertEqual(False, DatabaseHelper.UseOnlyFirstRegex(417, 'Cats'))

    def test_DatabaseHelperOnlyFirstRegexHelper(self):
        self.assertEqual(True, DatabaseHelper.useOnlyOneRegexHelper(417, 'Aerospace Engineering'))
        self.assertEqual(False, DatabaseHelper.useOnlyOneRegexHelper(417, 'Cats'))

    def test_UseOnlyFirstRegexAndRegexHelper(self):
        self.assertEqual(True, DatabaseHelper.useOnlyFirstRegexAndRegexHelper(417, 'Aerospace Engineering'))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexAndRegexHelper(417, 'Aerospace Cats'))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexAndRegexHelper(417, 'Engineering Cats'))

    def test_UseAllRegex(self):
        self.assertEqual(True, DatabaseHelper.useAllRegex(417, 'Aerospace Engineering'))

    def test_UseAllRegexHelper(self):
        self.assertEqual(True, DatabaseHelper.useAllRegexHelper(417, 'Aerospace Engineering'))

    def test_UseAllRegexAndRegexHelper(self):
        self.assertEqual(True, DatabaseHelper.useAllRegexAndRegexHelper(417, 'Aerospace Engineering'))
        self.assertEqual(False, DatabaseHelper.useAllRegexAndRegexHelper(417, 'Aerospace Cats'))
        self.assertEqual(False, DatabaseHelper.useAllRegexAndRegexHelper(417, 'Engineering Cats'))

    def test_UseOnlyFirstRegexTrue(self):
        self.assertEqual(True, DatabaseHelper.useOnlyFirstRegexTrue(417, 'Aerospace Engineering'))
        self.assertEqual(True, DatabaseHelper.useOnlyFirstRegexTrue(417, 'Engineering'))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexTrue(417, 'Aerospace'))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexTrue(417, 'Cat'))

    def test_UseOnlyFirstRegexHelperTrue(self):
        self.assertEqual(True, DatabaseHelper.useOnlyFirstRegexHelperTrue(417, 'Aerospace Engineering'))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexHelperTrue(417, 'Engineering'))
        self.assertEqual(True, DatabaseHelper.useOnlyFirstRegexHelperTrue(417, 'Aerospace'))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexHelperTrue(417, 'Cat'))

    def test_UseOnlyFirstRegexTrueRegexHelperTrue(self):
        self.assertEqual(True, DatabaseHelper.useOnlyFirstRegexTrueRegexHelperTrue(417, 'Aerospace Engineering'))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexTrueRegexHelperTrue(417, 'Engineering'))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexTrueRegexHelperTrue(417, 'Aerospace'))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexTrueRegexHelperTrue(417, 'Cat'))

    def test_UseOnlyFirstRegexTrueRegexHelperFalse(self):
        self.assertEqual(True, DatabaseHelper.useOnlyFirstRegexTrueRegexHelperFalse(417, 'Cat Engineering'))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexTrueRegexHelperFalse(417, 'Aerospace Engineering'))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexTrueRegexHelperFalse(417, 'Aerospace Pigeon'))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexTrueRegexHelperFalse(417, 'Cat Pigeon'))

    def test_UseOnlyFirstRegexFalseRegexHelperTrue(self):
        self.assertEqual(True, DatabaseHelper.useOnlyFirstRegexFalseRegexHelperTrue(417, 'Aerospace Pigeon'))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexFalseRegexHelperTrue(417, 'Aerospace Engineering'))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexFalseRegexHelperTrue(417, 'Cat Engineering'))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexFalseRegexHelperTrue(417, 'Cat Pigeon'))

    def test_UseOnlyFirstRegexFalseRegexHelperFalse(self):
        self.assertEqual(True, DatabaseHelper.useOnlyFirstRegexFalseRegexHelperFalse(417, 'Cat Pigeon'))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexFalseRegexHelperFalse(417, 'Aerospace Engineering'))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexFalseRegexHelperFalse(417, 'Cat Engineering'))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexFalseRegexHelperFalse(417, 'Aerospace Pigeon'))


if __name__ == '__main__':
    unittest.main()
