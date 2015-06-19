import re

ClassStandingOptions = ['high school senior', 'freshman', 'sophomore', 'junior', 'senior', 'masters level graduate',
                        'ph.d. level graduate', 'non-degree seeking graduate', 'law school student',
                        'medical school student', 'nursing school student',
                        'doctor of nursing practice', 'dnp', 'post-baccalaureate', 'postdoctoral', 'undergraduate']

ClassStandingOptions = '|'.join(ClassStandingOptions)

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

States = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida',
          'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
          'Maryland',
          'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
          'New Hampshire',
          'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
          'Pennsylvania',
          'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia',
          'Washington',
          'West Viriginia', 'Wisconsin', 'Wyoming', 'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI',
          'ID', 'IL',
          'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM',
          'NY', 'NC',
          'ND', 'OH', 'OK', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

States = '|\s'.join(States)

MajorUSCities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia', 'Phoenix', 'San Antonio',
                 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'San Francisco', 'Indianapolis',
                 'Columbus', 'Fort Worth',
                 'Charolotte', 'Detroit', 'El Paso', 'Seattle', 'Denver', 'Washington', 'Memphis', 'Boston',
                 'Nashville', 'Baltimore',
                 'Oklahoma City', 'Portland', 'Las Vegas', 'Louisville', 'Milwaukee', 'Albuquerque', 'Tucson', 'Fresno',
                 'Sacramento',
                 'Long Beach', 'Kansas City', 'Mesa', 'Atlanta', 'Virginia Beach', 'Omaha', 'Colorado Springs',
                 'Raleigh', 'Miami',
                 'Oakland', 'Minneapolis', 'Tulsa', 'Cleveland', 'Wichita', 'New Orleans', 'Arlington', 'Bakersfield',
                 'Tampa', 'Aurora',
                 'Honolulu', 'Anaheim', 'Santa Ana', 'Corpus Christi', 'Riverside', 'St. Louis', 'Lexington',
                 'Pittsburgh', 'Stockton',
                 'Anchorage', 'Cincinnati', 'Saint Paul', 'Greensboro', 'Toledo', 'Newark', 'Plano', 'Henderson',
                 'Lincoln', 'Orlando',
                 'Jersey City', 'Chula Vista', 'Buffalo', 'Fort Wayne', 'Chandler', 'St. Petersburg', 'Laredo',
                 'Durham', 'Irvine',
                 'Madison', 'Norfolk', 'Lubbock', 'Gilbert', 'Winston-Salem', 'Reno', 'Hialeah', 'Garland',
                 'Chesapeake', 'Irving',
                 'Scottsdale', 'Baton Rouge', 'Fremont', 'Richmond', 'Boise', 'San Bernardino', 'Birmingham', 'Spokane',
                 'Rochester',
                 'Modesto', 'Des Moines', 'Oxnard', 'Tacoma', 'Fontana', 'Fayetteville', 'Moreno Valley', 'Columbus',
                 'Huntington Beach',
                 'Yonkers', 'Montgomery', 'Aurora', 'Glendale', 'Shreveport', 'Akron', 'Little Rock', 'Amarillo',
                 'Augusta', 'Mobile',
                 'Grand Rapids', 'Salt Lake City', 'Huntsville', 'Tallahassee', 'Grand Prairie', 'Overland Park',
                 'Knoxville',
                 'Brownsville', 'Worchester', 'Newport News', 'Santa Clarita', 'Providence', 'Fort Lauderdale',
                 'Garden Grove',
                 'Oceanside', 'Rancho Cucamonga', 'Santa Rosa', 'Port St. Lucie', 'Chattanooga', 'Tempe', 'Jackson',
                 'Cape Coral',
                 'Vancouver', 'Ontario', 'Sioux Falls', 'Peoria', 'Springfield', 'Pembroke Pines', 'Elk Grove', 'Salem',
                 'Lancaster',
                 'Eugene', 'Palmdale', 'McKinney', 'Salinas', 'Fort Collins', 'Cary', 'Hayward', 'Pasadena', 'Macon',
                 'Pomona',
                 'Alexandria', 'Escondido', 'Sunnyvale', 'Lakewood', 'Kansas City', 'Rockford', 'Torrance', 'Hollywood',
                 'Joliet',
                 'Bridgeport', 'Clarksville', 'Patterson', 'Naperville', 'Frisco', 'Mesquite', 'Savannah', 'Syracuse',
                 'Dayton',
                 'Pasadena', 'Orange', 'Fullerton', 'McAllen', 'Kileen', 'Hampton', 'Bellevue', 'Warren', 'Miramar',
                 'West Valley City',
                 'Olathe', 'Columbia', 'Sterling Heights', 'Thornton', 'New Haven', 'Waco', 'Charleston',
                 'Thousand Oaks', 'Visalia',
                 'Cedar Rapids', 'Elizabeth', 'Roseville', 'Gainesville', 'Corrollton', 'Stamford', 'Denton', 'Midland',
                 'Coral Springs',
                 'Concord', 'Topeka', 'Simi Valley', 'Surprise', 'Lafayette', 'Kent', 'Hartford', 'Santa Clara',
                 'Victorville',
                 'Abilene', 'Murfreesboro', 'Evansville', 'Vallejo', 'Athens', 'Allentown', 'Berkeley', 'Norman',
                 'Ann Arbor',
                 'Beaumont', 'Independence', 'El Monte', 'Fargo', 'Lansing', 'Odessa', 'Downey', 'Wilmington', 'Arvana',
                 'Costa Mesa',
                 'Round Rock', 'Carlsbad', 'Miami Gardens', 'Westminster', 'Inglewood', 'Rochester', 'Fairfield',
                 'Elgin', 'West Jordan',
                 'Clearwater', 'Manchester', 'Lowell', 'Gresham', 'Cambridge', 'Ventura', 'Temecula', 'Waterbury',
                 'Antioch', 'Billings',
                 'High Point', 'Richardson', 'West Covina', 'Pueblo', 'Murrieta', 'Centennial', 'Nowalk', 'Charleston',
                 'Everett',
                 'Pompano Beach', 'Daly City', 'Palm Bay', 'Burbank', 'Wichita Falls', 'Boulder', 'Green Bay',
                 'Broken Arrow',
                 'West Palm Beach', 'College Station', 'Pearland', 'Santa Maria', 'El Cajon', 'San Mateo', 'Lewisville',
                 'Rialto',
                 'Davenport', 'Lakeland', 'Clovis', 'Sandy Springs', 'Tyler', 'Las Cruces', 'South Bend']

