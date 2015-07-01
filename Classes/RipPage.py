from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


class RipPage(object):
    @staticmethod
    def getPageSource(url):
        driver = webdriver.Firefox()
        driver.get(url)
        htmlSource = driver.page_source

        return htmlSource
