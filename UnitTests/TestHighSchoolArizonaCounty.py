import unittest
from Classes.HighSchoolArizonaCounty import HighSchoolArizonaCounty

ArizonaCounties = ['Apache', 'Cochise', 'Coconino', 'Gila', 'Graham', 'Greenlee', 'La Paz', 'Maricopa',
                   'Mohave', 'Navajo', 'Pima', 'Pinal', 'Santa Cruz', 'Yavapai', 'Yuma']

ArizonaCounties = '|'.join(ArizonaCounties)


class TestStringMethods(unittest.TestCase):
    def test_HighSchoolArizonaCounty(self):
        testhighschoolarizonacounty = HighSchoolArizonaCounty('Must attend highschool in Yuma county.', ArizonaCounties)
        self.assertIsNotNone(testhighschoolarizonacounty)
        self.assertEqual(testhighschoolarizonacounty.checkContext('high\sschool|highschool|hs'), True)
        self.assertEqual(testhighschoolarizonacounty.checkContext('county|counties'), True)
        self.assertEqual(testhighschoolarizonacounty.getHighSchoolArizonaCounty(), ['Yuma'])

    def test_HighSchoolArizonaCountyFailure(self):
        failtesthighschoolarizonacounty = HighSchoolArizonaCounty('Amphi high school is in Tucson', ArizonaCounties)
        self.assertIsNotNone(failtesthighschoolarizonacounty)
        self.assertEqual(failtesthighschoolarizonacounty.checkContext('high\sschool|highschool|hs'), True)
        self.assertEqual(failtesthighschoolarizonacounty.checkContext('county|counties'), False)
        self.assertEqual(failtesthighschoolarizonacounty.getHighSchoolArizonaCounty(), [])


if __name__ == '__main__':
    unittest.main()