from selenium import webdriver
from Classes.RipPage import RipPage
from Classes.CleanText import CleanText


class MastersInEducationLeads(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.base_url = 'http://www.mastersineducation.net/'
        self.driver.get(self.base_url + 'scholarships')
        self.driver.implicitly_wait(2)

        self.getInfoOnCurrentPage()

    def getInfoOnCurrentPage(self):
        visibleClickyDivs = self.driver.find_elements_by_xpath(
            "//section[@class='scholarships']/div[@class='tab h-results']/div[@class='h-result js-has-toggle']/div[@class='h-result-header js-toggle']")
        for clickyDiv in visibleClickyDivs:
            clickyDiv.click()


MastersInEducationLeads()
