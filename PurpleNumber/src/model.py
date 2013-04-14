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

class StarType(messages.Enum):
    """Enum for 主星 constants."""
    # Alpha stars
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
    # ALPHA_STAR_END = 100 defined below.
    
    # Beta stars
    LU_CUN = 101
    WEN_QU = 102
    HUO_XING = 103
    WEN_CHANG = 104

ALPHA_STARS = [StarType.ZI_WEI,
               StarType.TIAN_JI,
               StarType.TAI_YANG,
               StarType.WU_QU,
               StarType.TIAN_TONG,
               StarType.LIAN_ZHEN,
               StarType.TIAN_FU,
               StarType.TAI_YIN,
               StarType.TAN_LANG,
               StarType.JU_MEN,
               StarType.TIAN_XIANG,
               StarType.TIAN_LIANG,
               StarType.QI_SHA,
               StarType.PO_JUN]

BETA_STARS = [StarType.LU_CUN,
              StarType.WEN_QU,
              StarType.HUO_XING,
              StarType.WEN_CHANG]

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
    YANG = 0
    YIN = 1

class BoardClassification(messages.Enum):
    """ Enum for board classifications. """
    SI_TAO_HUA = 0
    SI_KU = 1
    SI_MA = 2

class Star(messages.Message):
    """ Structure of a 星 """
    type = messages.EnumField(StarType, 1)
    strength = messages.IntegerField(2)  # -1 for 陷, 0 for 平, 1 for 旺
    si_hua = messages.IntegerField(3)  # bitmask for 祿權科忌
    element = messages.EnumField(Element, 4, repeated=True)
    element_tachi = messages.EnumField(Taichi, 5, repeated=True)

def get_rank(star_type):
    assert isinstance(star_type, StarType)
    if star_type in ALPHA_STARS:
        return 0
    elif star_type in BETA_STARS:
        return 1
    else:
        return 2

class Grid(messages.Message):
    """Structure of a single 宮位.

    A Grid consists of TianGan, DiZhi, Palace, and a list of Stars. It may
    also optionally be the body palace."""
    tian_gan = messages.EnumField(TianGan, 1)
    di_zhi = messages.EnumField(DiZhi, 2)
    palace = messages.EnumField(Palace, 3)
    stars = messages.MessageField(Star, 4, repeated=True)
    is_body_palace = messages.BooleanField(5, default=False)
    da_xian_start = messages.IntegerField(6)
    da_xian_end = messages.IntegerField(7)

