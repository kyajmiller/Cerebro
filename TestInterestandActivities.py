import unittest
from Classes.InterestsAndActivities import InterestsAndActivities

ListInterestsandActivities = ['accounting', 'agricultural/food science', 'agricultural science', 'food science',
                              'life science',
                              'anatomy & physiology', 'anatomy and physiology', 'anthropology', 'architecture',
                              'arid lands', 'athletics',
                              'atmospheric science', 'audiology', 'automotive engineering', 'aviation',
                              'behavioral science', 'bike racing',
                              'biomedical engineering', 'business', 'business administration', 'chemistry',
                              'communications', 'community service',
                              'computer science', 'conservation', 'construction', 'counseling', 'criminal justice',
                              'cultures', 'heiritage',
                              'ecology', 'economics', 'education', 'electronic media', 'broadcasting', 'engineering',
                              'english', 'entrepreneurship',
                              'environment', 'epidemiological studies', 'film', 'finance', 'fine arts', 'flexography',
                              'food service', 'foreign language',
                              'gender studies', 'geology', 'golf', 'government', 'graphic communications',
                              'health and safety', 'history', 'horiculture',
                              'hotel management', 'humanities', 'hvac', 'hydrology', 'information resources',
                              'information technology', 'instrumentation',
                              'automation', 'international studies', 'journalism', 'landscape', 'languages', 'law',
                              'liberal arts', 'library science',
                              'linguistics', 'livestock', 'material science', 'management',
                              'management information systems', 'marine science', 'marketing',
                              'medicine', 'metallurgy', 'microbiology', 'middle eastern language', 'mining', 'music',
                              'natural resources', 'nuclear studies',
                              'nursing', 'oceanic science', 'press', 'psychology', 'public administration',
                              'public education', 'mathematics', 'math',
                              'social and behavioral science', 'sociology', 'study abroad', 'race', 'ethnicity',
                              'radiology', 'real estate', 'religion',
                              'technical broadcasting', 'technology', 'veterinary science', 'water skiing', 'education',
                              'teaching', 'art', 'entomology',
                              'nutritional sciences', 'chemical engineering', 'civil engineering',
                              'computer engineering', 'electrical engineering',
                              'engineering management', 'geological engineering', 'industrial engineering',
                              'mechanical engineering', 'non-destructive testing',
                              'optical science', 'welding', 'dance', 'media arts', 'theatre', 'classics', 'pharmacy',
                              'public health', 'biochemistry',
                              'biology', 'solid waste management', 'achaeology', 'aerospace', 'transportation',
                              'outdoor recreation', 'physical therapy',
                              'amateur radio', 'philosophy', 'palynology', 'football', 'interior design',
                              'intellectual property law', 'zoology',
                              'enology', 'viticulture', 'taekwondo', 'print communications', 'public speaking',
                              'archery', 'baseball', 'hospitality',
                              'travel', 'softball', 'bowling', 'equestrian', 'rodeo', 'respiratory care', 'research',
                              'fire science', 'biostatistics',
                              'operations management', 'paralegal', 'astronomy', 'national security',
                              'counterintelligence', 'creative writing',
                              'foreign service', 'explosives', 'plastics', 'polymers', 'visual arts', 'dairy industry',
                              'meteorology', 'insulators',
                              'physics', 'cross-country', 'track and field', 'basketball', 'swimming',
                              'veterans affairs', 'fashion', 'social justice',
                              'graphic arts', 'design', 'disabilities', 'retail', 'latin', 'greek', 'translation',
                              'interpretation', 'game development',
                              'religious mission', 'cosmetology', 'fishing', 'neuroscience', 'triathelete', 'beef',
                              'meat industry', 'ultilities',
                              'microelectronics', 'african american studies', 'optometry', 'neonatal', 'judaic studies',
                              'chiropractic care',
                              'laser', 'light based therapy', 'running', 'marathon', 'acoustics', 'robotics', 'soccer',
                              'phonetics', 'speech production',
                              'water resources', 'hispanic culture', 'botany', 'scottish culture', 'insurance',
                              'cross country', 'utilities',
                              'community involvement', 'school activity', 'patriotism', 'religious organization',
                              'mechanics', 'heritage conservation']

ListInterestsandActivities = list(set(ListInterestsandActivities))
ListInterestsandActivities = '|'.join(ListInterestsandActivities)


class TestStringMethods(unittest.TestCase):
    def test_InterestsAndActivities(self):
        testinterestsandactivities = InterestsAndActivities('Must have archery as a hobby.', ListInterestsandActivities)
        self.assertIsNotNone(testinterestsandactivities)
        self.assertEqual(testinterestsandactivities.checkContext('interest|activity|career|hobby|hobbies|achievement|demonstrate|involve|activities|commit'), True)
        self.assertEqual(testinterestsandactivities.getInterestsAndActivities(), ['archery'])

        failinterestsandactivities = InterestsAndActivities('Must have a major in Math.', ListInterestsandActivities)
        self.assertIsNotNone(failinterestsandactivities)
        self.assertEqual(failinterestsandactivities.checkContext('interest|activity|career|hobby|hobbies|achievement|demonstrate|involve|activities|commit'), False)
        self.assertNotEqual(failinterestsandactivities.getInterestsAndActivities(), ['math'])
        self.assertEqual(failinterestsandactivities.getInterestsAndActivities(), [])


if __name__ == '__main__':
    unittest.main()