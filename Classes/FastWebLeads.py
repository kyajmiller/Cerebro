from selenium import webdriver
from Classes.CleanText import CleanText


class FastWebLeads(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.base_url = 'http://www.fastweb.com/'

        self.driver.get(self.base_url)
        self.driver.find_element_by_xpath("//a[@class='login']").click()
        self.driver.find_element_by_id('login').clear()
        self.driver.find_element_by_id('login').send_keys('crawlyjones@gmail.com')
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys('sasgcoders')
        self.driver.find_element_by_id('user_form_submit').click()
        self.driver.implicitly_wait(2)

        self.driver.find_element_by_link_text('See my matches').click()
        self.driver.implicitly_wait(2)

        self.driver.find_element_by_xpath("//a[text() = 'All Matches']").click()
        self.driver.implicitly_wait(2)

        self.resultPagesArrays = []

    def getResultsOnCurrentPage(self):
        titlesList = self.getTitlesList()
        resultPageUrlsList = self.getResultsPageUrlsList()
        sponsorsList = self.getSponsorsList()
        amountsList = self.getAmountsList()
        deadlinesList = self.getDeadlinesList()

        for i in range(len(titlesList)):
            title = titlesList[i]
            url = resultPageUrlsList[i]
            sponsor = sponsorsList[i]
            amount = amountsList[i]
            deadline = deadlinesList[i]

            resultPageArray = [title, url, sponsor, amount, deadline]
            self.resultPagesArrays.append(resultPageArray)

    def getTitlesList(self):
        titlesList = []

        titlesDivs = self.driver.find_elements_by_xpath("//h3/a")
        for title in titlesDivs:
            titlesList.append(title.get_attribute('textContent'))

        titlesList = [CleanText.cleanALLtheText(title) for title in titlesList]
        return titlesList

    def getResultsPageUrlsList(self):
        resultsPageUrlsList = []

        urlsDivs = self.driver.find_elements_by_xpath("//h3/a")
        for url in urlsDivs:
            resultsPageUrlsList.append(url.get_attribute('href'))

        return resultsPageUrlsList

    def getSponsorsList(self):
        sponsorsList = []

        sponsorsDivs = self.driver.find_elements_by_xpath("//div[@class='provided_by']/p[not (@class='label')]")
        for sponsor in sponsorsDivs:
            sponsorsList.append(sponsor.get_attribute('textContent'))

        sponsorsList = [CleanText.cleanALLtheText(sponsor) for sponsor in sponsorsList]
        return sponsorsList

    def getAmountsList(self):
        amountsList = []

        amountsDivs = self.driver.find_elements_by_xpath("//div[@class='award']/p[not (@class='label')]")
        for amount in amountsDivs:
            amountsList.append(amount.get_attribute('textContent'))

        amountsList = [CleanText.cleanALLtheText(amount) for amount in amountsList]
        return amountsList

    def getDeadlinesList(self):
        deadlinesList = []

        deadlinesDiv = self.driver.find_elements_by_xpath("//div[@class='deadline']/p[not (@class='label')]")
        for deadline in deadlinesDiv:
            deadlinesList.append(deadline.get_attribute('textContent'))

        deadlinesList = [CleanText.cleanALLtheText(deadline) for deadline in deadlinesList]
        return deadlinesList

    def loopThroughPagesAndDoStuff(self):
        nextPageExists = self.checkIfNextPage()
        while nextPageExists:
            self.goToNextPage()
            nextPageExists = self.checkIfNextPage()

    def goToNextPage(self):
        if self.checkIfNextPage():
            self.driver.find_element_by_xpath("//a[@class='next_page']").click()
            self.driver.implicitly_wait(2)

    def checkIfNextPage(self):
        nextPageDiv = self.driver.find_elements_by_xpath("//a[@class='next_page']")
        if nextPageDiv != []:
            return True
        else:
            return False


test = FastWebLeads().getResultsOnCurrentPage()
