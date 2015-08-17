import unittest
from Classes.FastWebLeads import FastWebLeads


class TestStringMethods(unittest.TestCase):
    def test_FastWebLeads(self):
        testFastWebLeads = FastWebLeads().getLeads()
        self.assertIsNotNone(testFastWebLeads)
        firstArray = testFastWebLeads[0]
        self.assertEqual(len(firstArray), 12)


if __name__ == '__main__':
    unittest.main()
