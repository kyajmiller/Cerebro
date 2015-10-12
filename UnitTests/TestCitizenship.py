import unittest
from Classes.Citizenship import Citizenship

CountriesNationalities = ['U.S.', 'US', 'United States', 'China', 'Japan', 'Germany', 'United Kingdom', 'France', 'Brazil', 'Italy',
             'India', 'Russia', 'Canada', 'Australia', 'South Korea', 'Spain', 'Mexico', 'Indonesia', 'Netherlands',
             'Turkey', 'Saudi Arabia', 'Switzerland',
             'American', 'Chinese', 'Japanese', 'German', 'British', 'French', 'Brazilian', 'Italian', 'Indian',
             'Russian', 'Canadian', 'Australian', 'South Korean', 'Spanish', 'Mexican', 'Indonesian', 'Dutch',
             'Turkish', 'Saudi Arabian', 'Swiss']

CountriesNationalities = '|'.join(CountriesNationalities)

class TestStringMethods(unittest.TestCase):
    def test_Citizenship(self):
        testcitizenship = Citizenship('Must be a citizen of the United States.', CountriesNationalities)
        self.assertIsNotNone(testcitizenship)
        self.assertEqual(testcitizenship.checkContext('citizen'), True)
        self.assertEqual(testcitizenship.getCitizenship(), ['United States Citizen'])

    def test_CitizenshipFailure(self):
        failcitizenship = Citizenship("You have to be from Japan.", CountriesNationalities)
        self.assertIsNotNone(failcitizenship)
        self.assertEqual(failcitizenship.checkContext('citizen'), False)
        self.assertNotEqual(failcitizenship.getCitizenship(), ['Japan'])
        self.assertEqual(failcitizenship.getCitizenship(), [])


if __name__ == '__main__':
    unittest.main()