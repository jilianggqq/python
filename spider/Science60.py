#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'PETER'
import urllib
import urllib2
import re
import thread
import time
from bs4 import BeautifulSoup

# the spider for science 60s
url = 'http://www.scientificamerican.com/podcast/60-second-science/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)
reads = response.read()
soup = BeautifulSoup(reads, "lxml")
# print soup.prettify().encode('utf-8')
lis = soup.findAll("li", {'class': 'clearfix'})
# print len(lis)
# print lis
print '###########################first section#################################'
for li in lis:
    # we can use find.find to search subtags
    link = li.find('h3').find('a')
    print link.contents[0]
    print link.attrs['href']
print '###########################second section#################################'
for li in lis:
    download = li.find('p', {'class': 'metaClump'}).find('a', {'class': 'download'})
    print download.attrs
