import unittest
from Classes.Parser import Parser



class TestStringMethods(unittest.TestCase):
    def test_Parser(self):
        testparser = Parser('This is a test', 'test')
        self.assertIsNotNone(testparser)
        self.assertEqual(testparser.doesMatchExist(), True)
        self.assertEqual(testparser.getResult(), ['test'])

    def test_ParserFailure(self):
        failparser = Parser('This test should return false', 'chicken')
        self.assertIsNotNone(failparser)
        self.assertEqual(failparser.doesMatchExist(), False)


if __name__ == '__main__':
    unittest.main()