class Person(messages.Message):
    """Personal information.

    Includes metadata such as name, sex, and birthday (solar and lunar).
    """
    name = messages.StringField(1)
    sex = messages.EnumField(Sex, 2)

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
    that can be derived from the Grids such as the destiny StarType (命主), the
    body StarType (身主), the element of the board, etc."""
    # Exactly 12 grids, start with the grid with TianGan.JIA and DiZhi.ZI.
    grids = messages.MessageField(Grid, 1, repeated=True)
    person = messages.MessageField(Person, 2)

    # Meta information about the board.
    destiny_star = messages.MessageField(Star, 10)
    body_star = messages.MessageField(Star, 11)
    board_taichi = messages.EnumField(Taichi, 12)  # 陽宮，陰宮
    person_taichi = messages.EnumField(Taichi, 13)
    element = messages.EnumField(Element, 14)  # 土二局
    element_number = messages.IntegerField(15)  # 水二，木三，金四，土五，火六
    classification = messages.EnumField(BoardClassification, 16)  # 四庫，四馬，四桃花

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

    StarType.ZI_WEI: u"紫微",
    StarType.TIAN_JI: u"天機",
    StarType.TAI_YANG: u"太陽",
    StarType.WU_QU: u"武曲",
    StarType.TIAN_TONG: u"天同",
    StarType.LIAN_ZHEN: u"廉貞",
    StarType.TIAN_FU: u"天府",
    StarType.TAI_YIN: u"太陰",
    StarType.TAN_LANG: u"貪狼",
    StarType.JU_MEN: u"巨門",
    StarType.TIAN_XIANG: u"天相",
    StarType.TIAN_LIANG: u"天梁",
    StarType.QI_SHA: u"七殺",
    StarType.PO_JUN: u"破軍",
    StarType.LU_CUN: u"祿存",
    StarType.WEN_QU: u"文曲",
    StarType.HUO_XING: u"火星",
    StarType.WEN_CHANG: u"文昌",

    Sex.MALE: u"男",
    Sex.FEMALE: u"女",

    Taichi.YIN: u"陰",
    Taichi.YANG: u"陽",

    BoardClassification.SI_KU: u"四庫",
    BoardClassification.SI_MA: u"四馬",
    BoardClassification.SI_TAO_HUA: u"四桃花",

    0: u"零",
    1: u"一",
    2: u"二",
    3: u"三",
    4: u"四",
    5: u"五",
    6: u"六",
    7: u"七",
    8: u"八",
    9: u"九",
    10: u"十",
    11: u"十一",
    12: u"十二",
    13: u"十三",
    14: u"十四",
    15: u"十五",
    16: u"十六",
    17: u"十七",
    18: u"十八",
    19: u"十九",
    20: u"二十",
    21: u"廿一",
    22: u"廿二",
    23: u"廿三",
    24: u"廿四",
    25: u"廿五",
    26: u"廿六",
    27: u"廿七",
    28: u"廿八",
    29: u"廿九",
    30: u"三十",
    31: u"卅一",
    32: u"卅二",
    33: u"卅三",
    34: u"卅四",
    35: u"卅五",
    36: u"卅六",
    37: u"卅七",
    38: u"卅八",
    39: u"卅九",
    40: u"四十",
    50: u"五十",
    60: u"六十",
    70: u"七十",
    80: u"八十",
    90: u"九十",

    " ": u"　",
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
        u",".join([CHINESE[star.type] for star in grid.stars]),
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
        # alpha_stars=[StarType.TIAN_JI],
        stars=[Star(type=StarType.TIAN_JI)],
        da_xian_start=85,
        da_xian_end=94,
    ),
    Grid(
        tian_gan=TianGan.YI,
        di_zhi=DiZhi.CHOU,
        palace=Palace.ZI_NV,
        # alpha_stars=[StarType.ZI_WEI, StarType.PO_JUN],
        stars=[Star(type=StarType.ZI_WEI),
               Star(type=StarType.PO_JUN)],
        da_xian_start=95,
        da_xian_end=104,
    ),
    Grid(
        tian_gan=TianGan.JIA,
        di_zhi=DiZhi.YIN,
        palace=Palace.FU_QI,
        # alpha_stars=[],
        stars=[],
        da_xian_start=105,
        da_xian_end=114,
    ),
    Grid(
        tian_gan=TianGan.YI,
        di_zhi=DiZhi.MAO,
        palace=Palace.XIONG_DI,
        # alpha_stars=[StarType.TIAN_FU],
        stars=[Star(type=StarType.TIAN_FU)],
        da_xian_start=115,
        da_xian_end=124,
    ),
    Grid(
        tian_gan=TianGan.BING,
        di_zhi=DiZhi.CHEN,
        palace=Palace.MING_GONG,
        # alpha_stars=[StarType.TAI_YIN],
        stars=[Star(type=StarType.TAI_YIN)],        
        da_xian_start=5,
        da_xian_end=14,
    ),
    Grid(
        tian_gan=TianGan.DING,
        di_zhi=DiZhi.SI,
        palace=Palace.FU_MU,
        # alpha_stars=[StarType.LIAN_ZHEN, StarType.TAN_LANG],
        stars=[Star(type=StarType.LIAN_ZHEN),
               Star(type=StarType.TAN_LANG)],        
        da_xian_start=15,
        da_xian_end=24,
    ),
    Grid(
        tian_gan=TianGan.WU,
        di_zhi=DiZhi.WU,
        palace=Palace.FU_DE,
        # alpha_stars=[StarType.JU_MEN],
        stars=[Star(type=StarType.JU_MEN)],
        da_xian_start=25,
        da_xian_end=34,
    ),
    Grid(
        tian_gan=TianGan.JI,
        di_zhi=DiZhi.WEI,
        palace=Palace.TIAN_ZHAI,
        # alpha_stars=[StarType.TIAN_XIANG],
        stars=[Star(type=StarType.TIAN_XIANG)],        
        da_xian_start=35,
        da_xian_end=44,
    ),
    Grid(
        tian_gan=TianGan.GENG,
        di_zhi=DiZhi.SHEN,
        palace=Palace.GUAN_LU,
        # alpha_stars=[StarType.TIAN_TONG, StarType.TIAN_LIANG],
        stars=[Star(type=StarType.TIAN_TONG), 
               Star(type=StarType.TIAN_LIANG)],        
        da_xian_start=45,
        da_xian_end=54,
    ),
    Grid(
        tian_gan=TianGan.XIN,
        di_zhi=DiZhi.YOU,
        palace=Palace.JIAO_YOU,
        # alpha_stars=[StarType.WU_QU, StarType.QI_SHA],
        stars=[Star(type=StarType.WU_QU),
               Star(type=StarType.QI_SHA)],     
        da_xian_start=55,
        da_xian_end=64,
    ),
    Grid(
        tian_gan=TianGan.REN,
        di_zhi=DiZhi.XU,
        palace=Palace.QIAN_YI,
        # alpha_stars=[StarType.TAI_YANG],
        stars=[Star(type=StarType.TAI_YANG)],        
        is_body_palace=True,
        da_xian_start=65,
        da_xian_end=74,
    ),
    Grid(
        tian_gan=TianGan.KUI,
        di_zhi=DiZhi.HAI,
        palace=Palace.JI_E,
        # alpha_stars=[],
        stars=[],
        da_xian_start=75,
        da_xian_end=84,
    ),
]

SAMPLE_PERSON = Person(
    # name=u"戴采和",
    name=u"蘇容容",
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
    destiny_star=Star(type=StarType.LIAN_ZHEN),
    body_star=Star(type=StarType.TIAN_TONG),
    board_taichi=Taichi.YANG,
    person_taichi=Taichi.YIN,
    element=Element.TU,
    element_number=5,
    classification=BoardClassification.SI_KU,
)

