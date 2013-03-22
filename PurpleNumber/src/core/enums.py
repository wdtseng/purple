# coding=utf-8
"""protorpc enum definitions for various Chinese constants.

@author: Dustin Tseng
"""
from protorpc import messages

class TianGan(messages.Enum):
    """Enum for 天干 constants."""
    JIA = 0;
    YI = 1;
    BING = 2;
    DING = 3;
    WU = 4;
    JI = 5;
    GENG = 6;
    XIN = 7;
    REN = 8;
    KUI = 9;

class TianGanUtil():
    """Utility for 天干 constants."""
    __chinese = ("甲",
                 "乙",
                 "丙",
                 "丁",
                 "戊",
                 "己",
                 "庚",
                 "辛",
                 "壬",
                 "癸",
                )
    @staticmethod
    def chinese(tian_gan):
        return TianGanUtil.__chinese[TianGan(tian_gan).number]
