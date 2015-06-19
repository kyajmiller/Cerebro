import unittest

from Classes.HTMLWorker import HTMLWorker



class TestHtmlWorker(unittest.TestCase):

  def testJavaScriptRemover(self):
      result=HTMLWorker.removeAllJavascript("<javascript>item</javascript>")
      self.assertEqual("item",result)


  def testTagRemover(self):
      result=HTMLWorker.removeHtmlTags("<body><a href='test'>item</a><div>This is the end</div></body>")
      self.assertEqual("  item  This is the end  ",result)
  def testRemoveNonBodyObjects(self):
      result=HTMLWorker.removeNonBodyElements("<html><head>test</head><body><a href='test'>item</a><div>This is the end</div></body>")
      result=HTMLWorker.removeHtmlTags(result)
      self.assertEqual(" item  This is the end ",result)

if __name__ == '__main__':
    unittest.main()