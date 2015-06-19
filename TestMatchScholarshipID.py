import pyodbc
import sys
import re
import nltk

# =====================================================================
# Lists Used

# eventually need to fix this so that 'OR' (uppercase 'or') doesn't return as OR - Oregon; for now, the OR - Oregon doesn't appear in this list
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

# this list of cities only contains the largest 300 cities (by population) of the United States
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

Countries = ['U.S.', 'US', 'United States', 'China', 'Japan', 'Germany', 'United Kingdom', 'France', 'Brazil', 'Italy',
             'India', 'Russia', 'Canada', 'Australia', 'South Korea', 'Spain', 'Mexico', 'Indonesia', 'Netherlands',
             'Turkey',
             'Saudi Arabia', 'Switzerland']

Nationalities = ['American', 'Chinese', 'Japanese', 'German', 'British', 'French', 'Brazilian', 'Italian', 'Indian',
                 'Russian', 'Canadian', 'Australian', 'South Korean', 'Spanish', 'Mexican', 'Indonesian', 'Dutch',
                 'Turkish',
                 'Saudi Arabian', 'Swiss']

ArizonaCounties = ['Apache', 'Cochise', 'Coconino', 'Gila', 'Graham', 'Greenlee', 'La Paz', 'Maricopa',
                   'Mohave', 'Navajo', 'Pima', 'Pinal', 'Santa Cruz', 'Yavapai', 'Yuma']

FullorPartTimeKeyWords = ['full-time', 'part-time', 'full time', 'part time']

# interests and activities list taken from the SUAA dev website
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

# graduate has its own special conditional statement in the GetClassStanding function
ClassStandingOptions = ['high school senior', 'freshman', 'sophomore', 'junior', 'senior', 'masters level graduate',
                        'ph.d. level graduate', 'non-degree seeking graduate', 'law school student',
                        'medical school student', 'nursing school student',
                        'doctor of nursing practice', 'dnp', 'post-baccalaureate', 'postdoctoral', 'undergraduate']

# issue to solve: any of the majors with 'education' in the name will also return plain education
# need to figure out how to return plain education only if there are no modifiers in front of it
# can't just delete 'education' because of the rare instance where just 'education' is the correct response
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

Demographics = ['American Indian', 'Alaskan Native', 'Alaska Native', 'Asian American', 'African American', 'Black',
                'Hispanic', 'Latino',
                'Native Hawaiian', 'Pacific Islander', 'White', 'Caucasian', 'Other', 'Middle Eastern',
                'Mexican American', 'Native American',
                'Minority', 'minority', 'International', 'Asian', 'Canadian First Nations', 'African-American']

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

UAColleges = ['agriculture & life sciences', 'agriculture and life sciences',
              'architecture, planning & landscape architecture',
              'architecture planning and landscape architecture', 'education', 'engineering', 'fine arts', 'humanities',
              'medicine',
              'nursing', 'optical science', 'pharmacy', 'science', 'social and behavioral science',
              'letters, arts and science',
              'management', 'eller', 'honors', 'law', 'james e. rogers', 'public health', 'outreach college',
              'graduate college',
              'school of art', 'landscape architecture', 'snre']

AttributesPlusIDs = {'GPA': [1, 364], 'Standing': [21], 'Majors': [5, 417], 'SAT Score': [8], 'High School State': [14],
                     'High School City': [13], 'Required Units': [19], 'High School Arizona County': [22],
                     'Residency State': [35],
                     'Gender': [43], 'Citizenship': [49], 'Ethnicity': [137], 'Residency Arizona County': [163],
                     'FAFSA': [169],
                     'Enrollment Status': [171], 'Employment Status': [198], 'Interests and Activities': [229],
                     'About Me': [237],
                     'UA College': [377, 418]}

# =====================================================================

def ConnectToTheDatabase():
    global cnxn, cursor
    cnxn = pyodbc.connect(r'Driver={SQL Server};Server=SUDB-DEV;Database=Spiderman;Trusted_Connection=yes;')
    cursor = cnxn.cursor()


def GetFromDatabase():
    cursor.execute("SELECT TOP 10 * FROM dbo.DepartmentTestCases")


def GetGPA(IndividualEligibility):
    GPA = ''

    FindGPA = re.search(r'gpa|grade\spoint\saverage|maintain', IndividualEligibility.lower())
    if FindGPA:
        FindGPAValue = re.search(r'\d\.\d+', IndividualEligibility)
        if FindGPAValue:
            GPA = FindGPAValue.group()
            # FindCumulative = re.search(r'cumulative', IndividualEligibility.lower())
            # if FindCumulative:
            #    GPA = GPA + ' (cumulative)'

    if GPA != '':
        return GPA


