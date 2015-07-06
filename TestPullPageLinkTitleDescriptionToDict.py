import unittest
from Classes.PullPageLinkTitleDescriptionToArray import PullPageLinkTitleDescriptionToArray
from Classes.RipPage import RipPage

class TestStringMethods(unittest.TestCase):
    def test_PullPageLinkTitleDescriptionToArrayGetTitle(self):
        testPullPageLinkTitleDescriptionToArray = PullPageLinkTitleDescriptionToArray('https://www.google.com/')
        self.assertIsNotNone(testPullPageLinkTitleDescriptionToArray.getTitle())
        self.assertEqual('Google', testPullPageLinkTitleDescriptionToArray.getTitle())

    def test_PullPageLinkTitleDescriptionToArrayGetDescription(self):
        testPullPageLinkTitleDescriptionToArray = PullPageLinkTitleDescriptionToArray('https://www.google.com/')
        self.assertNotEqual('', testPullPageLinkTitleDescriptionToArray.getDescription())
        self.assertGreater(len(testPullPageLinkTitleDescriptionToArray.getDescription()), 10)

    def test_PullPageLinkTitleDescriptionToArrayGetPageURL(self):
        testPullPageLinkTitleDescriptionToArray = PullPageLinkTitleDescriptionToArray('http://grandcanyon.com')
        self.assertGreater(len(testPullPageLinkTitleDescriptionToArray.getPageURL()), 10)

    def test_PullPageLinkTitleDescriptionToArrayGetAllURLsOnPage(self):
        testPullPageLinkTitleDescriptionToArray = PullPageLinkTitleDescriptionToArray('http://grandcanyon.com')
        self.assertGreater(len(testPullPageLinkTitleDescriptionToArray.getAllURLsOnPage()), 1)

    def test_PullPageLinkTitleDescriptionToArray(self):
        testPullPageLinkTitleDescriptionToArray = PullPageLinkTitleDescriptionToArray('http://grandcanyon.com')
        self.assertEqual(4, len(testPullPageLinkTitleDescriptionToArray.arrayTitleDescriptionPageURLLinks()))
        self.assertEqual(testPullPageLinkTitleDescriptionToArray.title,
                         testPullPageLinkTitleDescriptionToArray.arrayTitleDescriptionPageURLLinks()[0])
        self.assertEqual(testPullPageLinkTitleDescriptionToArray.description,
                         testPullPageLinkTitleDescriptionToArray.arrayTitleDescriptionPageURLLinks()[1])
        self.assertEqual(testPullPageLinkTitleDescriptionToArray.pageurl,
                         testPullPageLinkTitleDescriptionToArray.arrayTitleDescriptionPageURLLinks()[2])
        self.assertEqual(testPullPageLinkTitleDescriptionToArray.allurlsonpage,
                         testPullPageLinkTitleDescriptionToArray.arrayTitleDescriptionPageURLLinks()[3])

if __name__ == '__main__':
    unittest.main()