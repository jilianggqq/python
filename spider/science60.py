#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'PETER'
import urllib
import urllib2
import re
import thread
import time
import sys
from bs4 import BeautifulSoup
from downloadFile import DownloadFile
from science60Contents import Content
if not len(sys.argv) == 3:
    sys.exit('parameter errror')
# the spider for science 60s
base_url = 'http://www.scientificamerican.com'
url = 'http://www.scientificamerican.com/podcast/60-second-science/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)
reads = response.read()
soup = BeautifulSoup(reads, "lxml")
# print soup.prettify().encode('utf-8')
lis = soup.findAll("li", {'class': 'clearfix'})
date = time.strftime('%Y%m%d')
# print len(lis)
# print lis

downloaddoc = sys.argv[1]
downloadmp3 = sys.argv[2]
isDownloaddoc = False
isDownloadmp3 = False
if downloaddoc and downloaddoc == 'doc':
    isDownloaddoc = True

if downloadmp3 and downloadmp3 == 'mp3':
    isDownloadmp3 = True

print '###########################first section#################################'
for li in lis:
    # we can use find.find to search subtags
    link = li.find('h3').find('a')
    # print link.contents[0]
    contenturl = link.attrs['href']
    title = link.contents[0]
    filep = title
    if isDownloaddoc:
        print '*****************start download doc********************'
        print 'page request url:' + contenturl
        content = Content(filep + '.txt', contenturl)
        content.start()
        print '*****************end download doc********************'

    if isDownloadmp3:
        download = li.find('p', {'class': 'metaClump'}).find('a', {'class': 'download'})
        mp3url = base_url + download.attrs['href']
        print '*****************start download mp3********************'
        print 'mp3 request url:' + mp3url
        download = DownloadFile(filep + ".mp3", mp3url)
        download.start()
        print '*****************end download mp3********************'
print 'download complete'
