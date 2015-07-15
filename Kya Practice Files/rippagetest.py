#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs

from Classes.RipPage import RipPage
from Classes.CleanText import CleanText

# rippedpage = RipPage.getPageSource('http://webapps.acs.org/findawards/detail.jsp?ContentId=CTP_004520')
ripped = RipPage.getPageSource('http://webapps.acs.org/findawards/detail.jsp?ContentId=CNBP_031057')
arr = bytearray(ripped, "utf-8")
print(str(arr))
ripped2=str(arr)
print(ripped2)