MajorUSCities = '|'.join(MajorUSCities)

ArizonaCounties = ['Apache', 'Cochise', 'Coconino', 'Gila', 'Graham', 'Greenlee', 'La Paz', 'Maricopa',
                   'Mohave', 'Navajo', 'Pima', 'Pinal', 'Santa Cruz', 'Yavapai', 'Yuma']

ArizonaCounties = '|'.join(ArizonaCounties)

CountriesNationalities = ['U.S.', 'US', 'United States', 'China', 'Japan', 'Germany', 'United Kingdom', 'France', 'Brazil', 'Italy',
             'India', 'Russia', 'Canada', 'Australia', 'South Korea', 'Spain', 'Mexico', 'Indonesia', 'Netherlands',
             'Turkey', 'Saudi Arabia', 'Switzerland',
             'American', 'Chinese', 'Japanese', 'German', 'British', 'French', 'Brazilian', 'Italian', 'Indian',
             'Russian', 'Canadian', 'Australian', 'South Korean', 'Spanish', 'Mexican', 'Indonesian', 'Dutch',
             'Turkish',
             'Saudi Arabian', 'Swiss']

CountriesNationalities = '|'.join(CountriesNationalities)

Demographics = ['American Indian', 'Alaskan Native', 'Alaska Native', 'Asian American', 'African American', 'Black',
                'Hispanic', 'Latino',
                'Native Hawaiian', 'Pacific Islander', 'White', 'Caucasian', 'Other', 'Middle Eastern',
                'Mexican American', 'Native American',
                'Minority', 'minority', 'International', 'Asian', 'Canadian First Nations', 'African\-American']

Demographics = '|'.join(Demographics)

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

UAColleges = ['agriculture & life sciences', 'agriculture and life sciences',
              'architecture, planning & landscape architecture',
              'architecture planning and landscape architecture', 'education', 'engineering', 'fine arts', 'humanities',
              'medicine', 'nursing', 'optical science', 'pharmacy', 'science', 'social and behavioral science',
              'letters, arts and science',
              'management', 'eller', 'honors', 'law', 'james e. rogers', 'public health', 'outreach college',
              'graduate college', 'school of art', 'landscape architecture', 'snre']

