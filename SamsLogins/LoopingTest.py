import unittest


class TestStringMethods(unittest.TestCase):

  def testForLoopReturn(self):
      i=0
      listOfItems=range(10)
      for x in listOfItems:

          if (x==3):

              continue
          else:
              i=i+1
              print("not 3")
      self.assertEqual(9,i)












if __name__ == '__main__':
    unittest.main()