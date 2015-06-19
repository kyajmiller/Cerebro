import unittest
from Classes.ResidencyState import ResidencyState

States = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida',
          'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
          'Maryland',
          'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
          'New Hampshire',
          'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
          'Pennsylvania',
          'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia',
          'Washington',
          'West Viriginia', 'Wisconsin', 'Wyoming', 'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI',
          'ID', 'IL',
          'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM',
          'NY', 'NC',
          'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

States = '|\s'.join(States)

class TestStringMethods(unittest.TestCase):
    def test_ResidencyState(self):
        testresidencystate = ResidencyState('Must be a resident of Texas', States)
        self.assertIsNotNone(testresidencystate)
        self.assertEqual(testresidencystate.checkContext('resident|reside|residency|live|live\sin'), True)
        self.assertEqual(testresidencystate.getResidencyState(), ['Texas'])

        failresidencystate = ResidencyState('I went to college in VT', States)
        self.assertIsNotNone(failresidencystate)
        self.assertEqual(failresidencystate.checkContext('resident|reside|residency|live|live\sin'), False)
        self.assertNotEqual(failresidencystate.getResidencyState(), ['VT'])
        self.assertEqual(failresidencystate.getResidencyState(), [])

        testresidencystateabbreviations = ResidencyState('I live in Tucson, AZ', States)
        self.assertIsNotNone(testresidencystateabbreviations)
        self.assertEqual(testresidencystateabbreviations.checkContext('resident|reside|residency|live|live\sin'), True)
        self.assertEqual(testresidencystateabbreviations.getResidencyState(), ['AZ'])


if __name__ == '__main__':
    unittest.main()