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
            self.assertEqual(SAMPLE.grids[dizhi.number].is_body_palace, board.grids[dizhi.number].is_body_palace)

        self.assertEqual(SAMPLE.element, board.element)
        self.assertEqual(SAMPLE.element_number, board.element_number)
        self.assertEqual(SAMPLE.person_taichi, board.person_taichi)
        self.assertEqual(SAMPLE.board_taichi, board.board_taichi)
        self.assertEqual(SAMPLE.classification, board.classification)
        self.assertEqual(SAMPLE.destiny_star, board.destiny_star)
        self.assertEqual(SAMPLE.body_star, board.body_star)