UAColleges = '|'.join(UAColleges)

class Parser:
    def __init__(self, stringToScan, searchCriteria):
        self.searchCriteria = searchCriteria
        self.stringToScan = stringToScan
        self.result = 'No Match.'

    def printStringToScan(self):
        print(self.stringToScan)

    def scanString(self):
        findMatch = re.findall(self.searchCriteria, self.stringToScan)
        if findMatch:
            self.result = findMatch
            return True

    def getResult(self):
        self.scanString()
        return self.result


class GPA(Parser):
    def __init__(self, stringToScan):
        Parser.__init__(self, stringToScan, '[1234]\.\d+')
        self.stringToScan = stringToScan
        self.resultList = []

    def checkContext(self):
        contextChecker = Parser(self.stringToScan.lower(), 'gpa|grade\spoint\saverage|maintain')
        if contextChecker.scanString():
            return True

    def getGPA(self):
        if self.checkContext() and self.scanString():
            self.resultList.append(self.result[0])

            print('GPA: %s' % self.resultList)


class ClassStanding(Parser):
    # needs work, currently does not allow for context dependent matches
    def __init__(self, stringToScan):
        Parser.__init__(self, stringToScan.lower(), ClassStandingOptions)
        self.stringToScan = stringToScan
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        if contextChecker.scanString():
            return True

    def getClassStanding(self):
        if self.scanString():
            for i in self.result:
                self.resultList.append(i)

        if self.checkContext('year'):
            findYear = Parser(self.stringToScan.lower(), '1st|2nd|3rd|4th|5th|6th')
            if findYear.scanString():
                for i in findYear.result:
                    self.resultList.append(i)

        if self.checkContext('upper\-division|upper\sdivision'):
            self.resultList.append('junior')
            self.resultList.append('senior')

        if not self.checkContext('graduate\sfrom|graduates'):
            findGraduate = Parser(self.stringToScan.lower(), '^graduate|\sgraduate')
            if findGraduate.scanString():
                self.resultList.append('graduate')

        if self.checkContext('medical|medicine|md') and not self.checkContext(
                'upper\-division|upper\sdivision|undergraduate|biomedical'):
            self.resultList.append('medical school student')

        if self.checkContext("masters|master's"):
            self.resultList.append('masters level graduate')

        if self.checkContext('ph\.d|phd|ph\sd'):
            self.resultList.append('ph.d. level graduate')

        self.resultList = list(set(self.resultList))
        print('Class Standing: %s' % self.resultList)


class Majors(Parser):
    def __init__(self, stringToScan):
        Parser.__init__(self, stringToScan.lower(), MajorOptions)
        self.stringToScan = stringToScan
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        if contextChecker.scanString():
            return True

    def getMajors(self):
        if self.checkContext(
                'enrolled in|majoring in|program|major|concentration|pursuing|student') and self.scanString():
            for i in self.result:
                self.resultList.append(i)

        self.resultList = list(set(self.resultList))

        specializedEngineeringMajors = ['aerospace engineering', 'chemical engineering', 'computer engineering',
                                        'electrical engineering',
                                        'environmental engineering', 'biosystems engineering',
                                        'bio systems engineering', 'geological engineering', 'mining engineering',
                                        'biomedical engineering', 'nuclear engineering', 'civil engineering',
                                        'mechanical engineering', 'engineering management']

        for SpecializedEngineeringMajor in specializedEngineeringMajors:
            if SpecializedEngineeringMajor in self.resultList and 'engineering' in self.resultList:
                self.resultList.remove('engineering')

        print('Majors: %s' % self.resultList)


class SATScore(Parser):
    def __init__(self, stringToScan):
        Parser.__init__(self, stringToScan, '\s\d{3,4}\s')
        self.stringToScan = stringToScan
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        if contextChecker.scanString():
            return True

    def getSATScore(self):
        if self.checkContext('sat|sat\sscore') and self.scanString():
            self.resultList.append(self.result[0].strip())

        print('SAT Score: %s' % self.resultList)


