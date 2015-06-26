import re
from Classes.Parser import Parser
from Classes.ScholarshipPackageRequirementFormat import ScholarshipPackageRequirement


class Majors(Parser):
    def __init__(self, stringToScan, majorOptions, scholarshipPackageId='0'):
        self.majorOptions = majorOptions
        self.stringToScan = stringToScan
        Parser.__init__(self, self.stringToScan.lower(), self.majorOptions)
        self.resultList = []
        self.attributeId = '417'
        self.requirementValue = ''
        self.logicGroup = '0'
        self.requirementTypeCode = '*'
        self.scholarshipPackageId = scholarshipPackageId

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        return contextChecker.doesMatchExist()

    def getMajors(self):
        if self.checkContext(
                'enrolled in|majoring in|program|major|concentration|pursuing|student|study\sof') and self.doesMatchExist():
            for i in self.getResult():
                self.resultList.append(i)

        if self.checkContext('of\sscience|of\sarts|of\smedicine') and self.doesMatchExist():
            if 'science' in self.resultList:
                self.resultList.remove('science')
            if 'arts' in self.resultList:
                self.resultList.remove('arts')
            if 'medicine' in self.resultList:
                self.resultList.remove('medicine')

        if self.checkContext('engineering'):
            tokenizeEngineeringString = re.findall(r"[\w']+", self.stringToScan)
            for i in range(len(tokenizeEngineeringString)):
                if tokenizeEngineeringString[i] == 'engineering':
                    engineeringContextSlice = tokenizeEngineeringString[i - 5:i]
                    concatenateEngineeringWithWord = []
                    for i in engineeringContextSlice:
                        concatenateEngineeringWithWord.append('%s engineering' % i)

                    for i in concatenateEngineeringWithWord:
                        checkEngineeringMajors = Parser(i, self.majorOptions)
                        if checkEngineeringMajors.doesMatchExist():
                            for i in checkEngineeringMajors.getResult():
                                self.resultList.append(i)
            if 'engineering' in self.resultList:
                self.resultList.remove('engineering')

        self.resultList = list(set(self.resultList))

        self.requirementValue = ', '.join(self.resultList)
        return self.requirementValue

    def getScholarshipPackageRequirementFormat(self):
        if self.getMajors() != '':
            Majors_SPRF = ScholarshipPackageRequirement(self.scholarshipPackageId, self.attributeId,
                                                        self.requirementTypeCode, self.getMajors(), self.logicGroup)

            return Majors_SPRF

    @staticmethod
    def majorsListForTesting():
        MajorOptions = ['accounting', 'adult gerontology acute care', 'nurse practitioner certificate',
                        'advanced clinical pharmacy practice', 'aerospace engineering', 'africana studies',
                        'agribusiness economics', 'agribusiness management', 'agricultural and biosystems engineering',
                        'agricultural and resource economics', 'agricultural education',
                        'agricultural technology management and education', 'american indian studies', 'animal science',
                        'anthropology and linguistics', 'anthropology', 'applied bioscience', 'applied mathematics',
                        'applied science', 'architecture', 'archival studies', 'arid lands resource sciences',
                        'art education',
                        'art history and education', 'art history', 'art and visual culture education', 'astronomy',
                        'atmospheric science', 'audiology', 'biochemistry', 'molecular biology', 'cellular biology',
                        'bioinformatics', 'biology', 'biomedical engineering', 'biostatistics',
                        'business administration',
                        'business economics', 'business intelligence and analytics', 'business management',
                        'cancer biology',
                        'cellular medicine', 'molecular medicine', 'chemical engineering', 'chemistry',
                        'civil engineering',
                        'engineering mechanics', 'classics', 'clinical research', 'translational research',
                        'collaborative governance', 'college teaching', 'commerce', 'communication', 'computer science',
                        'connecting environmental science and decision making', 'correspondence study', 'counseling',
                        'mental health', 'creative writing', 'criminal justice', 'crop production', 'dance',
                        'dendrochronology', 'development practice', 'digital information management',
                        'doctor of medicine',
                        'early childhood education', 'early modern studies', 'east asian studies', 'economic geology',
                        'economics', 'educational leadership and policy', 'educational leadership',
                        'educational psychology',
                        'educational technology', 'electrical and computer engineering', 'electrical engineering',
                        'elementary education', 'engineering', 'engineering management', 'english as a second language',
                        'esl',
                        'entomology', 'insect science', 'environment and water resource economics',
                        'environment hydrology',
                        'environment hydrology and water resources', 'environmental engineering',
                        'environmental health science', 'environmental studies', 'epidemiology', 'esociety',
                        'family and consumer science', 'family studies', 'human development', 'film and television',
                        'finance',
                        "gender and women's studies", 'general biology', 'general studies', 'genetics',
                        'geographic information science', 'geographic information systems technology', 'geography',
                        'geoscience', 'german studies', 'german', 'global health and development', 'global studies',
                        'government and public policy', 'government and public service', 'health behavior',
                        'health promotion',
                        'heritage conservation', 'higher education', 'history and theory of art', 'history',
                        'human language technology', 'hydrology', 'hydrometeorology', 'immunobiology',
                        'indigenous governance',
                        'industrial engineering', 'information resources', 'library science',
                        'information science and arts',
                        'information science and technology', 'integrated science', 'interdisciplinary studies',
                        'international security studies', 'international security', 'italian', 'journalism',
                        'judaic studies',
                        'landscape architecture', 'language', 'latin american studies', 'law',
                        'library and information science', 'linguistics', 'literacy learning and leadership',
                        'management information systems', 'management', 'marketing', 'master of legal studies',
                        'mathematics',
                        'mechanical engineering', 'mexican american studies', 'microbiology and pathobiology',
                        'microbiology', 'middle east studies', 'north african studies', 'mining engineering',
                        'mining geological engineering', 'mining geophysical engineering',
                        'mining occupational safety and health', 'molecular and cellular biology',
                        'motivating learning environments', 'music education', 'music', 'musical arts',
                        'musical theatre',
                        'natural resources', 'natural science for teachers', 'near eastern studies',
                        'neuroscience and cognitive science', 'neuroscience', 'nursing', 'nutritional science',
                        'operations management', 'optical sciences and engineering', 'optical science', 'performance',
                        'pharmaceutical science', 'pharmacology and toxicology', 'pharmacy',
                        'philosophy, politics, economics and law', 'philosophy', 'photonic communications engineering',
                        'physics', 'physiological science', 'physiology', 'planetary science', 'planning',
                        'plant pathology',
                        'plant science', 'political science', 'pre-architecture', 'pre-business',
                        'pre-computer science',
                        'pre-education', 'pre-family studies and human development', 'pre-journalism',
                        'pre-neuroscience',
                        'pre-nursing', 'pre-pharmacy', 'pre-physiology', 'pre-public health',
                        'pre-retailing and consumer science', 'professional geographic information systems technology',
                        'professional studies in health science', 'psychiatric mental health nurse practitioner',
                        'psychology',
                        'public administration', 'public health', 'public management and policy',
                        'real estate development',
                        'regional development', 'rehabilitation', 'religious studies', 'retailing and consumer science',
                        'rhetoric, composition and teaching english', 'russian', 'school psychology',
                        'science education',
                        'second language acquisition and teaching', 'secondary education', 'sociology',
                        'soil, water, and environmental science', 'spanish', 'special education and rehabilitation',
                        'special education', 'special graduate', 'speech, language, and hearing science', 'statistics',
                        'studio art', 'sustainable built environments', 'sustainable plant systems',
                        'systems and industrial engineering', 'systems engineering', 'teaching and teacher education',
                        'theatre arts', 'theatre production', 'transcultural german studies',
                        'urban and regional development',
                        'veterinary science', 'water policy', 'water, society, and policy', 'watershed management',
                        'wildlife and fisheries science', 'network administration', 'japanese']

        MajorOptions = list(set(MajorOptions))
        MajorOptions = '|'.join(MajorOptions)

        return MajorOptions
