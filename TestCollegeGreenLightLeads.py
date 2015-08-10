import unittest
from Classes.CollegeGreenLightLeads import CollegeGreenLightLeads


class TestStringMethods(unittest.TestCase):
    def test_CollegeGreenLightLeads(self):
        collegeLeads = CollegeGreenLightLeads().getLeads()
        firstLead = collegeLeads[0]
        self.assertEqual(9, len(firstLead))


if __name__ == '__main__':
    unittest.main()
