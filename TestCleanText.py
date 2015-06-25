import unittest
from Classes.CleanText import CleanText


class TestStringMethods(unittest.TestCase):
    def test_CleanText(self):
        self.assertEqual('This is the text I want to clean & make it look pretty', CleanText.cleanALLtheText(
            '<meow meow meow>This is the text I want &nbsp;to clean &amp; make it look pretty<98767888meow>'))

    def test_CleanTextRemoveAllTags(self):
        self.assertEqual('This text is good', CleanText.removeAllTags(
            '<This is a tag I want to remove!>This text is good<This tag also needs to go away>'))

    def test_CleanTextRemovenbsp(self):
        self.assertEqual('This function removes non-breaking spaces that are annoying to deal with',
                         CleanText.removenbsp(
                             'This function removes &nbsp;non-breaking spaces&nbsp; that are annoying to deal with'))

    def test_CleanTextConvertAmpersand(self):
        self.assertEqual('This function converts ampersands & makes them look nice',
                         CleanText.convertAmpersand('This function converts ampersands &amp; makes them look nice'))

    def test_CleanTextRemoveNonBodyText(self):
        self.assertEqual('I like cats', CleanText.removeNonBodyElements(
            "<html> This stuff isn't important <body>I like cats</body> This stuff also isn't important   "
            ""
            ""
            ""
            " </html>"))

if __name__ == '__main__':
    unittest.main()
