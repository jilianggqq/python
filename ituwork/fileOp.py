#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sysConfig import SysConfig
from commonMechine import CommonMechine
from mechines import *
import os
import shutil


class FileOp(object):

    """docstring for FileOp"""

    files = {'pwr': 'pwr/final.md', 'pnr': 'pnr/final.md',
             'drc': 'drc/final.md', 'lvs': 'lvs/final.md', 'syn': 'syn/final.md'}

    def __init__(self, mechine):
        super(FileOp, self).__init__()
        self.mechine = mechine
        # self.directs = ('pwr', 'pnr', 'drc', 'lvs', 'syn')

    # get file contents
    def getDrcContent(self):
        return 'drc -top_cell {0} -gds {1} -deck {2}'.format(self.mechine.gettop(), self.mechine.getgds(), self.mechine.getdrc())

    def getLvsContent(self):
        return 'lvs -top {0} -gds {1} -sch {2} -deck {3}'.format(self.mechine.gettop(), self.mechine.getgds(), self.mechine.getsch(), self.mechine.getlvs())

    # Logic Synthesis file
    def getSynContent(self):
        with open('templates/synthesis.conf', 'r') as f:
            template = f.read()
        return template

    # Power/IR/EM file
    def getPwrContent(self):
        with open('templates/power.conf', 'r') as f:
            template = f.read()
        return template.format(self.mechine.getlef(), self.mechine.getgds(), self.mechine.getsch(), self.mechine.getpwr(), self.mechine.getsdc(), self.mechine.getdef())

        # Power/IR/EM file
    def getPnrContent(self):
        with open('templates/dtmf.conf', 'r') as f:
            template = f.read()
        return template.format("{0}", '{1}', "{}", sdc=self.mechine.getsdc(), lef=self.mechine.getlef())

    def writePnr(self):
        self.__writefile(FileOp.files["pnr"], self.getPnrContent())

    def writePwr(self):
        self.__writefile(FileOp.files['pwr'], self.getPwrContent())

    def writeDrc(self):
        FileOp.files[''] = 'drc/final.md'
        self.__writefile(FileOp.files['drc'], self.getDrcContent())

    def writeLvs(self):
        FileOp.files[''] = 'lvs/final.md'
        self.__writefile(FileOp.files['lvs'], self.getLvsContent())

    def writeSyn(self):
        FileOp.files[''] = 'syn/final.md'
        self.__writefile(FileOp.files['syn'], self.getSynContent())

    def writefile(self):
        self.writePnr()
        self.writePwr()
        self.writeDrc()
        self.writeLvs()
        self.writeSyn()

    @staticmethod
    def clear():
        for direct, filename in FileOp.files.iteritems():
            if os.path.exists(os.path.dirname(filename)):
                shutil.rmtree(direct)
            else:
                print 'not fou'

    def __writefile(self, filename, contents):
        # print '&**********', os.path.dirname(filename)
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
        with open(filename, "w") as f:
            f.write(contents)


