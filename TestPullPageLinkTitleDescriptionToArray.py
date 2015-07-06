import unittest
from Classes.PullPageLinkTitleDescriptionToArray import PullPageLinkTitleDescriptionToArray
from Classes.RipPage import RipPage

class TestStringMethods(unittest.TestCase):
    def test_PullPageLinkTitleDescriptionToArray(self):
        testPullPageLinkTitleDescriptionToArray = PullPageLinkTitleDescriptionToArray(RipPage.getPageSource('https://www.google.com/'))
        self.assertIsNotNone(testPullPageLinkTitleDescriptionToArray.getTitle())
        self.assertEqual('Google', testPullPageLinkTitleDescriptionToArray.getTitle())

if __name__ == '__main__':
    unittest.main()