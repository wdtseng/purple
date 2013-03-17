# coding=utf-8
"""
Created on Mar 15, 2013

Constants needed for the purple board

@author: Robert Tseng
"""

import core.enum;

class TianGanEnumValue(core.enum.ChineseEnumValue):
    pass

TianGan = core.enum.CreateEnum(tuple(
    [TianGanEnumValue(name, chinese)
     for name, chinese in
         [("JIA", "甲"),
          ("YI", "乙"),
          ("BING", "丙"),
          ("DING", "丁"),
          ("WU", "戊"),
          ("JI", "己"),
          ("GENG", "庚"),
          ("XIN", "辛"),
          ("REN", "壬"),
          ("KUI", "癸"),
         ]]))

class DiZhiEnumValue(core.enum.ChineseEnumValue):
    pass

DiZhi = core.enum.CreateEnum(tuple(
    [DiZhiEnumValue(name, chinese)
     for name, chinese in
     [("ZI", "子"),
      ("CHOU", "丑"),
      ("YIN", "寅"),
      ("MAO", "卯"),
      ("CHEN", "辰"),
      ("SI", "巳"),
      ("WU", "午"),
      ("WEI", "未"),
      ("SHEN", "申"),
      ("YOU", "酉"),
      ("XU", "戌"),
      ("HAI", "亥"),
      ]]))

class PalaceEnumValue(core.enum.ChineseEnumValue):
    pass

Palace = core.enum.CreateEnum(tuple(
    [PalaceEnumValue(name, chinese)
     for name, chinese in
     [("MING", "命"),
      ("FUMU", "父母"),
      ("FUDE", "福德"),
      ("ZINV", "子女"),
      ("GUANLU", "官祿"),
      ("PENGYOU", "朋友"),
      ("QIANYI", "遷移"),
      ("JIE", "疾惡"),
      ("CAIBO", "財帛"),
      ("TIANZHAI", "田宅"),
      ("FUQI", "夫妻"),
      ("XIONGDI", "兄弟"),
      ]]))
