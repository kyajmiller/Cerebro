import unittest
from Classes.PopulateFatomeiLeadRequirements import PopulateFatomeiLeadRequirements


class TestStringMethods(unittest.TestCase):
    def test_GetMajors(self):
        sampleSentence = ['I am majoring in linguistics.']

        majors = PopulateFatomeiLeadRequirements().getMajorsFromDescriptionSourceText(sampleSentence)
        self.assertEqual('linguistics', majors)


if __name__ == '__main__':
    unittest.main()
