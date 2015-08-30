#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sysConfig import SysConfig


class CommonMechine(object):

    """docstring for CommonMechine
    """

    def __init__(self, dicConfig):
        super(CommonMechine, self).__init__()
        self.__topName = SysConfig.def_topcell_name
        self.__gds = SysConfig.def_gds
        self.__sch = SysConfig.def_sch
        self.__defi = SysConfig.def_def
        self.__rtl = SysConfig.def_rtl
        self.__pwr = SysConfig.def_pwr

        # datas
        self.__lef = dicConfig['lef']
        self.__lib = dicConfig['lib']
        self.__sdc = dicConfig['sdc']
        self.__drc = dicConfig['drc']
        self.__lvs = dicConfig['lvs']
        self.__synthesis = dicConfig['synthesis']

    # get file datas
    def getlef(self):
        return self.__lef

    def getlib(self):
        return self.__lib

    def getsdc(self):
        return self.__sdc

    def getdrc(self):
        return self.__drc

    def getlvs(self):
        return self.__lvs

    def getsysnthesis(self):
        return self.__sysnthesis

    # Your design data are listed below
    # top cell name
    def settop(self, topName):
        self.__topName = topName

    def gettop(self):
        return self.__topName

    #     GDS:  /home/design/top.gds
    def setgds(self, gds):
        self.__gds = gds

    def getgds(self):
        return self.__gds

    # Schematic Netlist: /home/design/top.sch
    def setsch(self, sch):
        self.__sch = sch

    def getsch(self):
        return self.__sch

    # DEF: /home/design/top.def
    def setdef(self, defi):
        self.__defi = defi

    def getdef(self):
        return self.__defi

    # RTL verilog: /home/design/top.v
    def setrtl(self, rtl):
        self.__rtl = rtl

    def getrtl(self):
        return self.__rtl

    # Power value: 5 (volt.)
    def setpwr(self, pwr):
        self.__pwr = pwr

    def getpwr(self):
        return self.__pwr



