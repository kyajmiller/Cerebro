import unittest
from Classes.HighSchoolState import HighSchoolState

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
    def test_HighSchoolState(self):
        testhighschoolstate = HighSchoolState('I went to high school in Virginia', States)
        self.assertIsNotNone(testhighschoolstate)
        self.assertEqual(testhighschoolstate.checkContext('high\sschool|highschool|hs'), True)
        self.assertEqual(testhighschoolstate.getHighSchoolState(), ['Virginia'])

        failhighschoolstate = HighSchoolState('I went to college in New York', States)
        self.assertIsNotNone(failhighschoolstate)
        self.assertEqual(failhighschoolstate.checkContext('high\sschool|highschool|hs'), False)
        self.assertNotEqual(failhighschoolstate.getHighSchoolState(), ['New York'])
        self.assertEqual(failhighschoolstate.getHighSchoolState(), [])

        testhighschoolstateabbreviations = HighSchoolState('I also went to highschool in Tucson, AZ', States)
        self.assertIsNotNone(testhighschoolstateabbreviations)
        self.assertEqual(testhighschoolstateabbreviations.checkContext('high\sschool|highschool|hs'), True)
        self.assertEqual(testhighschoolstateabbreviations.getHighSchoolState(), ['AZ'])


if __name__ == '__main__':
    unittest.main()