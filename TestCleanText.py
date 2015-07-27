#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from Classes.CleanText import CleanText


class TestStringMethods(unittest.TestCase):
    def test_CleanText(self):
        self.assertEqual('This is the text I want to clean & make it look pretty', CleanText.cleanALLtheText(
            '<meow meow meow>This is the text I want &nbsp;to clean &amp; make it look pretty<98767888meow>'))

    def test_CleanTextRemoveAllTags(self):
        self.assertEqual('This text is good', CleanText.cleanALLtheText(
            '<This is a tag I want to remove!>This text is good<This tag also needs to go away>'))

    def test_CleanTextRemovenbsp(self):
        self.assertEqual('This function removes non-breaking spaces that are annoying to deal with',
                         CleanText.cleanALLtheText(
                             'This function removes &nbsp;non-breaking spaces&nbsp; that are annoying to deal with'))

    def test_CleanTextConvertAmpersand(self):
        self.assertEqual('This function converts ampersands & makes them look nice',
                         CleanText.cleanALLtheText('This function converts ampersands &amp; makes them look nice'))

    def test_CleanTextRemoveNonBodyText(self):
        self.assertEqual('I like cats', CleanText.cleanALLtheText(
            "<html> This stuff isn't important <body>I like cats</body> This stuff also isn't important     \n \r \n all sorts of stuff </html>"))

    def test_CleanTextRemoveScriptAndJavaScript(self):
        self.assertEqual('There is no Javascript in this string', CleanText.cleanALLtheText(
            '<script>meowmeowmeow</script>There is no Javascript in this string'))

    def test_CleanTextRemoveStyle(self):
        self.assertEqual('All of the style stuff is gone',
                         CleanText.cleanALLtheText('<style blah blah>StyleStuff</style>All of the style stuff is gone'))

    def test_CleanTextReplaceSingleQuotes(self):
        self.assertEqual("There''s some extra single quotes in this line",
                         CleanText.cleanALLtheText(
                             "There's some extra single quotes in this line"))

    def test_RemoveMoreLess(self):
        self.assertEqual("There is less and there is more",
                         CleanText.cleanALLtheText('There is « lessless and there is moremore »'))

if __name__ == '__main__':
    unittest.main()