def GetClassStanding(IndividualEligibility):
    Standing = []

    DoesStandingExist = re.search(r'(standing)|(year)|(status)', IndividualEligibility.lower())
    if DoesStandingExist:
        for ClassStandingOption in ClassStandingOptions:
            ClassStanding = re.search('\s' + ClassStandingOption, IndividualEligibility.lower())
            if ClassStanding:
                Standing.append(ClassStandingOption)
    else:
        for ClassStandingOption in ClassStandingOptions:
            ClassStanding = re.search('\s' + ClassStandingOption, IndividualEligibility.lower())
            if ClassStanding:
                Standing.append(ClassStandingOption)

    FindNotGradStudentKeywords = re.search('graduate\sfrom|graduates', IndividualEligibility.lower())
    if not FindNotGradStudentKeywords:
        FindGraduate = re.search('^graduate|\sgraduate', IndividualEligibility.lower())
        if FindGraduate:
            Standing.append('graduate')

    FindYearKeyword = re.search(r'year', IndividualEligibility.lower())
    if FindYearKeyword:
        YearNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th']
        for YearNumber in YearNumbers:
            FindYearNumber = re.search(YearNumber, IndividualEligibility.lower())
            if FindYearNumber:
                Standing.append(FindYearNumber.group() + ' Year')

    FindMedicalKeywords = re.search(r'medical|medicine|md', IndividualEligibility.lower())
    if FindMedicalKeywords:
        FindNotMedicalSchoolKeywords = re.search(r'upper\-division|upper\sdivision|undergraduate|biomedical',
                                                 IndividualEligibility.lower())
        if not FindNotMedicalSchoolKeywords:
            Standing.append('medical school student')

    FindUpperDivision = re.search(r'upper\-division|upper\sdivision', IndividualEligibility.lower())
    if FindUpperDivision:
        Standing.append('junior')
        Standing.append('senior')

    FindPhD = re.search(r'ph\.d|phd|ph\sd', IndividualEligibility.lower())
    if FindPhD:
        Standing.append('ph.d. level graduate')

    FindMasters = re.search(r"masters|master's", IndividualEligibility.lower())
    if FindMasters:
        Standing.append('masters level graduate')

    if Standing != []:
        Standing = list(set(Standing))
        Standing = ', '.join(Standing)
        return Standing


def GetMajor(IndividualEligibility):
    Majors = []

    MajorContextKeywords = ['enrolled in', 'majoring in', 'program', 'major', 'concentration', 'pursuing', 'student']

    for MajorContextKeyword in MajorContextKeywords:
        CheckForMajorContextKeywords = re.search(MajorContextKeyword, IndividualEligibility.lower())
        if CheckForMajorContextKeywords:
            for MajorOption in MajorOptions:
                MajorFound = re.search(MajorOption, IndividualEligibility.lower())
                if MajorFound:
                    Majors.append(MajorOption)

    SpecializedEngineeringMajors = ['aerospace engineering', 'chemical engineering', 'computer engineering',
                                    'electrical engineering',
                                    'environmental engineering', 'biosystems engineering', 'bio systems engineering',
                                    'geological engineering', 'mining engineering',
                                    'biomedical engineering', 'nuclear engineering', 'civil engineering',
                                    'mechanical engineering', 'engineering management']

    for SpecializedEngineeringMajor in SpecializedEngineeringMajors:
        if SpecializedEngineeringMajor in Majors:
            if 'engineering' in Majors:
                Majors.remove('engineering')

    if Majors != []:
        Majors = ', '.join(list(set(Majors)))
        return Majors


def GetSATScore(IndividualEligibility):
    SATScore = ''

    FindSAT = re.search(r'sat\sscore', IndividualEligibility.lower())
    if FindSAT:
        SATScoreValue = re.search(r'\d+', IndividualEligibility.lower())
        if SATScoreValue:
            SATScore = SATScoreValue.group()
    if SATScore != '':
        return SATScore


def GetHighSchoolState(IndividualEligibility):
    HighSchoolState = []

    FindHighSchool = re.search(r'high\sschool', IndividualEligibility.lower())
    if FindHighSchool:
        for State in States:
            StateFound = re.search('\s' + State, IndividualEligibility)
            if StateFound:
                HighSchoolState.append(State)

    if HighSchoolState != []:
        HighSchoolState = ', '.join(HighSchoolState)
        return HighSchoolState


def GetRelevantYear(IndividualEligibility):
    RelevantYear = ''

    FindYear = re.search(r'\d{4}', IndividualEligibility)
    if FindYear:
        RelevantYear = FindYear.group()

    if RelevantYear != '':
        return RelevantYear


