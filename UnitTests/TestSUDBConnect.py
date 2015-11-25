import unittest
from Classes.SUDBConnect import SUDBConnect


class TestStringMethods(unittest.TestCase):
    def test_ConnectToDBDefaultArguments(self):
        db = SUDBConnect()
        rows = db.getRows("select * from dbo.Tests")
        self.assertIsNotNone(rows)
        self.assertGreater(len(rows), 0)

    def test_ConnectToDBInsertUpdateDelete(self):
        db = SUDBConnect()
        rows = db.getRows("select * from dbo.Tests")
        self.assertGreater(len(rows), 0)
        db.insertUpdateOrDelete("insert into dbo.Tests (Regex, AttributeId) values ('meow', 2)")
        rows = db.getRows("select * from dbo.Tests where Regex='meow'")
        self.assertGreater(len(rows), 0)
        db.insertUpdateOrDelete("update dbo.Tests set Regex='kitty' where Regex='meow'")
        rows = db.getRows("select * from dbo.Tests where Regex='kitty'")
        self.assertGreater(len(rows), 0)
        db.insertUpdateOrDelete("delete from dbo.Tests where Regex='kitty'")
        rows = db.getRows("select * from dbo.Tests where Regex='kitty'")
        self.assertEqual(len(rows), 0)


if __name__ == '__main__':
    unittest.main()
