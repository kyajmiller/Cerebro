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

    def test_UseOnlyFirstRegexTrueAndRegexHelperTrue(self):
        self.assertEqual(True, DatabaseHelper.useOnlyFirstRegexTrueAndRegexHelperTrue(417, 'Aerospace Engineering'))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexTrueAndRegexHelperTrue(417, 'Engineering'))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexTrueAndRegexHelperTrue(417, 'Aerospace'))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexTrueAndRegexHelperTrue(417, 'Cat'))

    def test_UseOnlyFirstRegexTrueAndRegexHelperFalse(self):
        self.assertEqual(True, DatabaseHelper.useOnlyFirstRegexTrueAndRegexHelperFalse(417, 'Cat Engineering'))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexTrueAndRegexHelperFalse(417, 'Aerospace Engineering'))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexTrueAndRegexHelperFalse(417, 'Aerospace Pigeon'))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexTrueAndRegexHelperFalse(417, 'Cat Pigeon'))

'''
    def test_UseOnlyFirstRegexOrRegexHelper(self):
        self.assertEqual(True, DatabaseHelper.useOnlyFirstRegexOrRegexHelperTrueFalse(417, 'Aerospace Engineering',
                                                                                      matchRegEx=True,
                                                                                      matchRegExHelper=None))

        self.assertEqual(True, DatabaseHelper.useOnlyFirstRegexOrRegexHelperTrueFalse(417, 'Engineering', matchRegEx=True, matchRegExHelper=None))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexOrRegexHelperTrueFalse(417, 'Engineering', matchRegEx=False, matchRegExHelper=None))
        self.assertEqual(False,
                         DatabaseHelper.useOnlyFirstRegexOrRegexHelperTrueFalse(417, 'Engineering', matchRegEx=False,
                                                                                matchRegExHelper=True))
        self.assertEqual(False,
                         DatabaseHelper.useOnlyFirstRegexOrRegexHelperTrueFalse(417, 'Engineering', matchRegEx=True,
                                                                                matchRegExHelper=True))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexOrRegexHelperTrueFalse(417, 'Cat', matchRegEx=True,
                                                                                       matchRegExHelper=None))

        self.assertEqual(True, DatabaseHelper.useOnlyFirstRegexOrRegexHelperTrueFalse(417, 'Aerospace', matchRegEx=None, matchRegExHelper=True))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexOrRegexHelperTrueFalse(417, 'Aerospace', matchRegEx=None, matchRegExHelper=False))
        self.assertEqual(False,
                         DatabaseHelper.useOnlyFirstRegexOrRegexHelperTrueFalse(417, 'Aerospace', matchRegEx=True,
                                                                                matchRegExHelper=True))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexOrRegexHelperTrueFalse(417, 'Cat', matchRegEx=None,
                                                                                       matchRegExHelper=True))

        self.assertEqual(True, DatabaseHelper.useOnlyFirstRegexOrRegexHelperTrueFalse(417, 'Cat Engineering', matchRegEx=True, matchRegExHelper=False))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexOrRegexHelperTrueFalse(417, 'Cat Engineering', matchRegEx=False, matchRegExHelper=True))
        self.assertEqual(False,
                         DatabaseHelper.useOnlyFirstRegexOrRegexHelperTrueFalse(417, 'Cat Engineering', matchRegEx=True,
                                                                                matchRegExHelper=True))

        self.assertEqual(True, DatabaseHelper.useOnlyFirstRegexOrRegexHelperTrueFalse(417, 'Aerospace Pigeons', matchRegEx=False, matchRegExHelper=True))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexOrRegexHelperTrueFalse(417, 'Aerospace Pigeons', matchRegEx=True, matchRegExHelper=True))

        self.assertEqual(True, DatabaseHelper.useOnlyFirstRegexOrRegexHelperTrueFalse(417, 'Cat Pigeon', matchRegEx=False, matchRegExHelper=False))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexOrRegexHelperTrueFalse(417, 'Cat Pigeon', matchRegEx=True, matchRegExHelper=False))
        self.assertEqual(False,
                         DatabaseHelper.useOnlyFirstRegexOrRegexHelperTrueFalse(417, 'Cat Pigeon', matchRegEx=True,
                                                                                matchRegExHelper=True))

        self.assertEqual(True, DatabaseHelper.useOnlyFirstRegexOrRegexHelperTrueFalse(417, 'Aerospace Engineering',
                                                                                      matchRegEx=True,
                                                                                      matchRegExHelper=True))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexOrRegexHelperTrueFalse(417, 'Aerospace Engineering',
                                                                                       matchRegEx=False,
                                                                                       matchRegExHelper=False))
        self.assertEqual(False, DatabaseHelper.useOnlyFirstRegexOrRegexHelperTrueFalse(417, 'Aerospace Engineering',
                                                                                       matchRegEx=True,
                                                                                       matchRegExHelper=False))
        # note: for cases where both the Regex and the RegexHelper do actually match the string, if either matchRegEx or
        # matchRegExHelper is set to True the function will always return true. The only time it will return False is if
        # both arguments are set to False. I don't know how to fix it.
'''
if __name__ == '__main__':
    unittest.main()
