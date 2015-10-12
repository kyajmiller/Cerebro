import unittest
from Classes.ResidencyArizonaCounty import ResidencyArizonaCounty

ArizonaCounties = ['Apache', 'Cochise', 'Coconino', 'Gila', 'Graham', 'Greenlee', 'La Paz', 'Maricopa',
                   'Mohave', 'Navajo', 'Pima', 'Pinal', 'Santa Cruz', 'Yavapai', 'Yuma']

ArizonaCounties = '|'.join(ArizonaCounties)

class TestStringMethods(unittest.TestCase):
    def test_ResidencyArizonaCounty(self):
        testresidencyarizonacounty = ResidencyArizonaCounty('Must live in Maricopa county.', ArizonaCounties)
        self.assertIsNotNone(testresidencyarizonacounty)
        self.assertEqual(True, testresidencyarizonacounty.checkContext('resident|reside|residency|live|live\sin'))
        self.assertEqual(True, testresidencyarizonacounty.checkContext('county|counties'))
        self.assertEqual(['Maricopa'], testresidencyarizonacounty.getResidencyArizonaCounty())

    def test_ResidencyArizonaCountyFailure(self):
        failtestresidencyarizonacounty = ResidencyArizonaCounty('Amphi high school is in Pima county', ArizonaCounties)
        self.assertIsNotNone(failtestresidencyarizonacounty)
        self.assertEqual(False, failtestresidencyarizonacounty.checkContext('resident|reside|residency|live|live\sin'))
        self.assertEqual(True, failtestresidencyarizonacounty.checkContext('county|counties'))
        self.assertEqual([], failtestresidencyarizonacounty.getResidencyArizonaCounty())


if __name__ == '__main__':
    unittest.main()