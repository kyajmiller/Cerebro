import SamsLogins.FastWebClass as FWR
import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_classFirstVariable(self):
        testObject=FWR.FastWebClass("nameTest")
        self.assertEqual(testObject.name,"nameTest")
        print("name variable set correctly")
    def test_classSecondVariable(self):
        testObject=FWR.FastWebClass("name","provider")
        self.assertEqual(testObject.name,"name")
        self.assertEqual(testObject.provider,"provider")
        print("provider  variable set correctly")
    def test_classThirdVariable(self):
        testObject=FWR.FastWebClass("name","provider","award")
        self.assertEqual(testObject.name,"name")
        self.assertEqual(testObject.provider,"provider")
        self.assertEqual(testObject.award,"award")
        print("award variable set correctly")

    def test_classForthVariable(self):
        testObject=FWR.FastWebClass("name","provider","award","fastwebUrl")
        self.assertEqual(testObject.name,"name")
        self.assertEqual(testObject.provider,"provider")
        self.assertEqual(testObject.award,"award")
        self.assertEqual(testObject.fastwebUrl,"fastwebUrl")
        print("fastweburl variable set correctly")




if __name__ == '__main__':
    unittest.main()