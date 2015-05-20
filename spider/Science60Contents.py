#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'PETER'
import urllib
import urllib2
import re
import thread
import time
from bs4 import BeautifulSoup


class Content(object):

    """docstring for content"""

    def __init__(self, url='', filename=''):
        self.url = url
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.filename = filename

    def doRequest(self):
        request = urllib2.Request(self.url, headers=self.headers)
        response = urllib2.urlopen(request)
        reads = response.read()
        soup = BeautifulSoup(reads, "lxml")
        # print soup.prettify().encode('utf-8')
        pinfo = soup.find("section", {'class': 'article-content'}).findAll('p')
        print len(pinfo)
        artcle = ''
        for info in pinfo:
            # print info.contents[0].encode('utf-8')
            contents = info.contents
            for content in contents:
                artcle += str(content.string.encode('utf-8'))
            artcle += '\n\n'
        return artcle

    def writefile(self, contents):
        f = open(self.filename, 'w')
        f.write(contents)
        f.close()

    def start(self):
        artcle = self.doRequest()
        self.writefile(artcle)
        print 'ok'


# c = Content('http://www.scientificamerican.com/podcast/episode/first-woman-mlber-will-probably-pitch/', 'first-woman-mlber-will-probably-pitch.txt')
c = Content('http://www.scientificamerican.com/podcast/episode/seashell-shapes-show-strength-for-safety1/', 'seashell-shapes-show-strength-for-safety1.txt')

c.start()

# the spider for science 60s
# url = 'http://www.scientificamerican.com/podcast/episode/first-woman-mlber-will-probably-pitch/'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# headers = {'User-Agent': user_agent}
# request = urllib2.Request(url, headers=headers)
# response = urllib2.urlopen(request)
# reads = response.read()
# soup = BeautifulSoup(reads, "lxml")
# print soup.prettify().encode('utf-8')
# pinfo = soup.find("section", {'class': 'article-content'}).findAll('p')
# print len(pinfo)
# print pinfo
# f = open('first-woman-mlber-will-probably-pitch.txt', 'w')
# artcle = ''
# for info in pinfo:
# print info.contents[0].encode('utf-8')
#     contents = info.contents
#     for content in contents:
#         artcle += str(content.string.encode('utf-8'))
#     artcle += '\n'
# f.write(artcle)
# f.close()
