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

class DiZhi(messages.Enum):
    """Enum for 地支 constants."""
    ZI = 0;
    CHOU = 1;
    YIN = 2;
    MAO = 3;
    CHEN = 4;
    SI = 5;
    WU = 6;
    WEI = 7;
    SHEN = 8;
    YOU = 9;
    XU = 10;
    HAI = 11;

class AlphaStar(messages.Enum):
    """Enum for 主星 constants."""
    ZI_WEI = 0;
    TIAN_JI = 1;
    TAI_YANG = 2;
    WU_QU = 3;
    TIAN_TONG = 4;
    LIAN_JEN = 5;
    TIAN_FU = 6;
    TAI_YIN = 7;
    TANG_LANG = 8;
    JU_MEN = 9;
    TIAN_XIANG = 10;
    TIAN_LIANG = 11;
    QI_SHA = 12;
    PUO_JUN = 13;

class Palace(messages.Enum):
    """Enum for 宮位 constants."""
    MING_GONG = 0;
    XIONG_DI = 1;
    FU_QI = 2;
    ZI_NV = 3;
    CAI_BO = 4;
    JI_E = 5;
    QIAN_YI = 6;
    JIAO_YOU = 7;
    GUAN_LU = 8;
    TIAN_ZHAI = 9;
    FU_DE = 10;
    FU_MU = 11;
    

class Grid(messages.Enum):



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
