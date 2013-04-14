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
from model import ALPHA_STARS
from model import BETA_STARS

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
    
    def test_rank_coverage(self):
        for star_type in StarType:
            self.assertTrue(star_type in ALPHA_STARS or star_type in BETA_STARS)
