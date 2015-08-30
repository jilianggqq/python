#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sysConfig import SysConfig


class CommonMechine(object):

    """docstring for CommonMechine
    def_topcell_name = 'TOP'
    def_gds = '/home/design/top.gds'
    def_sch = '/home/design/top.sch'
    def_def = '/home/design/top.def'
    def_rtl = '/home/design/top.v'
    def_pwr = '5 (volt.)'
    """

    def __init__(self, top=SysConfig.def_topcell_name, gds=SysConfig.def_gds, sch=SysConfig.def_sch, rtl=SysConfig.def_rtl, pwr=SysConfig.def_pwr):
        super(CommonMechine, self).__init__()
        self.__topName = top
        self.__gds = gds
        self.__sch = sch
        self.__rtl = rtl

    def getDrc(self):
        return 'drc -top_cell {0} -gds {1} -deck {2}'.format(self.getTopCellName(), self.getGds(), self.getSch())

    def getLvs(self):
        return 'lvs -top dtmf -gds ./dtmf.gds -sch ./dtmf.sch -deck ./tapeout.lvs'

    # top cell name
    def setTopCellName(self, topName):
        self.__topName = topName

    def getTopCellName(self):
        return self.__topName

    #     GDS:  /home/design/top.gds
    def setGds(self, gds):
        self.__gds = gds

    def getGds(self):
        return self.__gds

    # Schematic Netlist: /home/design/top.sch
    def setSch(self, sch):
        self.__sch = sch

    def getSch(self):
        return self.__sch

    # DEF: /home/design/top.def
    def setDef(self, defi):
        self.__defi = defi

    def getDef(self):
        return self.__defi

    # RTL verilog: /home/design/top.v
    def setRtl(self, rtl):
        self.__rtl = rtl

    def getRtl(self):
        return self.__rtl

    # Power value: 5 (volt.)
    def setPwr(self, pwr):
        self.__pwr = pwr

    def getPwr(self):
        return self.__pwr

if __name__ == '__main__':
    print SysConfig.def_gds
    c = CommonMechine()
    print c.getDrc()
    c.setTopCellName("top")
    print c.getTopCellName()
    # c.setGds()
    # print c.getGds()
