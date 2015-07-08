import re
from selenium import webdriver


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
        else:

            arrayOfMatchedDivParts = driver.find_elements_by_xpath(
                "//h3[contains(concat(' ', @class, ' '), 'r')]/following-sibling::div/div")
            for element in arrayOfMatchedDivParts:
                elementParts = element.text.split('\n')
                elementLink = elementParts[0]
                if not re.search('http://|https://', elementLink):
                    elementLink = 'http://' + elementLink
                elementTitle = elementParts[1]
                elementDescription = elementParts[2]

                singleResultArray = [elementTitle, elementLink, elementDescription]
                self.arrayOfGoogleLeads.append(singleResultArray)

        driver.quit()

        return self.arrayOfGoogleLeads
