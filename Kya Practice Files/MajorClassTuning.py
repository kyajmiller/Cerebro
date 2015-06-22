from Classes.Majors import Majors
import pyodbc
import re

MajorOptions = ['aerospace engineering', 'accounting', 'anthropology', 'arts', 'business management', '\schemistry',
                'chemical engineering', 'civil engineering', 'communication', 'computing & software systems',
                'computer engineering',
                'computer science', 'ecology', 'economics', 'electrical engineering', 'english',
                'environmental engineering', 'environmental sciences', 'entrepreneurship', 'finance', 'geology',
                'history',
                'human resource management', 'hydrogeology', 'hydrology', 'information science', 'information systems',
                'information systems technology management', 'electrical engineering', 'journalism', 'laser optics',
                'library science',
                'linguistics', 'marketing', 'mathematics', 'mechanical engineering', 'medicine', 'metallurgy', 'mining',
                'nursing',
                'physics', 'political science', 'psychology', 'science technology', 'social sciences',
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
                'engineering mechanics', 'physiology', 'computer engineering']

MajorOptions = list(set(MajorOptions))
MajorOptions = '|'.join(MajorOptions)

def ConnectToTheDatabase():
    global cnxn, cursor
    cnxn = pyodbc.connect(r'Driver={SQL Server};Server=SUDB-DEV;Database=Spiderman;Trusted_Connection=yes;')
    cursor = cnxn.cursor()


def GetInfoFromDatabase():
    cursor.execute("SELECT ScholarshipPackageId, Elgibility FROM dbo.DepartmentTestCases WHERE AttributeId =5 OR AttributeId =417")

ConnectToTheDatabase()
GetInfoFromDatabase()

Eligibilities = []
ScholarshipIds = []
while 1:
    row = cursor.fetchone()
    if not row:
        break
    Eligibilities.append(row.Elgibility)
    ScholarshipIds.append(row.ScholarshipPackageId)

for e in range(len(Eligibilities)):
    Eligibility = Eligibilities[e]
    print(ScholarshipIds[e])

    FormattedEligibilities = []
    StripULTag = re.sub('<ul>|</ul>', '', Eligibility)
    Eligibility = StripULTag
    IndividualEligibilities = Eligibility.split('</li>')
    for IndividualEligibility in IndividualEligibilities:
        IndividualEligibility.strip('\r')
        IndividualEligibility.strip('\n')
        StripXMLTags = re.sub('<\/*[a-z]*\s*\/*>', '', IndividualEligibility)
        #need to remove the xml tags first (specificially the end of line) or else the next one will capture the whole
        #string and delete it
        StripRemainingTags = re.sub('<.*>', '', StripXMLTags)
        IndividualEligibility = StripRemainingTags
        FormattedEligibilities.append(IndividualEligibility)

    JoinEligibilitytoString = ', '.join(FormattedEligibilities)
    StripApostrophe = re.sub('\'*\"*', '', JoinEligibilitytoString)
    Stripnbsp = re.sub('&nbsp;', '', StripApostrophe)
    JoinEligibilitytoString = Stripnbsp

    Eligibility = JoinEligibilitytoString

    testMajors = Majors(Eligibility, ScholarshipIds[e], MajorOptions)
    print(Eligibility)
    print(testMajors.getMajors())
    print('\n\n')