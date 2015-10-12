import unittest

from Classes.HTMLWorker import HTMLWorker


class TestHtmlWorker(unittest.TestCase):
    def testJavaScriptRemover(self):
        result = HTMLWorker.removeAllJavascript("<javascript>item</javascript>")
        self.assertEqual("item", result)

    def testTagRemover(self):
        result = HTMLWorker.removeHtmlTags("<body><a href='test'>item</a><div>This is the end</div></body>")
        self.assertEqual("  item  This is the end  ", result)

    def testRemoveNonBodyObjects(self):
        result = HTMLWorker.removeNonBodyElements(
            "<html><head>test</head><body><a href='test'>item</a><div>This is the end</div></body>")
        result = HTMLWorker.removeHtmlTags(result)
        self.assertEqual(" item  This is the end ", result)

    def testPreProcessing(self):
        htmlpage = '''<html><script>var x=1;</script><head>Test</head><body><div id='test'><ol><li>test</li></ol></div></body></html>'''
        result = HTMLWorker.cleanWebPageBeforeProcessing(htmlpage)
        self.assertEqual("test", result)


if __name__ == '__main__':
    unittest.main()