def GetHighSchoolCity(IndividualEligibility):
    HighSchoolCity = []

    FindHighSchool = re.search(r'high\sschool', IndividualEligibility.lower())
    if FindHighSchool:
        for MajorUSCity in MajorUSCities:
            CityFound = re.search(MajorUSCity, IndividualEligibility)
            if CityFound:
                HighSchoolCity.append(CityFound.group())

    if HighSchoolCity != []:
        HighSchoolCity = ', '.join(HighSchoolCity)
        return HighSchoolCity


def GetRequiredUnits(IndividualEligibility):
    RequiredUnits = ''

    FindUnits = re.search(r'units', IndividualEligibility.lower())
    if FindUnits:
        RequireUnitsValue = re.search(r'\d{1,3}', IndividualEligibility)
        if RequireUnitsValue:
            RequiredUnits = RequireUnitsValue.group()

    if RequiredUnits != '':
        return RequiredUnits


def GetHighSchoolArizonaCounty(IndividualEligibility):
    HighSchoolArizonaCounty = []

    FindHighSchool = re.search(r'high\sschool', IndividualEligibility.lower())
    if FindHighSchool:
        FindCounty = re.search(r'county|counties', IndividualEligibility.lower())
        if FindCounty:
            for ArizonaCounty in ArizonaCounties:
                FindArizonaCounty = re.search(ArizonaCounty, IndividualEligibility)
                if FindArizonaCounty:
                    HighSchoolArizonaCounty.append(ArizonaCounty)

    if HighSchoolArizonaCounty != []:
        HighSchoolArizonaCounty = ', '.join(HighSchoolArizonaCounty)
        return HighSchoolArizonaCounty


def GetRequiredResidencyState(IndividualEligibility):
    RequiredResidencyState = []

    FindResidency = re.search(r'resident|reside|residency', IndividualEligibility.lower())
    if FindResidency:
        for State in States:
            FindState = re.search('\s' + State, IndividualEligibility)
            if FindState:
                RequiredResidencyState.append(State)

    if RequiredResidencyState != []:
        RequiredResidencyState = ', '.join(RequiredResidencyState)
        return RequiredResidencyState


def GetRequiredGender(IndividualEligibility):
    RequiredGender = ''

    FindGender = re.search(r'female|\smale', IndividualEligibility.lower())
    if FindGender:
        RequiredGender = FindGender.group()
    if RequiredGender == ' male':
        RequiredGender = 'male'

    if RequiredGender != '':
        return RequiredGender


def GetCitizenship(IndividualEligibility):
    Citizenship = []

    FindCitizenship = re.search(r'citizen|citizenship', IndividualEligibility.lower())
    if FindCitizenship:
        for Country in Countries:
            FindCountry = re.search(Country, IndividualEligibility)
            if FindCountry:
                Citizenship.append(Country + ' Citizen')
        for Nationality in Nationalities:
            FindNationality = re.search(Nationality, IndividualEligibility)
            if FindNationality:
                Citizenship.append(Nationality + ' Citizen')

    FindNational = re.search(r'\snational', IndividualEligibility.lower())
    if FindNational:
        for Country in Countries:
            FindCountry = re.search(Country, IndividualEligibility)
            if FindCountry:
                Citizenship.append(Country + ' National')
        for Nationality in Nationalities:
            FindNationality = re.search(Nationality, IndividualEligibility)
            if FindNationality:
                Citizenship.append(Nationality + ' National')

    FindResidentAlien = re.search(r'resident\salien', IndividualEligibility.lower())
    if FindResidentAlien:
        Citizenship.append('Permanent Resident Alien')

    if Citizenship != []:
        Citizenship = ', '.join(Citizenship)
        return Citizenship


def GetEthnicity(IndividualEligibility):
    Ethnicity = []

    FindEthnicityKeywords = re.search('ethnicity|descent|lineage|ancestry|be\sa', IndividualEligibility.lower())
    if FindEthnicityKeywords:
        for Demographic in Demographics:
            FindDemographic = re.search(Demographic, IndividualEligibility)
            if FindDemographic:
                Ethnicity.append(Demographic)
    else:
        NotEthnicityKeyWords = re.search('major|department|studies|language', IndividualEligibility.lower())
        if not NotEthnicityKeyWords:
            for Demographic in Demographics:
                FindDemographic = re.search(Demographic, IndividualEligibility)
                if FindDemographic:
                    Ethnicity.append(Demographic)

    if Ethnicity != []:
        Ethnicity = ', '.join(Ethnicity)
        return Ethnicity


