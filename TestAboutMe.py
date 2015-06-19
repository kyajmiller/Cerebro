import unittest
from Classes.AboutMe import AboutMe

ListAboutMeAttributes = ['adopted', 'foster child', 'orphan', 'cancer survivor', 'medical condition', 'diability',
                         'domestic abuse victim', 'first generation student', 'homeless', 'non-traditional student',
                         'online education degree',
                         'parent', 'guardian', 'student athlete', 'vegetarian', 'vegan', 'lgbtq', 'straight ally',
                         'immigrant', 'migrant worker',
                         'single parent', 'head of household', 'financial need', 'low income',
                         'incoming transfer student', 'transfer student',
                         'animal rights', 'business owner', 'trade school', 'wheelchair', 'disabled', '9/11',
                         'community college transfer',
                         'marching band', 'student council', 'victim of crime', 'financial aid', 'has a child']

ListAboutMeAttributes = '|'.join(ListAboutMeAttributes)


class TestStringMethods(unittest.TestCase):
    def test_AboutMe(self):
        testaboutme = AboutMe('Must demonstrate financial need', ListAboutMeAttributes)
        self.assertIsNotNone(testaboutme)
        self.assertEqual(testaboutme.getAboutMe(), ['financial need'])

        failaboutme = AboutMe('This line does not have any of the About Me attributes in it.', ListAboutMeAttributes)
        self.assertIsNotNone(failaboutme)
        self.assertEqual(failaboutme.getAboutMe(), [])


if __name__ == '__main__':
    unittest.main()