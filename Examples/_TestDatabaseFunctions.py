import unittest

from ClassModels.SUDBConnect import SUDBConnect



class TestDatabaseFunctions(unittest.TestCase):

  def testSUDBConnect(self):
      db=SUDBConnect()
      rows = db.getRowsDB("select * from tests")
      self.assertIsNotNone(rows)
  def testgetTestCases(self):
      db=SUDBConnect()
      rows =db.getAllTestCases()
      self.assertIsNotNone(rows)
  def testgetNumberOfTestCases(self):
      db=SUDBConnect()
      rows =db.getNumberOfTestCases(10)
      self.assertIsNotNone(rows)
      self.assertEqual(10,rows.__len__())
  def testgetNumberOfRandomTestCases(self):
      db=SUDBConnect()
      rows =db.getNumberOfRandomTestCases(10)
      firstRow=rows[0]
      secondRow=rows[0]
      self.assertEqual(firstRow,secondRow)
      rows =db.getNumberOfRandomTestCases(10)
      secondRow=rows[0]
      self.assertNotEqual(firstRow,secondRow)
  def testInsertState(self):
      db=SUDBConnect()
      db.insertUpdateOrDeleteDB("delete from  dbo.JustTests where TestValue='testit'")
      row = db.getRowsDB("select * from JustTests where testvalue='testit'")
      self.assertEqual(0,row.__len__())
      db.insertUpdateOrDeleteDB("INSERT INTO dbo.JustTests(  TestValue )VALUES  (  'testit'  )")
      row = db.getRowsDB("select * from JustTests where testvalue='testit'")
      self.assertIsNotNone(row)
  def testInsertIntoJustCase(self):
      db=SUDBConnect()
      db.insertUpdateOrDeleteDB("delete from  dbo.JustTests where TestValue='dubmthing'")
      db.insertIntoJustTests("dubmthing")
      rows = db.getRowsDB("select * from justtests where testvalue ='dubmthing'")
      self.assertEqual("dubmthing",rows[0].TestValue)
if __name__ == '__main__':
    unittest.main()