class HighSchoolState(Parser):
    def __init__(self, stringToScan):
        Parser.__init__(self, stringToScan, States)
        self.stringToScan = stringToScan
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        if contextChecker.scanString():
            return True

    def getHighSchoolState(self):
        if self.checkContext('high school') and self.scanString():
            for i in self.result:
                self.resultList.append(i.strip())

        self.resultList = list(set(self.resultList))
        print('High School State: %s' % self.resultList)


class HighSchoolCity(Parser):
    def __init__(self, stringToScan):
        Parser.__init__(self, stringToScan, MajorUSCities)
        self.stringToScan = stringToScan
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        if contextChecker.scanString():
            return True

    def getHighSchoolCity(self):
        if self.checkContext('high school') and self.scanString():
            for i in self.result:
                self.resultList.append(i.strip())

        self.resultList = list(set(self.resultList))
        print('High School City: %s' % self.resultList)


class HighSchoolArizonaCounty(Parser):
    def __init__(self, stringToScan):
        Parser.__init__(self, stringToScan, ArizonaCounties)
        self.stringToScan = stringToScan
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        if contextChecker.scanString():
            return True

    def getHighSchoolArizonaCounty(self):
        if self.checkContext('high school') and self.checkContext('county|counties') and self.scanString():
            for i in self.result:
                self.resultList.append(i)

        self.resultList = list(set(self.resultList))
        print('High School Arizona County: %s' % self.resultList)


class ResidencyState(Parser):
    def __init__(self, stringToScan):
        Parser.__init__(self, stringToScan, States)
        self.stringToScan = stringToScan
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        if contextChecker.scanString():
            return True

    def getResidencyState(self):
        if self.checkContext('resident|reside|residency|live|live\sin') and self.scanString():
            for i in self.result:
                self.resultList.append(i.strip())

        self.resultList = list(set(self.resultList))
        print('State of Residency: %s' % self.resultList)


class ResidencyArizonaCounty(Parser):
    def __init__(self, stringToScan):
        Parser.__init__(self, stringToScan, ArizonaCounties)
        self.stringToScan = stringToScan
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        if contextChecker.scanString():
            return True

    def getResidencyArizonaCounty(self):
        if self.checkContext('resident|reside|residency|live|live\sin') and self.checkContext(
                'county|counties') and self.scanString():
            for i in self.result:
                self.resultList.append(i)

        self.resultList = list(set(self.resultList))
        print('Arizona County of Residence: %s' % self.resultList)


class RequiredUnits(Parser):
    def __init__(self, stringToScan):
        Parser.__init__(self, stringToScan, '\d{1,3}')
        self.stringToScan = stringToScan
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        if contextChecker.scanString():
            return True

    def getRequiredUnits(self):
        if self.checkContext('units?') and self.scanString():
            self.resultList.append(self.result[0])

        print('Required Units: %s' % self.resultList)


class RequiredGender(Parser):
    def __init__(self, stringToScan):
        Parser.__init__(self, stringToScan.lower(), '\smale|female')
        self.stringToScan = stringToScan
        self.resultList = []

    def getRequiredGender(self):
        if self.scanString():
            self.resultList.append(self.result[0])

        print('Required Gender: %s' % self.resultList)


class Citizenship(Parser):
    def __init__(self, stringToScan):
        Parser.__init__(self, stringToScan, CountriesNationalities)
        self.stringToScan = stringToScan
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        if contextChecker.scanString():
            return True

    def getCitizenship(self):
        if self.checkContext('citizen') and self.scanString():
            for i in self.result:
                self.resultList.append('%s citizen' % i)

        if self.checkContext('\snational') and self.scanString():
            for i in self.result:
                self.resultList.append('%s national' % i)

        if self.checkContext('resident alien'):
            self.resultList.append('permanent resident alien')

        self.resultList = list(set(self.resultList))
        print('Citizenship: %s' % self.resultList)


class Ethnicity(Parser):
    def __init__(self, stringToScan):
        Parser.__init__(self, stringToScan, Demographics)
        self.stringToScan = stringToScan
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        if contextChecker.scanString():
            return True

    def getEthnicity(self):
        if self.checkContext('ethnicity|descent|lineage|ancestry|be\sa') and self.scanString():
            for i in self.result:
                self.resultList.append(i)
        elif not self.checkContext('major|department|studies|language') and self.scanString():
            for i in self.result:
                self.resultList.append(i)

        self.resultList = list(set(self.resultList))
        print('Ethnicity: %s' % self.resultList)


