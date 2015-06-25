import unittest
from Classes.CleanText import CleanText


class TestStringMethods(unittest.TestCase):
    def test_CleanText(self):
        self.assertEqual('This is the text I want to clean & make it look pretty', CleanText.cleanALLtheText(
            '<meow meow meow>This is the text I want &nbsp;to clean &amp; make it look pretty<98767888meow>'))


if __name__ == '__main__':
    unittest.main()
