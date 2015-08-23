#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Qiqiang Guan'

"""
just a test
"""

# print main.__doc__

import sys

lens = len(sys.argv)
print lens
print sys.argv

i = 1
cmdlists = ['-t', '-p', '-n', '-s', '-g', '-r', '-d', '-v']
while i < lens:
    if sys.argv[i] in cmdlists:
        print sys.argv[i] + ' ---------> ' + sys.argv[i + 1]
        i = i + 2
    elif '-h' == sys.argv[i]:
        print 'display help'
        i = i + 1
    else:
        print sys.argv[i] + ' is a error param'
        i = i + 1


if __name__ == '__main__':
    pass
