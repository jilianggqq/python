#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Qiqiang Guan'


class SysConfig(object):

    """this is the configuration of all the Foundry companies"""
    # following technology data from Foundry companies, they are located at the specified paths
    tcmc45_6 = {"lef": "/A/B/C/tsmc/45nm/6ml/physical/tech.lef /A/B/C/tsmc/45nm/6ml/physical/macro.lef",
                "lib": "/D/E/F/tsmc/45nm/6ml/fast/corner.lib /D/E/F/tsmc/45nm/6ml/fast/stdcell.lib /D/E/F/tsmc/45nm/6ml/fast/io.lib",
                "sdc": "/D/E/F/tsmc/45nm/6ml/fast/timing/tapeout.sdc",
                "drc": "/A/B/C/tsmc/45nm/6ml/drc/tapeout.drc",
                "lvs": "/A/B/C/tsmc/45nm/6ml/lvs/tapeout.lvs",
                "synthesis": "/B/G/H/tsmc/6ml/45nm/syn.teh"}

    tcmc45_7 = {"lef": "/A/B/C/tsmc/45nm/7ml/physical/tech.lef /A/B/C/tsmc/45nm/7ml/physical/macro.lef",
                "lib": "/D/E/F/tsmc/45nm/7ml/fast/corner.lib /D/E/F/tsmc/45nm/7ml/fast/stdcell.lib /D/E/F/tsmc/45nm/7ml/fast/io.lib",
                "sdc": "/D/E/F/tsmc/45nm/7ml/fast/timing/tapeout.sdc",
                "drc": "/A/B/C/tsmc/45nm/7ml/drc/tapeout.drc",
                "lvs": "/A/B/C/tsmc/45nm/7ml/lvs/tapeout.lvs",
                "synthesis": "/B/G/H/tsmc/7ml/45nm/syn.teh"}

    tcmc65_6 = {"lef": "/A/B/C/tsmc/65nm/physical/tech.lef /A/B/C/tsmc/65nm/physical/macro.lef",
                "lib": "/D/E/F/tsmc/65nm/fast/corner.lib /D/E/F/tsmc/65nm/fast/stdcell.lib /D/E/F/tsmc/65nm/fast/io.lib",
                "sdc": "/D/E/F/tsmc/65nm/fast/timing/tapeout.sdc",
                "drc": "/A/B/C/tsmc/65nm/drc/tapeout.drc",
                "lvs": "/A/B/C/tsmc/65nm/lvs/tapeout.lvs",
                "synthesis": "/B/G/H/tsmc/65nm/syn.teh"}

    umc45_6 = {"lef": "/A/B/C/umc/45nm/physical/tech.lef /A/B/C/umc/45nm/physical/macro.lef",
               "lib": "/D/E/F/umc/45nm/fast/corner.lib /D/E/F/umc/45nm/fast/stdcell.lib /D/E/F/umc/45nm/fast/io.lib",
               "sdc": "/D/E/F/umc/45nm/fast/timing/tapeout.sdc",
               "drc": "/A/B/C/umc/45nm/drc/tapeout.drc",
               "lvs": "/A/B/C/umc/45nm/lvs/tapeout.lvs",
               "synthesis": "/B/G/H/umc/45nm/syn.tec"}

    # my default design data 
    def_topcell_name = 'TOP'
    def_gds = '/home/design/top.gds'
    def_sch = '/home/design/top.sch'
    def_def = '/home/design/top.def'
    def_rdl = '/home/design/top.v'
    def_pwr = '5 (volt.)'

if __name__ == '__main__':
    print '** test **'
    print SysConfig.def_pwr
    print SysConfig.def_def
    print SysConfig.def_gds
    print SysConfig.tcmc65_6['lef']
    print SysConfig.umc45_6['synthesis']
