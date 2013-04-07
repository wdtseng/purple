# coding=utf-8
"""Unit test for gen-board.py.

@author: Dustin Tseng
"""
import unittest
import itertools
import gen_board
from model import *

class TestGenBoard(unittest.TestCase):
    """Test the board generation function"""
    def test_generate_board(self):
        board = gen_board.generate_board(SAMPLE_PERSON)
        for dizhi in DiZhi:
            self.assertEqual(SAMPLE.grids[dizhi.number].tian_gan, board.grids[dizhi.number].tian_gan)
            self.assertEqual(SAMPLE.grids[dizhi.number].di_zhi, board.grids[dizhi.number].di_zhi)
            self.assertEqual(SAMPLE.grids[dizhi.number].palace, board.grids[dizhi.number].palace)
