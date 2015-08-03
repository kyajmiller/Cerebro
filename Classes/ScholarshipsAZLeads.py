from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from Classes.CleanText import CleanText
from Classes.RipPage import RipPage


class ScholarshipsAZLeads(object):
    def __init__(self, searchTerm, isTest=False):
        self.isTest = isTest
        self.searchTerm = searchTerm
        self.driver = webdriver.Firefox()
