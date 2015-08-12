import re
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Classes.CleanText import CleanText
from Classes.RipPage import RipPage


class IefaLeads(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.base_url = 'http://www.iefa.org/'
        self.driver.get(self.base_url + 'scholarships')
        self.driver.find_element_by_id('LoginForm_username').clear()
        self.driver.find_element_by_id('LoginForm_username').send_keys('crawlyjones@gmail.com')
        self.driver.find_element_by_id('LoginForm_password').clear()
        self.driver.find_element_by_id('LoginForm_password').send_keys('sasgcoders')
        self.driver.find_element_by_name('yt3').click()
        self.driver.implicitly_wait(2)

        self.driver.find_element_by_xpath("//ul[@id='yw8']/li[@id='scholarshipsLink']/a").click()
        self.driver.implicitly_wait(2)
        Select(self.driver.find_element_by_id('pageSize')).select_by_visible_text('100')
        self.goToNextPreviousPageRefreshCache()

        self.arrayOfResultsPagesArrays = []

        self.loopOverResultsPagesAndDoStuff()

        self.driver.quit()

    def loopOverResultsPagesAndDoStuff(self):
        self.getResultsOnCurrentPage()

        pageCounter = 1
        while pageCounter < 12:
            if self.checkIfNextPage():
                self.goToNextPageUrl()
                self.getResultsOnCurrentPage()
            pageCounter += 1

        for individualArray in self.arrayOfResultsPagesArrays:
            title = individualArray[0]
            resultPageLink = individualArray[1]
            majors = individualArray[2]

            leadInfoArray = self.goToIndividualPagesAndGetInfo(resultPageLink)

    def getResultsOnCurrentPage(self):
        titlesList = self.getTitlesList()
        resultsPagesLinksList = self.getResultsPagesLinksList()
        majorsList = self.getMajorsList()

        for i in range(len(titlesList)):
            title = titlesList[i]
            resultPageLink = resultsPagesLinksList[i]
            majors = majorsList[i]

            individualResultsPageArray = [title, resultPageLink, majors]
            self.arrayOfResultsPagesArrays.append(individualResultsPageArray)

    def getTitlesList(self):
        titlesList = []

        featuredTitlesDivs = self.driver.find_elements_by_xpath("//tbody/tr[@class='featured']/td[@width='200px']/a[3]")
        normalTitlesDivs = self.driver.find_elements_by_xpath(
            "//tbody/tr[not (@class='featured')]/td[@width='200px']/a")

        for titleDiv in featuredTitlesDivs:
            titlesList.append(titleDiv.get_attribute('textContent'))
        for titleDiv in normalTitlesDivs:
            titlesList.append(titleDiv.get_attribute('textContent'))

        return titlesList

    def getResultsPagesLinksList(self):
        resultsPagesLinksList = []

        featuredLinksDivs = self.driver.find_elements_by_xpath("//tbody/tr[@class='featured']/td[@width='200px']/a[3]")
        normalLinksDivs = self.driver.find_elements_by_xpath("//tbody/tr[not (@class='featured')]/td[@width='200px']/a")

        for linkDiv in featuredLinksDivs:
            resultsPagesLinksList.append(linkDiv.get_attribute('href'))
        for linkDiv in normalLinksDivs:
            resultsPagesLinksList.append(linkDiv.get_attribute('href'))

        return resultsPagesLinksList

    def getMajorsList(self):
        majorsList = []

        featuredMajorsDivs = self.driver.find_elements_by_xpath(
            "//tbody/tr[@class='featured']/td[@style='width: 95px']")
        normalMajorsDivs = self.driver.find_elements_by_xpath(
            "//tbody/tr[not (@class='featured')]/td[@style='width: 95px']")

        for majorsDiv in featuredMajorsDivs:
            majorsList.append(majorsDiv.get_attribute('textContent'))
        for majorsDiv in normalMajorsDivs:
            majorsList.append(majorsDiv.get_attribute('textContent'))

        return majorsList

    def goToIndividualPagesAndGetInfo(self, resultPageLink):
        pass

    def checkIfNextPage(self):
        checkNextPage = self.driver.find_elements_by_link_text('Next >')
        if checkNextPage != []:
            return True
        else:
            return False

    def goToNextPageClick(self):
        nextPageButton = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Next >')))
        try:
            nextPageButton.click()
            self.driver.implicitly_wait(2)
        except ElementNotVisibleException:
            self.driver.implicitly_wait(2)

    def goToNextPageUrl(self):
        nextPageButton = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Next >')))
        try:
            nextPageUrl = self.driver.find_element_by_link_text('Next >').get_attribute('href')
            self.driver.get(nextPageUrl)
            self.driver.implicitly_wait(2)
        except ElementNotVisibleException:
            self.driver.implicitly_wait(2)

    def goToPreviousPage(self):
        previousPageButton = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, '< Previous')))
        try:
            previousPageButton.click()
            self.driver.implicitly_wait(2)
        except ElementNotVisibleException:
            self.driver.implicitly_wait(2)

    def goToNextPreviousPageRefreshCache(self):
        self.goToNextPageClick()
        self.goToPreviousPage()


IefaLeads()
