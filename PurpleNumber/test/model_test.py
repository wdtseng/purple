# coding=utf-8
"""Unit test for model.py.

@author: Dustin Tseng
"""
import unittest
import itertools
from model import TianGan
from model import DiZhi
from model import StarType
from model import Element
from model import Palace
from model import Grid
from model import Board
from model import CHINESE
from model import SAMPLE
from model import print_board
from model import get_rank

class TestModel(unittest.TestCase):
    """Test the CHINESE dictionary defined in model."""
    def test_example(self):
        self.assertEqual(u"甲", CHINESE[TianGan.JIA])
        self.assertEqual(u"子", CHINESE[DiZhi.ZI])
    def test_coverage(self):
        for tian_gan in itertools.chain(TianGan,
                                        DiZhi,
                                        Element,
                                        Palace,
                                        StarType):
            self.assertTrue(tian_gan in CHINESE)
    def test_print(self):
        print_board(SAMPLE)
        
class TestUtilityFunctions(unittest.TestCase):
    """ Test the utility function in model """
    
    def test_get_rank(self):
        alpha = [StarType.ZI_WEI,
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
        beta = [StarType.LU_CUN,
                StarType.WEN_QU,
                StarType.HUO_XING,
                StarType.WEN_CHANG]
        for type in alpha:
            self.assertEqual(0, get_rank(type))
        for type in beta:
            self.assertEqual(1, get_rank(type))
