import unittest
from Classes.UnigoLeads import UnigoLeads


class TestStringMethods(unittest.TestCase):
    def test_UnigoLeads(self):
        unigoLeads = UnigoLeads().getLeads()
        firstLead = unigoLeads[0]
        self.assertEqual(12, len(firstLead))


if __name__ == '__main__':
    unittest.main()
