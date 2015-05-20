#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'PETER'

import urllib2


class DownloadFile(object):

    def __init__(self, filename, url):
        # super(DownloadFile, self).__init__()
        self.filename = filename
        self.url = url

    def doDownload(self):
        u = urllib2.urlopen(self.url)
        f = open(self.filename, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (self.filename, file_size)

        file_size_dl = 0
        block_sz = 2048

        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            # print chr(8) * (len(status) + 1)
            status = status + chr(8) * (len(status) + 1)
            print status,
        f.close()

    def start(self):
        self.doDownload()

download = DownloadFile('p.mp3', "http://www.scientificamerican.com/podcast/podcast.mp3?fileId=0EB7C7F2-EDB5-48B5-A7630CB76CABA391&ref=sciam")
download.start()
