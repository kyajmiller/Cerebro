import SamsLogins.FastWebResults as FastWebResults
import unittest


class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_importToFastTrackWeb(self):
      self.assertEqual(1,1)






if __name__ == '__main__':
    unittest.main()