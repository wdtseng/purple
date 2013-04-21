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
    ZUO_FU = 101
    YOU_BI = 102
    WEN_QU = 103
    WEN_CHANG = 104
    LU_CUN = 105
    QING_YANG = 106
    TUO_LUO = 107
    TIAN_KUI = 108
    TIAN_RONG = 109
    MING_MA = 110
    YUE_MA = 111
    XI_SHEN = 112
    HUA_GAI = 113
    HONG_LUAN = 114
    TIAN_XI = 115
    GU_CHEN = 116
    GUA_SU = 117
    TIAN_KU = 118
    TIAN_XU = 119
    TIAN_KONG = 120
    TIAN_XING = 121
    TIAN_YAO = 122
    YIN_SHA = 123
    DI_KONG = 124
    DI_JIE = 125
    HUO_XING = 126
    LING_XING = 127

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
    """Enum for board classifications."""
    SI_TAO_HUA = 0
    SI_KU = 1
    SI_MA = 2

class SiHua(messages.Enum):
    HUA_LU = 0
    HUA_QUAN = 1
    HUA_KE = 2
    HUA_JI = 3

class Brightness(messages.Enum):
    """Enum for brightness of a star."""
    XIAN = 0  # 陷
    PING = 1  # 平
    WANG = 2  # 旺
    MIAO = 3  # 廟

class Star(messages.Message):
    """ Structure of a 星 """
    type = messages.EnumField(StarType, 1)
    brightness = messages.EnumField(Brightness, 2)
    si_hua = messages.EnumField(SiHua, 3)
    element = messages.EnumField(Element, 4, repeated=True)
    element_tachi = messages.EnumField(Taichi, 5, repeated=True)

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

class StaticProperty(messages.Message):
    """Message that stores static properties for like 天干, 地支, 陰陽, 五行.

    StaticProperty can be associated with  
    """
    taichi = messages.EnumField(Taichi, 1)
    element = messages.EnumField(Element, 2)
    chinese = messages.StringField(3)

