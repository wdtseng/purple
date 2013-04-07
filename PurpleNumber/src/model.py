# coding=utf-8
"""protorpc enum and message definitions of 紫微斗數 命盤.

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
    LIAN_ZHEN = 5
    TIAN_FU = 6
    TAI_YIN = 7
    TAN_LANG = 8
    JU_MEN = 9
    TIAN_XIANG = 10
    TIAN_LIANG = 11
    QI_SHA = 12
    PO_JUN = 13

class Palace(messages.Enum):
    """Enum for 宮位 constants."""
    MING_GONG = 0
    FU_MU = 1
    FU_DE = 2
    TIAN_ZHAI = 3
    GUAN_LU = 4
    JIAO_YOU = 5
    QIAN_YI = 6
    JI_E = 7
    CAI_BO = 8
    ZI_NV = 9
    FU_QI = 10
    XIONG_DI = 11

class Element(messages.Enum):
    """Enum for 五行 constants."""
    MU = 0
    HUO = 1
    TU = 2
    JIN = 3
    SHUI = 4

class Sex(messages.Enum):
    """Enum for sex."""
    MALE = 0
    FEMALE = 1

class Taichi(messages.Enum):
    """Enum for 五行 constants."""
    YIN = 0
    YANG = 1

class Grid(messages.Message):
    """Structure of a single 宮位.

    A Grid consists of TianGan, DiZhi, Palace, and a list of AlphaStars. It may
    also optionally be the body palace."""
    tian_gan = messages.EnumField(TianGan, 1)
    di_zhi = messages.EnumField(DiZhi, 2)
    palace = messages.EnumField(Palace, 3)
    alpha_stars = messages.EnumField(AlphaStar, 4, repeated=True)
    is_body_palace = messages.BooleanField(5, default=False)

class Person(messages.Message):
    """Personal information.

    Includes metadata such as name, sex, and birthday (solar and lunar).
    """
    name = messages.StringField(1)
    sex = messages.EnumField(Sex, 2)
    taichi = messages.EnumField(Taichi, 3)

    # Solar birthday.
    year = messages.IntegerField(10)  # E.g., 1949.
    month_of_year = messages.IntegerField(11)  # 1 - 12.
    day_of_month = messages.IntegerField(12)  # 1 - 31.

    # Lunar birthday.
    year_tian_gan = messages.EnumField(TianGan, 20)
    year_di_zhi = messages.EnumField(DiZhi, 21)
    lunar_month_of_year = messages.IntegerField(22) # 1 - 12.
    lunar_day_of_month = messages.IntegerField(23) # 1 - 30.
    time_di_zhi = messages.EnumField(DiZhi, 24)

class Board(messages.Message):
    """Structure of a 命盤.

    A Board consists of a Person and twelve Grids. It also contains metadata
    that can be derived from the Grids such as the destiny AlphaStar (命主), the
    body AlphaStar (身主), the element of the board, etc."""
    # Exactly 12 grids, start with the grid with TianGan.JIA and DiZhi.ZI.
    grids = messages.MessageField(Grid, 1, repeated=True)
    person = messages.MessageField(Person, 2)

    # Meta information about the board.
    destiny_star = messages.EnumField(AlphaStar, 10)
    body_star = messages.EnumField(AlphaStar, 11)
    element = messages.EnumField(Element, 12)

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

    Element.MU: u"木",
    Element.HUO: u"火",
    Element.TU: u"土",
    Element.JIN: u"金",
    Element.SHUI: u"水",

    AlphaStar.ZI_WEI: u"紫微",
    AlphaStar.TIAN_JI: u"天機",
    AlphaStar.TAI_YANG: u"太陽",
    AlphaStar.WU_QU: u"武曲",
    AlphaStar.TIAN_TONG: u"天同",
    AlphaStar.LIAN_ZHEN: u"廉貞",
    AlphaStar.TIAN_FU: u"天府",
    AlphaStar.TAI_YIN: u"太陰",
    AlphaStar.TAN_LANG: u"貪狼",
    AlphaStar.JU_MEN: u"巨門",
    AlphaStar.TIAN_XIANG: u"天相",
    AlphaStar.TIAN_LIANG: u"天梁",
    AlphaStar.QI_SHA: u"七殺",
    AlphaStar.PO_JUN: u"破軍",

    Sex.MALE: u"男",
    Sex.FEMALE: u"女",

    Taichi.YIN: u"陰",
    Taichi.YANG: u"陽",
}

def print_person(person):
    """Print the contents of a given Person.

    Args:
        person, a Person.
    """
    assert isinstance(person, Person)
    print u"Name: %s" % person.name
    print u"Sex: %s" % CHINESE[person.sex]
    print u"陽曆%4d年%2d月%2d日生" % (person.year, person.month_of_year,
                                     person.day_of_month)
    print u"陰曆%s%s年%2d月%2d日%s時生" % (CHINESE[person.year_tian_gan],
                                          CHINESE[person.year_di_zhi],
                                          person.lunar_month_of_year,
                                          person.lunar_day_of_month,
                                          CHINESE[person.time_di_zhi])
def print_grid(grid):
    """Print the contents of a given Grid.

    Args:
        grid, a Grid.
    """
    assert isinstance(grid, Grid)
    print u"%s%s %s%s, [%s]" % (
        CHINESE[grid.tian_gan],
        CHINESE[grid.di_zhi],
        CHINESE[grid.palace],
        u"(身)" if grid.is_body_palace else u"",
        u",".join([CHINESE[star] for star in grid.alpha_stars]),
    )

def print_board(board):
    """Print the contents of a given Board.

    Args:
        board, a Board.
    """
    assert isinstance(board, Board)
    print_person(board.person)
    for grid in board.grids:
        print_grid(grid)

GRIDS = [
    Grid(
        tian_gan=TianGan.JIA,
        di_zhi=DiZhi.ZI,
        palace=Palace.CAI_BO,
        alpha_stars=[AlphaStar.TIAN_JI],
    ),
    Grid(
        tian_gan=TianGan.YI,
        di_zhi=DiZhi.CHOU,
        palace=Palace.ZI_NV,
        alpha_stars=[AlphaStar.ZI_WEI, AlphaStar.PO_JUN],
    ),
    Grid(
        tian_gan=TianGan.JIA,
        di_zhi=DiZhi.YIN,
        palace=Palace.FU_QI,
        alpha_stars=[],
    ),
    Grid(
        tian_gan=TianGan.YI,
        di_zhi=DiZhi.MAO,
        palace=Palace.XIONG_DI,
        alpha_stars=[AlphaStar.TIAN_FU],
    ),
    Grid(
        tian_gan=TianGan.BING,
        di_zhi=DiZhi.CHEN,
        palace=Palace.MING_GONG,
        alpha_stars=[AlphaStar.TAI_YIN],
    ),
    Grid(
        tian_gan=TianGan.DING,
        di_zhi=DiZhi.SI,
        palace=Palace.FU_MU,
        alpha_stars=[AlphaStar.LIAN_ZHEN, AlphaStar.TAN_LANG],
    ),
    Grid(
        tian_gan=TianGan.WU,
        di_zhi=DiZhi.WU,
        palace=Palace.FU_DE,
        alpha_stars=[AlphaStar.JU_MEN],
    ),
    Grid(
        tian_gan=TianGan.JI,
        di_zhi=DiZhi.WEI,
        palace=Palace.TIAN_ZHAI,
        alpha_stars=[AlphaStar.TIAN_XIANG],
    ),
    Grid(
        tian_gan=TianGan.GENG,
        di_zhi=DiZhi.SHEN,
        palace=Palace.GUAN_LU,
        alpha_stars=[AlphaStar.TIAN_TONG, AlphaStar.TIAN_LIANG],
    ),
    Grid(
        tian_gan=TianGan.XIN,
        di_zhi=DiZhi.YOU,
        palace=Palace.JIAO_YOU,
        alpha_stars=[AlphaStar.WU_QU, AlphaStar.QI_SHA],
    ),
    Grid(
        tian_gan=TianGan.REN,
        di_zhi=DiZhi.XU,
        palace=Palace.QIAN_YI,
        alpha_stars=[AlphaStar.TAI_YANG],
        is_body_palace=True,
    ),
    Grid(
        tian_gan=TianGan.KUI,
        di_zhi=DiZhi.HAI,
        palace=Palace.JI_E,
        alpha_stars=[],
    ),
]

SAMPLE_PERSON = Person(
    name=u"戴吟珍",
    sex=Sex.FEMALE,
    year=1964,
    month_of_year=1,
    day_of_month=18,
    year_tian_gan=TianGan.KUI,
    year_di_zhi=DiZhi.MAO,
    lunar_month_of_year=12,
    lunar_day_of_month=4,
    time_di_zhi=DiZhi.YOU,
)

SAMPLE = Board(
    person=SAMPLE_PERSON,
    grids=GRIDS,
)

