from selenium import webdriver
from Classes.CleanText import CleanText
from Classes.RipPage import RipPage


class TrafficSafetyStoreLeads(object):
    def __init__(self):
        self.driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        self.base_url = 'https://www.trafficsafetystore.com/resources/teen-safe-driving-scholarships'
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(2)
