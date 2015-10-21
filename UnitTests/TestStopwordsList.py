import unittest
from Classes.StopwordsList import StopwordsList


class TestStringMethods(unittest.TestCase):
    def test_stopwordsList(self):
        testlist = StopwordsList.stopwords()
        self.assertGreater(len(testlist), 350)


if __name__ == '__main__':
    unittest.main()
