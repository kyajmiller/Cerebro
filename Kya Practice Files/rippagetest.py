#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Classes.RipPage import RipPage
from Classes.CleanText import CleanText

# rippedpage = RipPage.getPageSource('http://webapps.acs.org/findawards/detail.jsp?ContentId=CTP_004520')
ripped = RipPage.getPageSource('http://webapps.acs.org/findawards/detail.jsp?ContentId=CNBP_031057')
# dripped = ripped.decode('utf-8', 'ignore')
print(ripped)
