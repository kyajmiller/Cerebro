import unittest
from Classes.Majors import Majors

MajorOptions = ['accounting', 'adult gerontology acute care', 'nurse practitioner certificate',
                'advanced clinical pharmacy practice', 'aerospace engineering', 'africana studies',
                'agribusiness economics', 'agribusiness management', 'agricultural and biosystems engineering',
                'agricultural and resource economics', 'agricultural education',
                'agricultural technology management and education', 'american indian studies', 'animal science',
                'anthropology and linguistics', 'anthropology', 'applied bioscience', 'applied mathematics',
                'applied science', 'architecture', 'achival studies', 'arid lands resource sciences', 'art education',
                'art history and education', 'art history', 'art and visual culture education', 'astronomy',
                'atmospheric science', 'audiology', 'biochemistry', 'molecular biology', 'cellular biology',
                'bioinformatics', 'biology', 'biomedical engineering', 'biostatistics', 'business administration',
                'business economics', 'business intelligence and analytics', 'business management', 'cancer biology',
                'cellular medicine', 'molecular medicine', 'chemical engineering', 'chemistry', 'civil engineering',
                'engineering mechanics', 'classics', 'clinical research', 'translational research',
                'collaborative governance', 'college teaching', 'commerce', 'communication', 'computer science',
                'connecting environmental science and decision making', 'correspondence study', 'counseling',
                'mental health', 'creative writing', 'criminal justice', 'crop production', 'dance',
                'dendrochronology', 'development practice', 'digital information management', 'doctor of medicine',
                'early childhood education', 'early modern studies', 'east asian studies', 'economic geology',
                'economics', 'educational leadership and policy', 'educational leadership', 'educational psychology',
                'educational technology', 'electrical and computer engineering', 'electrical engineering',
                'elementary education', 'engineering', 'engineering management', 'english as a second language', 'esl',
                'entomology', 'insect science', 'environment and water resource economics', 'environment hydrology',
                'environment hydrology and water resources', 'environmental engineering',
                'environmental health science', 'environmental studies', 'epidemiology', 'esociety',
                'family and consumer science', 'family studies', 'human development', 'film and television', 'finance',
                "gender and women's studies", 'general biology', 'general studies', 'genetics',
                'geographic information science', 'geographic information systems technology', 'geography',
                'geoscience', 'german studies', 'german', 'global health and development', 'global studies',
                'government and public policy', 'goverment and public servie', 'health behavior', 'health promotion',
                'heritage conservation', 'higher education', 'history and theory of art', 'history',
                'human language technology', 'hydrology', 'hydrometeorology', 'immunobiology', 'indigenous governance',
                'industrial engineering', 'information resources', 'library science', 'information science and arts',
                'information science and techology', 'integrated science', 'interdisciplinary studies',
                'international security studies', 'international security', 'italian', 'journalism', 'judaic studies',
                'landscape architecture', 'language', 'latin american studies', 'law',
                'library and information science', 'linguistics', 'literacy learning and leadership',
                'management information systems', 'management', 'marketing', 'master of legal studies', 'mathematics',
                'math', 'mechanical engineering', 'mexican american studies', 'microbiology and pathobiology',
                'microbiology', 'middle east studies', 'north african studies', 'mining engineering',
                'mining geological engineering', 'mining geophysical engineering',
                'mining occupational safety and health', 'molecular and cellular biology',
                'motivating learning environments', 'music education', 'music', 'musical arts', 'musical theatre',
                'natural resources', 'natural science for teachers', 'near eastern studies',
                'neuroscience and cognitive science', 'neuroscience', 'nursing', 'nutritional science',
                'operations management', 'optical sciences and engineering', 'optical science', 'performance',
                'pharmaceutical science', 'pharmacology and toxicology', 'pharmacy',
                'philosophy, politics, economics and law', 'philosophy', 'photonic communcations engineering',
                'physics', 'physiological science', 'physiology', 'planetary science', 'planning', 'plant pathology',
                'plant science', 'political science', 'pre-architecture', 'pre-business', 'pre-computer science',
                'pre-education', 'pre-family studies and human development', 'pre-journalism', 'pre-neuroscience',
                'pre-nursing', 'pre-pharmacy', 'pre-physiology', 'pre-public health',
                'pre-retailing and consumer science', 'professional geographic informtion systems technology',
                'professional studies in health science', 'psychiatric mental health nurse practitioner', 'psychology',
                'public administration', 'public health', 'public management and policy', 'real estate development',
                'regional development', 'rehabilitation', 'religious studies', 'retailing and consumer science',
                'rhetoric, composition and teaching english', 'russian', 'school psychology', 'science education',
                'second language aquisition and teaching', 'secondary education', 'sociology',
                'soil, water, and environmental science', 'spanish', 'special education and rehabilitation',
                'special education', 'special graduate', 'speech, language, and hearing science', 'statistics',
                'studio art', 'sustainable built environments', 'sustainable plant systems',
                'systems and industrial engineering', 'systems engineering', 'teaching and teacher education',
                'theatre arts', 'theatre production', 'transcultural german studies', 'urban and regional development',
                'veterinary sciece', 'water policy', 'water, society, and policy', 'watershed management',
                'wildlife and fisheries science', 'network administration', 'japanese']

MajorOptions = list(set(MajorOptions))
MajorOptions = '|'.join(MajorOptions)


class TestStringMethods(unittest.TestCase):
    def test_Majors(self):
        testmajors = Majors('You must be a linguistics major', '5', MajorOptions)
        self.assertIsNotNone(testmajors)
        self.assertEqual(True,
                         testmajors.checkContext(
                             'enrolled in|majoring in|program|major|concentration|pursuing|student'))
        self.assertEqual(testmajors.getMajors(), 'linguistics')

    def test_Majorsfailure(self):
        failmajors = Majors('I really like plant science', '5', MajorOptions)
        self.assertIsNotNone(failmajors)
        self.assertEqual(False,
                         failmajors.checkContext(
                             'enrolled in|majoring in|program|major|concentration|pursuing|student'))
        self.assertNotEqual('plant science', failmajors.getMajors())
        self.assertEqual('', failmajors.getMajors())

    def test_MajorsCreateSPRFClass(self):
        testSPRFforMajors = Majors('You must be a Japanese major in order to make this SPRF class work.', '2947',
                                   MajorOptions)
        self.assertIsNotNone(testSPRFforMajors)
        self.assertEqual(True, testSPRFforMajors.checkContext(
            'enrolled in|majoring in|program|major|concentration|pursuing|student'))
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
