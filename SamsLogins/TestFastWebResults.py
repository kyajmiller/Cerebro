import SamsLogins.FastWebResults as FWR
import unittest


class TestStringMethods(unittest.TestCase):

  def test_importToFastTrackWebNameVarables(self):
      self.assertEqual(1,1)
      names=["name","name2"]
      searchTerms=["search","search2"]
      providers=["provider","provider2"]
      awards=["award","award2"]
      #add array for every item in list
      fastResults= FWR.FastWebResults(searchTerms,names,providers,awards)
      fastResults.addScholarshipToObject()
      self.assertEqual("name",fastResults.names[0])
      self.assertEqual("name2",fastResults.names[1])
      self.assertEqual("search",fastResults.searchTerms[0])
      self.assertEqual("search2",fastResults.searchTerms[1])






if __name__ == '__main__':
    unittest.main()