class FAFSA(Parser):
    def __init__(self, stringToScan):
        Parser.__init__(self, stringToScan.lower(), 'fafsa')
        self.stringToScan = stringToScan
        self.resultList = []

    def getFAFSA(self):
        if self.scanString():
            self.resultList.append('yes')

        print('FAFSA Required: %s' % self.resultList)


class EnrollmentStatus(Parser):
    def __init__(self, stringToScan):
        Parser.__init__(self, stringToScan.lower(), 'full\-time|part\-time|full\stime|part\stime')
        self.stringToScan = stringToScan
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        if contextChecker.scanString():
            return True

    def getEnrollmentStatus(self):
        if self.checkContext('enroll') and self.scanString():
            for i in self.result:
                self.resultList.append(i)
        elif not self.checkContext('work|employ|job') and self.scanString():
            for i in self.result:
                self.resultList.append(i)

        self.resultList = list(set(self.resultList))
        print('Enrollment Status: %s' % self.resultList)


class EmploymentStatus(Parser):
    def __init__(self, stringToScan):
        Parser.__init__(self, stringToScan.lower(), 'full\-time|part\-time|full\stime|part\stime')
        self.stringToScan = stringToScan
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        if contextChecker.scanString():
            return True

    def getEmploymentStatus(self):
        if self.checkContext('work|employ|job'):
            if self.scanString():
                for i in self.result:
                    self.resultList.append(i)
            elif self.checkContext('hour'):
                findHours = Parser(self.stringToScan.lower(), '\d{1,2}')
                if findHours.stringToScan():
                    self.resultList.append(findHours.result[0])

        self.resultList = list(set(self.resultList))
        print('Employment Status: %s' % self.resultList)


class InterestsandActivites(Parser):
    def __init__(self, stringToScan):
        Parser.__init__(self, stringToScan.lower(), ListInterestsandActivities)
        self.stringToScan = stringToScan
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        if contextChecker.scanString():
            return True

    def getInterestsandActivities(self):
        if self.checkContext('interest|activity|career|hobby|achievement|demonstrate|involve|activities|commit') and self.scanString():
            for i in self.result:
                self.resultList.append(i)

        self.resultList = list(set(self.resultList))
        print('Interests and Activities: %s' % self.resultList)


class AboutMe(Parser):
    def __init__(self, stringToScan):
        Parser.__init__(self, stringToScan.lower(), ListAboutMeAttributes)
        self.stringToScan = stringToScan
        self.resultList = []

    def getAboutMe(self):
        if self.scanString():
            for i in self.result:
                self.resultList.append(i)

        self.resultList = list(set(self.resultList))
        print('About Me Attributes: %s' % self.resultList)


class UACollege(Parser):
    def __init__(self, stringToScan):
        Parser.__init__(self, stringToScan.lower(), UAColleges)
        self.stringToScan = stringToScan
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        if contextChecker.scanString():
            return True

    def getUACollege(self):
        if self.checkContext('college|college\sof|school\sof') and self.scanString():
            for i in self.result:
                self.resultList.append(i)

        self.resultList = list(set(self.resultList))
        print('UA College: %s' % self.resultList)



testGPAParser = GPA('The GPA is 3.159 not 5.449')
testGPAParser.getGPA()

testClassStandingParser = ClassStanding(
    'Must be an undergraduate student, junior, senior, 4th year, 5th upper division md student')
testClassStandingParser.getClassStanding()

testClassStandingParser = ClassStanding('Must be an student, junior, senior, 4th year md student')
testClassStandingParser.getClassStanding()

testMajorParser = Majors('Must be pursuing a major in chemical engineering or linguistics')
testMajorParser.getMajors()

testSATParser = SATScore('I got a 1600 on my SAT test.')
testSATParser.getSATScore()

testHighSchoolStateParser = HighSchoolState(
    'I went to high school in Tucson, Arizona, New York, and Virginia Beach, VA')
testHighSchoolStateParser.getHighSchoolState()

testHighSchoolCity = HighSchoolCity(
    'I went to high school in Tucson, Arizona, New York City, New York, and Virginia Beach, VA')
testHighSchoolCity.getHighSchoolCity()

testArizonaCounty = HighSchoolArizonaCounty('Must have gone to high school in Pima, Maricopa or Yuma counties')
testArizonaCounty.getHighSchoolArizonaCounty()
