from selenium import webdriver
from Classes.CleanText import CleanText
from Classes.RipPage import RipPage


class TrafficSafetyStoreLeads(object):
    def __init__(self):
        self.driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        self.base_url = 'https://www.trafficsafetystore.com/resources/teen-safe-driving-scholarships'
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(2)

    def getLeads(self):
        titleDivs = self.driver.find_elements_by_xpath("//h2[@class='col-xs-12']")
        titlesList = [titleDiv.get_attribute('textContent') for titleDiv in titleDivs]

        descriptionDivs = self.driver.find_elements_by_xpath("//div[@class='col-md-10 col-md-offset-1']/div[1]/p[1]")
        descriptionsList = [descriptionDiv.get_attribute('textContent') for descriptionDiv in descriptionDivs]

        eligibilityDivs = self.driver.find_elements_by_xpath("//div[@class='col-md-10 col-md-offset-1']/div[1]/p[2]")
        eligbilitiesList = [eligibilityDiv.get_attribute('textContent') for eligibilityDiv in eligibilityDivs]

    def checkIfElementExists(self, xpath):
        checkElementExists = self.driver.find_elements_by_xpath(xpath)
        if checkElementExists != []:
            return True
        else:
            return False
