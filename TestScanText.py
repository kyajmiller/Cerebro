import unittest
from Classes.ScanText import ScanText


class TestStringMethods(unittest.TestCase):
    def test_ScanText(self):
        with open('ScholarshipTestText1.txt') as filein:
            filein = ''.join(filein)
            testscantext = ScanText(filein)
            self.assertIsNotNone(testscantext)


if __name__ == '__main__':
    unittest.main()
