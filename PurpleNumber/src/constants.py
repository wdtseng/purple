# coding=utf-8
"""
Created on Mar 15, 2013

tiangan and dizhi constants

@author: Robert Tseng
"""

import enum;

TianGan = enum.CreateEnum(tuple(
    [enum.ChineseEnumValue(name, chinese)
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

DiZhi = enum.CreateEnum(tuple(
    [enum.ChineseEnumValue(name, chinese)
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


if __name__ == "__main__":
    print "checking"
    print TianGan.JIA
    print TianGan[0]
    print TianGan.JIA.number
    print TianGan.JIA.name
    it = iter(TianGan)
    print it.next()
    print [value for value in list(iter(TianGan))]
    print [TianGan.JIA, TianGan.YI]
    print list(iter(DiZhi))
