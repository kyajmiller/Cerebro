from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


class GoogleLeads(object):
    def __init__(self, searchTerm):
        self.searchTerm = searchTerm
        self.driver = webdriver.Firefox()
        self.base_url = 'https://www.google.com/'
        self.arrayOfGoogleLeads = []

    def goToGoogleAndGetResults(self):
        driver = self.driver
        driver.get(self.base_url + '/?gws_rd=ssl')
        driver.find_element_by_id('lst-ib').clear()
        driver.find_element_by_id('lst-ib').send_keys(self.searchTerm)
        driver.find_element_by_name('btnG').click()
        driver.implicitly_wait(2)

        arrayOfTitles = driver.find_elements_by_xpath("//h3[contains(concat(' ', @class, ' '), 'r')]")
        arrayOfLinks = driver.find_elements_by_xpath("//h3[contains(concat(' ', @class, ' '), 'r')]/a")
        arrayOfDescriptions = driver.find_elements_by_xpath("//span[contains(concat(' ', @class, ' '), 'st')]")

        if len(arrayOfTitles) == len(arrayOfLinks) == len(arrayOfDescriptions):
            for i in range(len(arrayOfTitles)):
                elementTitle = arrayOfTitles[i].text
                elementLink = arrayOfLinks[i].text
                elementDescription = arrayOfDescriptions[i].text

                singleResultArray = [elementTitle, elementLink, elementDescription]
                self.arrayOfGoogleLeads.append(singleResultArray)

            driver.quit()

            return self.arrayOfGoogleLeads
        else:
            print('no')
