import re
from Classes.RipPage import RipPage


class PullPageLinkTitleDescriptionToArray(object):
    def __init__(self, htmlSource):
        self.htmlSource = htmlSource
        self.title = ''
        self.pageurl = ''
        self.allurlsonpage = []
        self.description = ''

    def getTitle(self):
        findTitle = re.search('<title>(.*?)</title>', self.htmlSource)
        if findTitle:
            return findTitle.group(1)

