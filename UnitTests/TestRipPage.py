import unittest
from Classes.RipPage import RipPage


class TestStringMethods(unittest.TestCase):
    def test_RipPage(self):
        test_rippage = RipPage.getPageSource('https://www.google.com/')
        self.assertIsNotNone(test_rippage)
        self.assertGreater(len(test_rippage), 10)


if __name__ == '__main__':
    unittest.main()
