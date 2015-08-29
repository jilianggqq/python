#!/usr/bin/env python
# -*- coding: utf-8 -*-

class CommonMechine(object):
    """docstring for CommonMechine"""
    def __init__(self):
        super(CommonMechine, self).__init__()

    def getDrc(self, topName, gdsPath, drcPath):
        return 'drc -top_cell {0} -gds {1} -deck {2}'.format(topName, gdsPath, drcPath)


if __name__ == '__main__':
    c = CommonMechine()
    print c.getDrc('a','b','c')
