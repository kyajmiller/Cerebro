import unittest
from Classes.PullPageLinkTitleDescriptionToArray import PullPageLinkTitleDescriptionToArray
from Classes.RipPage import RipPage

class TestStringMethods(unittest.TestCase):
    def test_PullPageLinkTitleDescriptionToDictGetTitle(self):
        testPullPageLinkTitleDescriptionToDict = PullPageLinkTitleDescriptionToArray(
            RipPage.getPageSource('https://www.google.com/'))
        self.assertIsNotNone(testPullPageLinkTitleDescriptionToDict.getTitle())
        self.assertEqual('Google', testPullPageLinkTitleDescriptionToDict.getTitle())

    def test_PullPageLinkTitleDescriptionToDictGetDescription(self):
        testPullPageLinkTitleDescriptionToDict = PullPageLinkTitleDescriptionToArray(
            RipPage.getPageSource('https://www.google.com/'))
        self.assertNotEqual('', testPullPageLinkTitleDescriptionToDict.getDescription())
        self.assertGreater(len(testPullPageLinkTitleDescriptionToDict.getDescription()), 10)

    def test_PullPageLinkTitleDescriptionToDictGetPageURL(self):
        testPullPageLinkTitleDescriptionToDict = PullPageLinkTitleDescriptionToArray(
            RipPage.getPageSource('http://grandcanyon.com'))
        self.assertGreater(len(testPullPageLinkTitleDescriptionToDict.getPageURL()), 10)

    def test_PullPageLinkTitleDescriptionToDictGetAllURLsOnPage(self):
        testPullPageLinkTitleDescriptionToDict = PullPageLinkTitleDescriptionToArray(
            RipPage.getPageSource('http://grandcanyon.com'))
        self.assertGreater(len(testPullPageLinkTitleDescriptionToDict.getAllURLsOnPage()), 1)
        print(testPullPageLinkTitleDescriptionToDict.getAllURLsOnPage())

if __name__ == '__main__':
    unittest.main()