def GetResidencyArizonaCounty(IndividualEligibility):
    ResidencyArizonaCounty = []

    FindResidency = re.search(r'resident|reside|residency', IndividualEligibility.lower())
    if FindResidency:
        FindCounty = re.search(r'county|counties', IndividualEligibility.lower())
        if FindCounty:
            for ArizonaCounty in ArizonaCounties:
                FindArizonaCounty = re.search(ArizonaCounty, IndividualEligibility)
                if FindArizonaCounty:
                    ResidencyArizonaCounty.append(ArizonaCounty)

    if ResidencyArizonaCounty != []:
        ResidencyArizonaCounty = ', '.join(ResidencyArizonaCounty)
        return ResidencyArizonaCounty


def GetFAFSARequirement(IndividualEligibility):
    NeedFAFSA = ''

    FindFAFSA = re.search(r'FAFSA|fafsa', IndividualEligibility)
    if FindFAFSA:
        NeedFAFSA = 'yes'

    if NeedFAFSA == 'yes':
        return NeedFAFSA


def GetEnrollmentStatus(IndividualEligibility):
    EnrollmentStatus = []

    FindEnrollmentStatus = re.search(r'enroll', IndividualEligibility.lower())
    if FindEnrollmentStatus:
        for FullorPartTimeKeyWord in FullorPartTimeKeyWords:
            FindFullorPartTime = re.search(FullorPartTimeKeyWord, IndividualEligibility.lower())
            if FindFullorPartTime:
                EnrollmentStatus.append(FullorPartTimeKeyWord)
    else:
        FindWorkKeyword = re.search(r'work|employ|job', IndividualEligibility.lower())
        if not FindWorkKeyword:
            for FullorPartTimeKeyWord in FullorPartTimeKeyWords:
                FindFullorPartTime = re.search(FullorPartTimeKeyWord, IndividualEligibility.lower())
                if FindFullorPartTime:
                    EnrollmentStatus.append(FullorPartTimeKeyWord)

    if EnrollmentStatus != []:
        EnrollmentStatus = ', '.join(EnrollmentStatus)
        return EnrollmentStatus


def GetEmploymentStatus(IndividualEligibility):
    EmploymentStatus = []

    FindEmploymentStatus = re.search(r'employ|work|job', IndividualEligibility.lower())
    if FindEmploymentStatus:
        for FullorPartTimeKeyWord in FullorPartTimeKeyWords:
            FindFullorPartTime = re.search(FullorPartTimeKeyWord, IndividualEligibility.lower())
            if FindFullorPartTime:
                EmploymentStatus.append(FindFullorPartTime.group())

        FindHours = re.search(r'hour', IndividualEligibility.lower())
        if FindHours:
            FindNumHours = re.search(r'\d{1,2}', IndividualEligibility)
            if FindNumHours:
                EmploymentStatus.append(FindNumHours.group() + ' Hours')

    if EmploymentStatus != []:
        EmploymentStatus = ', '.join(EmploymentStatus)
        return EmploymentStatus


def GetInterestsandActivities(IndividualEligibility):
    InterestsandActivities = []

    FindInterestKeywords = re.search(
        r'interest|activity|career|hobby|achievement|demonstrate|involve|activities|commit',
        IndividualEligibility.lower())
    if FindInterestKeywords:
        for ListInterestsandActivity in ListInterestsandActivities:
            FindInterest = re.search(ListInterestsandActivity, IndividualEligibility.lower())
            if FindInterest:
                InterestsandActivities.append(ListInterestsandActivity)

    if InterestsandActivities != []:
        InterestsandActivities = ', '.join(InterestsandActivities)
        return InterestsandActivities


def GetAboutMeAttributes(IndividualEligibility):
    AboutMeAttributes = []

    for ListAboutMeAttribute in ListAboutMeAttributes:
        FindAboutMeAttributes = re.search(ListAboutMeAttribute, IndividualEligibility.lower())
        if FindAboutMeAttributes:
            AboutMeAttributes.append(ListAboutMeAttribute)

    if AboutMeAttributes != []:
        AboutMeAttributes = ', '.join(AboutMeAttributes)
        return AboutMeAttributes


def GetUACollege(IndividualEligibility):
    RequiredUACollege = []

    FindCollegeKeywords = re.search(r'college|college\sof|school\sof', IndividualEligibility.lower())
    if FindCollegeKeywords:
        for UACollege in UAColleges:
            FindCollege = re.search(UACollege, IndividualEligibility.lower())
            if FindCollege:
                RequiredUACollege.append(UACollege)

    FindSNRE = re.search(r'snre', IndividualEligibility.lower())
    if FindSNRE:
        RequiredUACollege.append('snre')

    if RequiredUACollege != []:
        RequiredUACollege = list(set(RequiredUACollege))
        RequiredUACollege = ', '.join(RequiredUACollege)
        return RequiredUACollege


