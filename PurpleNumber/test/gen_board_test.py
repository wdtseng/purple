# coding=utf-8
"""Unit test for gen-board.py.

@author: Dustin Tseng
"""
import unittest
import itertools
import gen_board
from model_data import SAMPLE_PERSON
from model_data import SAMPLE

class TestGenBoard(unittest.TestCase):
    """Test the board generation function"""
    def test_generate_board(self):
        board = gen_board.generate_board(SAMPLE_PERSON)
        self.assertEqual(SAMPLE, board)
