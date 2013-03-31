# coding=utf-8
"""protorpc enum definitions for various Chinese constants.

@author: Dustin Tseng
"""
from protorpc import messages

class TianGan(messages.Enum):
    """Enum for 天干 constants."""
    JIA = 0
    YI = 1
    BING = 2
    DING = 3
    WU = 4
    JI = 5
    GENG = 6
    XIN = 7
    REN = 8
    KUI = 9

class DiZhi(messages.Enum):
    """Enum for 地支 constants."""
    ZI = 0
    CHOU = 1
    YIN = 2
    MAO = 3
    CHEN = 4
    SI = 5
    WU = 6
    WEI = 7
    SHEN = 8
    YOU = 9
    XU = 10
    HAI = 11

class AlphaStar(messages.Enum):
    """Enum for 主星 constants."""
    ZI_WEI = 0
    TIAN_JI = 1
    TAI_YANG = 2
    WU_QU = 3
    TIAN_TONG = 4
    LIAN_JEN = 5
    TIAN_FU = 6
    TAI_YIN = 7
    TANG_LANG = 8
    JU_MEN = 9
    TIAN_XIANG = 10
    TIAN_LIANG = 11
    QI_SHA = 12
    PUO_JUN = 13

class Palace(messages.Enum):
    """Enum for 宮位 constants."""
    MING_GONG = 0
    XIONG_DI = 1
    FU_QI = 2
    ZI_NV = 3
    CAI_BO = 4
    JI_E = 5
    QIAN_YI = 6
    JIAO_YOU = 7
    GUAN_LU = 8
    TIAN_ZHAI = 9
    FU_DE = 10
    FU_MU = 11

class Grid(messages.Message):
    """Structure of a single 宮位.

    A Grid consists of TianGan, DiZhi, Palace, and a list of AlphaStars. It may
    also optionally be the body palace."""
    tian_gan = messages.EnumField(TianGan, 1)
    di_zhi = messages.EnumField(DiZhi, 2)
    palace = messages.EnumField(Palace, 3)
    stars = messages.EnumField(AlphaStar, 4, repeated=True)
    is_body_palace = messages.BooleanField(5, default=False)

class Board(messages.Message):
    """Structure of a 命盤.

    A Board consists of twelve Grids, a destiny AlphaStar (命主), and a body
    AlphaStar (身主). It also contains metadata such as name, sex, birth date,
    and the lunar birth date."""
    # Exactly 12 grids, start with the grid with TianGan.JIA and DiZhi.ZI.
    grids = messages.MessageField(Grid, 1, repeated=True)
    destiny_star = messages.EnumField(AlphaStar, 2)
    body_star = messages.EnumField(AlphaStar, 3)
    name = messages.StringField(4)
    is_male = messages.BooleanField(5)
    year = messages.IntegerField(6)  # E.g., 1949.
    month_of_year = messages.IntegerField(7)  # 1 - 12.
    day_of_month = messages.IntegerField(8)  # 1 - 31.
    year_tian_gan = messages.EnumField(TianGan, 9)
    year_di_zhi = messages.EnumField(DiZhi, 10)
    lunar_month_of_year = messages.IntegerField(11) # 1 - 12.
    lunar_day_of_month = messages.IntegerField(12) # 1 - 30.
    time_di_zhi = messages.EnumField(DiZhi, 13)

def print_board(board):
    """Print the contents of a given Board.

    Args:
      board, a Board.
    """
    assert isinstance(board, Board)
    print u"Name: %s" % board.name
    print u"Sex: %s" % ("male" if board.is_male else "female")
    print u"陽曆%4d年%2d月%2d日生" % (board.year, board.month_of_year,
                                     board.day_of_month)
    print u"陰曆%s%s年%2d月%2d日%s時生" % (CHINESE[board.year_tian_gan],
                                          CHINESE[board.year_di_zhi],
                                          board.lunar_month_of_year,
                                          board.lunar_day_of_month,
                                          CHINESE[board.time_di_zhi])

CHINESE = {
    TianGan.JIA: u"甲",
    TianGan.YI: u"乙",
    TianGan.BING: u"丙",
    TianGan.DING: u"丁",
    TianGan.WU: u"戊",
    TianGan.JI: u"己",
    TianGan.GENG: u"庚",
    TianGan.XIN: u"辛",
    TianGan.REN: u"壬",
    TianGan.KUI: u"癸",

    DiZhi.ZI: u"子",
    DiZhi.CHOU: u"丑",
    DiZhi.YIN: u"寅",
    DiZhi.MAO: u"卯",
    DiZhi.CHEN: u"辰",
    DiZhi.SI: u"巳",
    DiZhi.WU: u"午",
    DiZhi.WEI: u"未",
    DiZhi.SHEN: u"申",
    DiZhi.YOU: u"酉",
    DiZhi.XU: u"戌",
    DiZhi.HAI: u"亥",

    Palace.MING_GONG: u"命宮",
    Palace.XIONG_DI: u"兄弟",
    Palace.FU_QI: u"夫妻",
    Palace.ZI_NV: u"子女",
    Palace.CAI_BO: u"財帛",
    Palace.JI_E: u"疾厄",
    Palace.QIAN_YI: u"遷移",
    Palace.JIAO_YOU: u"交友",
    Palace.GUAN_LU: u"官祿",
    Palace.TIAN_ZHAI: u"田宅",
    Palace.FU_DE: u"福德",
    Palace.FU_MU: u"父母",
}

SAMPLE = Board()
SAMPLE.name = u"戴吟珍"
SAMPLE.is_male = False
SAMPLE.year = 1964
SAMPLE.month_of_year = 1
SAMPLE.day_of_month = 18
SAMPLE.year_tian_gan = TianGan.KUI
SAMPLE.year_di_zhi = DiZhi.MAO
SAMPLE.lunar_month_of_year = 12
SAMPLE.lunar_day_of_month = 4
SAMPLE.time_di_zhi = DiZhi.YOU

print_board(SAMPLE)