def GetOnlineDegreeRequirement(IndividualEligibility):
    OnlineDegreeRequirement = ''

    FindOnline = re.search(r'online', IndividualEligibility.lower())
    if FindOnline:
        FindDegreeKeywords = re.search(r'degree|program|major', IndividualEligibility.lower())
        if FindDegreeKeywords:
            OnlineDegreeRequirement = 'yes'

    if OnlineDegreeRequirement == 'yes':
        return OnlineDegreeRequirement

# =====================================================================

ConnectToTheDatabase()
GetFromDatabase()
Eligibilities = []
ScholarshipIDs = []
ScholarshipPackageId = []
LogicGroup = []
# ScholarshipsEntries = {}
while 1:
    row = cursor.fetchone()
    if not row:
        break
    Eligibilities.append(row.Elgibility)
    ScholarshipIDs.append(row.Scholarshipid)
    ScholarshipPackageId.append(row.ScholarshipPackageId)
    LogicGroup.append(row.LogicGroup)
    # ScholarshipsEntries[ScholarshipID] = Eligibilities

    # process the values and figure out what the answer is
    # call a function that inserts your answer into database

for e in range(len(Eligibilities)):

    Eligibility = (Eligibilities[e])

    if ScholarshipIDs[e] != ScholarshipIDs[e - 1]:
        print(ScholarshipIDs[e])

        GPA = ''
        Standing = []
        Majors = ''
        SATScore = ''
        HighSchoolState = ''
        CollegeGraduationYear = ''
        HighSchoolCity = ''
        RequiredUnits = ''
        HighSchoolArizonaCounty = ''
        RequiredResidencyState = ''
        RequiredGender = ''
        Citizenship = ''
        Ethnicity = ''
        ResidencyArizonaCounty = ''
        NeedFAFSA = ''
        EnrollmentStatus = ''
        EmploymentStatus = ''
        InterestsandActivities = ''
        AboutMeAttributes = ''
        RequiredUACollege = ''
        RelevantYear = ''
        OnlineDegreeRequirement = ''

        FormattedEligibilities = []

        StripULTag = re.sub('<ul>|</ul>', '', Eligibility)
        Eligibility = StripULTag
        IndividualEligibilities = Eligibility.split('</li>')
        for IndividualEligibility in IndividualEligibilities:

            IndividualEligibility.strip('\r')
            IndividualEligibility.strip('\n')
            StripXMLTags = re.sub('<\/*[a-z]*\s*\/*>', '', IndividualEligibility)
            # need to remove the xml tags first (specificially the end of line) or else the next one will capture the whole
            # string and delete it
            StripRemainingTags = re.sub('<.*>', '', StripXMLTags)
            IndividualEligibility = StripRemainingTags
            FormattedEligibilities.append(IndividualEligibility)

            if GetGPA(IndividualEligibility) is not None:
                GPA = GetGPA(IndividualEligibility)
            if GetClassStanding(IndividualEligibility) is not None:
                Standing.append(GetClassStanding(IndividualEligibility))
            if GetMajor(IndividualEligibility) is not None:
                Majors = GetMajor(IndividualEligibility)
            if GetSATScore(IndividualEligibility) is not None:
                SATScore = GetSATScore(IndividualEligibility)
            if GetHighSchoolState(IndividualEligibility) is not None:
                HighSchoolState = GetHighSchoolState(IndividualEligibility)
            if GetHighSchoolCity(IndividualEligibility) is not None:
                HighSchoolCity = GetHighSchoolCity(IndividualEligibility)
            if GetRequiredUnits(IndividualEligibility) is not None:
                RequiredUnits = GetRequiredUnits(IndividualEligibility)
            if GetHighSchoolArizonaCounty(IndividualEligibility) is not None:
                HighSchoolArizonaCounty = GetHighSchoolArizonaCounty(IndividualEligibility)
            if GetRequiredResidencyState(IndividualEligibility) is not None:
                RequiredResidencyState = GetRequiredResidencyState(IndividualEligibility)
            if GetRequiredGender(IndividualEligibility) is not None:
                RequiredGender = GetRequiredGender(IndividualEligibility)
            if GetCitizenship(IndividualEligibility) is not None:
                Citizenship = GetCitizenship(IndividualEligibility)
            if GetEthnicity(IndividualEligibility) is not None:
                Ethnicity = GetEthnicity(IndividualEligibility)
            if GetResidencyArizonaCounty(IndividualEligibility) is not None:
                ResidencyArizonaCounty = GetResidencyArizonaCounty(IndividualEligibility)
            if GetFAFSARequirement(IndividualEligibility) is not None:
                NeedFAFSA = GetFAFSARequirement(IndividualEligibility)
            if GetEnrollmentStatus(IndividualEligibility) is not None:
                EnrollmentStatus = GetEnrollmentStatus(IndividualEligibility)
            if GetEmploymentStatus(IndividualEligibility) is not None:
                EmploymentStatus = GetEmploymentStatus(IndividualEligibility)
            if GetInterestsandActivities(IndividualEligibility) is not None:
                InterestsandActivities = GetInterestsandActivities(IndividualEligibility)
            if GetAboutMeAttributes(IndividualEligibility) is not None:
                AboutMeAttributes = GetAboutMeAttributes(IndividualEligibility)
            if GetUACollege(IndividualEligibility) is not None:
                RequiredUACollege = GetUACollege(IndividualEligibility)
            if GetRelevantYear(IndividualEligibility) is not None:
                RelevantYear = GetRelevantYear(IndividualEligibility)
            if GetOnlineDegreeRequirement(IndividualEligibility) is not None:
                OnlineDegreeRequirement = GetOnlineDegreeRequirement(IndividualEligibility)

            print(IndividualEligibility)

        JoinEligibilitytoString = ', '.join(FormattedEligibilities)
        StripApostrophe = re.sub('\'*\"*', '', JoinEligibilitytoString)
        JoinEligibilitytoString = StripApostrophe

        if Standing == []:
            Standing = ''

        Standing = ', '.join(Standing)

        if GPA != '':
            print('GPA:', GPA)
            cursor.execute(
                "INSERT INTO dbo.Tests ( RequirementValue, LogicGroup, Eligibility, AttributeId, RequirementTypeCode, ScholarshipId, AttributeName) VALUES  ( '" + GPA + "', '" + str(
                    LogicGroup[e]) + "','" + JoinEligibilitytoString + "', '1', '>=', '" + str(
                    ScholarshipIDs[e]) + "', 'What is your cumulative UA GPA?' )")
            cursor.commit()
        if Standing != '':
            print('Standing:', Standing)
            cursor.execute(
                "INSERT INTO dbo.Tests ( RequirementValue, LogicGroup, Eligibility, AttributeId, RequirementTypeCode, ScholarshipId, AttributeName) VALUES  ( '" + Standing + "', '" + str(
                    LogicGroup[e]) + "','" + JoinEligibilitytoString + "', '21', '*', '" + str(
                    ScholarshipIDs[e]) + "', 'My Class Status is:' )")
            cursor.commit()
        if Majors != '':
            print('Majors:', Majors)
            Majors = re.sub('\'*\"*', '', Majors)
            cursor.execute(
                "INSERT INTO dbo.Tests ( RequirementValue, LogicGroup, Eligibility, AttributeId, RequirementTypeCode, ScholarshipId, AttributeName) VALUES  ( '" + Majors + "', '" + str(
                    LogicGroup[e]) + "','" + JoinEligibilitytoString + "', '417', '*', '" + str(
                    ScholarshipIDs[e]) + "', 'What majors are you enrolled in?')")
            cursor.commit()
        if SATScore != '':
            print('SAT Score:', SATScore)
            cursor.execute(
                "INSERT INTO dbo.Tests ( RequirementValue, LogicGroup, Eligibility, AttributeId, RequirementTypeCode, ScholarshipId, AttributeName) VALUES  ( '" + SATScore + "', '" + str(
                    LogicGroup[e]) + "','" + JoinEligibilitytoString + "', '8', '>=', '" + str(
                    ScholarshipIDs[e]) + "', 'What is your highest composite SAT Score' )")
            cursor.commit()
        if HighSchoolState != '':
            print('State of High School:', HighSchoolState)
            cursor.execute(
                "INSERT INTO dbo.Tests ( RequirementValue, LogicGroup, Eligibility, AttributeId, RequirementTypeCode, ScholarshipId, AttributeName) VALUES  ( '" + HighSchoolState + "', '" + str(
                    LogicGroup[e]) + "','" + JoinEligibilitytoString + "', '14', '*', '" + str(
                    ScholarshipIDs[e]) + "', 'State of my High School:' )")
            cursor.commit()
        if HighSchoolCity != '':
            print('High School City:', HighSchoolCity)
            cursor.execute(
                "INSERT INTO dbo.Tests ( RequirementValue, LogicGroup, Eligibility, AttributeId, RequirementTypeCode, ScholarshipId, AttributeName) VALUES  ( '" + HighSchoolCity + "', '" + str(
                    LogicGroup[e]) + "','" + JoinEligibilitytoString + "', '13', '*', '" + str(
                    ScholarshipIDs[e]) + "', 'In what city did/will you graduate high school from?' )")
            cursor.commit()
        if RequiredUnits != '':
            print('Required Units:', RequiredUnits)
            cursor.execute(
                "INSERT INTO dbo.Tests ( RequirementValue, LogicGroup, Eligibility, AttributeId, RequirementTypeCode, ScholarshipId, AttributeName) VALUES  ( '" + RequiredUnits + "', '" + str(
                    LogicGroup[e]) + "','" + JoinEligibilitytoString + "', '19', '>=', '" + str(ScholarshipIDs[
                                                                                                    e]) + "', 'How many college units have you completed towards your declared degree?' )")
            cursor.commit()
        if HighSchoolArizonaCounty != '':
            print('Arizona County of High School:', HighSchoolArizonaCounty)
            cursor.execute(
                "INSERT INTO dbo.Tests ( RequirementValue, LogicGroup, Eligibility, AttributeId, RequirementTypeCode, ScholarshipId, AttributeName) VALUES  ( '" + HighSchoolArizonaCounty + "', '" + str(
                    LogicGroup[e]) + "','" + JoinEligibilitytoString + "', '22', '*', '" + str(
                    ScholarshipIDs[e]) + "', 'Which Arizona county did or will you graduate high school from?' )")
            cursor.commit()
        if RequiredResidencyState != '':
            print('State of Residence:', RequiredResidencyState)
            cursor.execute(
                "INSERT INTO dbo.Tests ( RequirementValue, LogicGroup, Eligibility, AttributeId, RequirementTypeCode, ScholarshipId, AttributeName) VALUES  ( '" + RequiredResidencyState + "', '" + str(
                    LogicGroup[e]) + "','" + JoinEligibilitytoString + "', '35', '*', '" + str(ScholarshipIDs[
                                                                                                   e]) + "', 'What state(s) or U.S. territories do you consider yourself a resident of?' )")
            cursor.commit()
        if RequiredGender != '':
            print('Required Gender:', RequiredGender)
            cursor.execute(
                "INSERT INTO dbo.Tests ( RequirementValue, LogicGroup, Eligibility, AttributeId, RequirementTypeCode, ScholarshipId, AttributeName) VALUES  ( '" + RequiredGender + "', '" + str(
                    LogicGroup[e]) + "','" + JoinEligibilitytoString + "', '43', '*', '" + str(
                    ScholarshipIDs[e]) + "', 'What is your gender?' )")
            cursor.commit()
        if Citizenship != '':
            print('Citizenship:', Citizenship)
            cursor.execute(
                "INSERT INTO dbo.Tests ( RequirementValue, LogicGroup, Eligibility, AttributeId, RequirementTypeCode, ScholarshipId, AttributeName) VALUES  ( '" + Citizenship + "', '" + str(
                    LogicGroup[e]) + "','" + JoinEligibilitytoString + "', '49', '*', '" + str(
                    ScholarshipIDs[e]) + "', 'What is your current citizenship status?' )")
            cursor.commit()
        if Ethnicity != '':
            print('Ethnicity:', Ethnicity)
            cursor.execute(
                "INSERT INTO dbo.Tests ( RequirementValue, LogicGroup, Eligibility, AttributeId, RequirementTypeCode, ScholarshipId, AttributeName) VALUES  ( '" + Ethnicity + "', '" + str(
                    LogicGroup[e]) + "','" + JoinEligibilitytoString + "', '137', '*', '" + str(
                    ScholarshipIDs[e]) + "', 'What ethnicity do you identify yourself as?' )")
            cursor.commit()
        if ResidencyArizonaCounty != '':
            print('Arizona County of Residence:', ResidencyArizonaCounty)
            cursor.execute(
                "INSERT INTO dbo.Tests ( RequirementValue, LogicGroup, Eligibility, AttributeId, RequirementTypeCode, ScholarshipId, AttributeName) VALUES  ( '" + ResidencyArizonaCounty + "', '" + str(
                    LogicGroup[e]) + "','" + JoinEligibilitytoString + "', '163', '*', '" + str(
                    ScholarshipIDs[e]) + "', 'What Arizona county are you a permanent resident of?' )")
            cursor.commit()
        if NeedFAFSA != '':
            print('FAFSA Required:', NeedFAFSA)
            cursor.execute(
                "INSERT INTO dbo.Tests ( RequirementValue, LogicGroup, Eligibility, AttributeId, RequirementTypeCode, ScholarshipId, AttributeName) VALUES  ( '" + NeedFAFSA + "', '" + str(
                    LogicGroup[e]) + "','" + JoinEligibilitytoString + "', '169', '=', '" + str(
                    ScholarshipIDs[e]) + "', 'Have you completed a current FAFSA for the academic year?' )")
            cursor.commit()
        if EnrollmentStatus != '':
            print('Required Enrollment:', EnrollmentStatus)
            cursor.execute(
                "INSERT INTO dbo.Tests ( RequirementValue, LogicGroup, Eligibility, AttributeId, RequirementTypeCode, ScholarshipId, AttributeName) VALUES  ( '" + EnrollmentStatus + "', '" + str(
                    LogicGroup[e]) + "','" + JoinEligibilitytoString + "', '171', '*', '" + str(
                    ScholarshipIDs[e]) + "', 'What is your enrollment status for the academic year?' )")
            cursor.commit()
        if EmploymentStatus != '':
            print('Required Employment:', EmploymentStatus)
            cursor.execute(
                "INSERT INTO dbo.Tests ( RequirementValue, LogicGroup, Eligibility, AttributeId, RequirementTypeCode, ScholarshipId, AttributeName) VALUES  ( '" + EmploymentStatus + "', '" + str(
                    LogicGroup[e]) + "','" + JoinEligibilitytoString + "', '198', '*', '" + str(
                    ScholarshipIDs[e]) + "', 'What is your current employment status?' )")
            cursor.commit()
        if InterestsandActivities != '':
            print('Interests and Activities:', InterestsandActivities)
            cursor.execute(
                "INSERT INTO dbo.Tests ( RequirementValue, LogicGroup, Eligibility, AttributeId, RequirementTypeCode, ScholarshipId, AttributeName) VALUES  ( '" + InterestsandActivities + "', '" + str(
                    LogicGroup[e]) + "','" + JoinEligibilitytoString + "', '229', '*', '" + str(
                    ScholarshipIDs[e]) + "', 'My Interests and Activities:' )")
            cursor.commit()
        if AboutMeAttributes != '':
            print('About Me Attributes:', AboutMeAttributes)
            cursor.execute(
                "INSERT INTO dbo.Tests ( RequirementValue, LogicGroup, Eligibility, AttributeId, RequirementTypeCode, ScholarshipId, AttributeName) VALUES  ( '" + AboutMeAttributes + "', '" + str(
                    LogicGroup[e]) + "','" + JoinEligibilitytoString + "', '237', '*', '" + str(
                    ScholarshipIDs[e]) + "', 'About Me:' )")
            cursor.commit()
        if RequiredUACollege != '':
            print('UA College:', RequiredUACollege)
            cursor.execute(
                "INSERT INTO dbo.Tests ( RequirementValue, LogicGroup, Eligibility, AttributeId, RequirementTypeCode, ScholarshipId, AttributeName) VALUES  ( '" + RequiredUACollege + "', '" + str(
                    LogicGroup[e]) + "','" + JoinEligibilitytoString + "', '377', '*', '" + str(
                    ScholarshipIDs[e]) + "', 'UA college(s) of study?' )")
            cursor.commit()
        if RelevantYear != '':
            print('Relevant Year:', RelevantYear)
            cursor.execute(
                "INSERT INTO dbo.Tests ( RequirementValue, LogicGroup, Eligibility, AttributeId, RequirementTypeCode, ScholarshipId, AttributeName) VALUES  ( '" + RelevantYear + "', '" + str(
                    LogicGroup[e]) + "','" + JoinEligibilitytoString + "', '17', '!*', '" + str(
                    ScholarshipIDs[e]) + "', 'What is your current expected college graduation date?' )")
            cursor.commit()
        if OnlineDegreeRequirement != '':
            print('Online Degree Program:', OnlineDegreeRequirement)
            cursor.execute(
                "INSERT INTO dbo.Tests ( RequirementValue, LogicGroup, Eligibility, AttributeId, RequirementTypeCode, ScholarshipId, AttributeName) VALUES  ( '" + OnlineDegreeRequirement + "', '" + str(
                    LogicGroup[e]) + "','" + JoinEligibilitytoString + "', '1003', '=', '" + str(
                    ScholarshipIDs[e]) + "', 'Did you enroll in an online degree program through UA Online?' )")
            cursor.commit()

        print('\n\n')


# print ("done")
cnxn.close()
