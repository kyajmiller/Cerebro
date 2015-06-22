import unittest
from Classes.Majors import Majors

MajorOptions = ['aerospace engineering', 'accounting', 'anthropology', 'arts', 'business management', '\schemistry',
                'chemical engineering', 'civil engineering', 'communication', 'computing & software systems',
                'computer engineering',
                'computer science', 'ecology', 'economics', 'electrical engineering', 'engineering', 'english',
                'environmental engineering', 'environmental sciences', 'entrepreneurship', 'finance', 'geology',
                'history',
                'human resource management', 'hydrogeology', 'hydrology', 'information science', 'information systems',
                'information systems technology management', 'electrical engineering', 'journalism', 'laser optics',
                'library science',
                'linguistics', 'marketing', 'mathematics', 'mechanical engineering', 'medicine', 'metallurgy', 'mining',
                'nursing',
                'physics', 'political science', 'psychology', 'science', 'science technology', 'social sciences',
                'sociology',
                'agricultural & biosystems engineering', 'biosystems engineering', 'bio systems engineering',
                'software systems',
                'agricultural education', 'agricultural & resource economics', 'agricultural technology',
                'agricultural technology management', 'animal sciences', 'architecture', 'astronomy', 'biochemistry',
                'business economics', 'classics', 'creative writing', 'criminal justice administration', 'dance',
                'dramatic theory',
                'earth science', 'east asian studies', 'elementary education', 'engineering mathematics',
                'engineering physics',
                'family and consumer sciences education', 'family studies', 'fine and performing arts',
                'fine arts studies', 'french',
                'business administration', 'geography', 'geological engineering', 'geosciences', 'german studies',
                'greek',
                'health education', 'health & human service administration', 'health and human service administration',
                'computing and software systems', 'agricultural and biosystems engineering',
                'agricultural and resource economics',
                'humanities', 'judaic studies', 'latin american studies', 'liberal studies',
                'materials science and engineering',
                'media arts', 'medical technology', 'mexican american studies', 'microbiology', 'mining engineering',
                'molecular & cellular biology', 'molecular and cellular biology', 'music', 'music education',
                'musical theatre',
                'natural sciences and mathematics', 'geography and regional development', 'religious studies',
                'russian',
                'secondary education', 'soil & water science', 'soil and water science', 'spanish',
                'special education & rehabilitation',
                'special education and rehabilitation', 'speech & hearing sciences', 'speech and hearing sciences',
                'studio art',
                'systems and industrial engineering', 'undecided/no major', 'undecided', 'no major',
                'veterinary science', 'wildlife',
                'watershed & rangeland resources', 'watershed and rangeland resources', "women's studies", 'technology',
                'public administration', 'biomedical engineering', 'nuclear engineering', 'ppel',
                'politics, philosophy, economics & law',
                'natural resources', 'landscape architecture', 'public health', 'visual communication', 'biology',
                'retail and consumer sciences', 'latin', 'criminal justice studies', 'criminal justice', 'italian',
                'neuroscience',
                'entomology', 'agronomy', 'math', 'law', 'forestry', 'pharmacy', 'agriculture', 'enligsh',
                'foreign language', 'studio art',
                'special education', 'early childhood education', 'teaching', 'literacy', 'counseling', 'education',
                'studio art',
                'plant science', 'portuguese', 'japanese', 'horticulture', 'nutritional science', 'animal science',
                'retail',
                'family and consumer resources', 'family and consumer science', 'engineering management',
                'engineering mechanics']

MajorOptions = list(set(MajorOptions))
MajorOptions = '|'.join(MajorOptions)


class TestStringMethods(unittest.TestCase):
    def test_Majors(self):
        testmajors = Majors('You must be a linguistics major', '5', MajorOptions)
        self.assertIsNotNone(testmajors)
        self.assertEqual(True,
            testmajors.checkContext('enrolled in|majoring in|program|major|concentration|pursuing|student'))
        self.assertEqual(testmajors.getMajors(), 'linguistics')

    def test_Majorsfailure(self):
        failmajors = Majors('I really like plant science', '5', MajorOptions)
        self.assertIsNotNone(failmajors)
        self.assertEqual(False,
            failmajors.checkContext('enrolled in|majoring in|program|major|concentration|pursuing|student'))
        self.assertNotEqual('plant science', failmajors.getMajors())
        self.assertEqual('', failmajors.getMajors())

    def test_MajorsCreateSPRFClass(self):
        testSPRFforMajors = Majors('You must be a Japanese major in order to make this SPRF class work.', '2947', MajorOptions)
        self.assertIsNotNone(testSPRFforMajors)
        self.assertEqual(True, testSPRFforMajors.checkContext('enrolled in|majoring in|program|major|concentration|pursuing|student'))
        self.assertEqual('japanese', testSPRFforMajors.getMajors())
        self.assertIsNotNone(testSPRFforMajors.getScholarshipPackageRequirementFormat())
        test_SPRF = testSPRFforMajors.getScholarshipPackageRequirementFormat()
        self.assertEqual('2947', test_SPRF.scholarshipPackageId)
        self.assertEqual('417', test_SPRF.attributeId)
        self.assertEqual('*', test_SPRF.requirementType)
        self.assertEqual('japanese', test_SPRF.requirementValue)
        self.assertEqual('0', test_SPRF.logicGroup)


if __name__ == '__main__':
    unittest.main()
