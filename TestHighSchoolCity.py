import unittest
from Classes.HighSchoolCity import HighSchoolCity

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

class TestStringMethods(unittest.TestCase):
    def test_HighSchoolCity(self):
        testhighschoolcity = HighSchoolCity('I went to high school in Virginia Beach, Virginia', MajorUSCities)
        self.assertIsNotNone(testhighschoolcity)
        self.assertEqual(testhighschoolcity.checkContext('high\sschool|highschool|hs'), True)
        self.assertEqual(testhighschoolcity.getHighSchoolCity(), ['Virginia Beach'])

        failhighschoolcity = HighSchoolCity('I attend college in Tucson, Arizona', MajorUSCities)
        self.assertIsNotNone(failhighschoolcity)
        self.assertEqual(failhighschoolcity.checkContext('high\sschool|highschool|hs'), False)
        self.assertNotEqual(failhighschoolcity.getHighSchoolCity(), ['Tucson'])
        self.assertEqual(failhighschoolcity.getHighSchoolCity(), [])


if __name__ == '__main__':
    unittest.main()