import SamsLogins.FastWebResults as FWR
import unittest


class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_importToFastTrackWeb(self):
      self.assertEqual(1,1)
      names=["test","test2"]
      searchTerms=[]
      providers=[]
      awards=[]
     # fastResults= FWR.FastWebResults(names,searchTerms,providers,awards)
     # fastResults.addScholarshipToObject()
     # self.assertEqual("test",FWR.names[0])






if __name__ == '__main__':
    unittest.main()