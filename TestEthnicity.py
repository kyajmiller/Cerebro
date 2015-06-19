import unittest
from Classes.Ethnicity import Ethnicity

Demographics = ['American Indian', 'Alaskan Native', 'Alaska Native', 'Asian American', 'African American', 'Black',
                'Hispanic', 'Latino',
                'Native Hawaiian', 'Pacific Islander', 'White', 'Caucasian', 'Other', 'Middle Eastern',
                'Mexican American', 'Native American',
                'Minority', 'minority', 'International', 'Asian', 'Canadian First Nations', 'African\-American']

Demographics = '|'.join(Demographics)


class TestStringMethods(unittest.TestCase):
    def test_Ethnicity(self):
        testethnicity = Ethnicity('Must be an Alaska Native', Demographics)
        self.assertIsNotNone(testethnicity)
        self.assertEqual(testethnicity.checkContext('ethnicity|descent|lineage|ancestry|be\sa'), True)
        self.assertEqual(testethnicity.getEthnicity(), ['Alaska Native'])

        failethnicity = Ethnicity('Must be majoring in East Asian Studies', Demographics)
        self.assertIsNotNone(failethnicity)
        self.assertEqual(failethnicity.checkContext('ethnicity|descent|lineage|ancestry|be\sa'), False)
        self.assertEqual(failethnicity.checkContext('major|department|studies|language'), True)
        self.assertNotEqual(failethnicity.getEthnicity(), ['Asian'])
        self.assertEqual(failethnicity.getEthnicity(), [])


if __name__ == '__main__':
    unittest.main()