import unittest
from Classes.ResidencyArizonaCounty import ResidencyArizonaCounty

ArizonaCounties = ['Apache', 'Cochise', 'Coconino', 'Gila', 'Graham', 'Greenlee', 'La Paz', 'Maricopa',
                   'Mohave', 'Navajo', 'Pima', 'Pinal', 'Santa Cruz', 'Yavapai', 'Yuma']

ArizonaCounties = '|'.join(ArizonaCounties)

class TestStringMethods(unittest.TestCase):
    def test_ResidencyArizonaCounty(self):
        testresidencyarizonacounty = ResidencyArizonaCounty('Must live in Maricopa county.', ArizonaCounties)
        self.assertIsNotNone(testresidencyarizonacounty)
        self.assertEqual(testresidencyarizonacounty.checkContext('resident|reside|residency|live|live\sin'), True)
        self.assertEqual(testresidencyarizonacounty.checkContext('county|counties'), True)
        self.assertEqual(testresidencyarizonacounty.getResidencyArizonaCounty(), ['Maricopa'])

        failtestresidencyarizonacounty = ResidencyArizonaCounty('Amphi high school is in Pima county', ArizonaCounties)
        self.assertIsNotNone(failtestresidencyarizonacounty)
        self.assertEqual(failtestresidencyarizonacounty.checkContext('resident|reside|residency|live|live\sin'), False)
        self.assertEqual(failtestresidencyarizonacounty.checkContext('county|counties'), True)
        self.assertEqual(failtestresidencyarizonacounty.getResidencyArizonaCounty(), [])


if __name__ == '__main__':
    unittest.main()