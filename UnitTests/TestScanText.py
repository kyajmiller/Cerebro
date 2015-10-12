import unittest
from Classes.ScanText import ScanText


class TestStringMethods(unittest.TestCase):
    def test_ScanText(self):
        with open('ScholarshipTestText1.txt') as filein:
            filein = ''.join(filein)

            testscantext = ScanText(filein)
            self.assertIsNotNone(testscantext)

            testscantext.prepareText()
            testDoGPA = testscantext.doGPAParser()
            self.assertIsNotNone(testDoGPA)
            self.assertEqual('1', testDoGPA.attributeId)
            self.assertEqual('3.0', testDoGPA.requirementValue)
            self.assertEqual('0', testDoGPA.logicGroup)
            self.assertEqual('>=', testDoGPA.requirementType)
            self.assertEqual('0', testDoGPA.scholarshipPackageId)



if __name__ == '__main__':
    unittest.main()
