# coding=utf-8
"""Unit test for model.py.

@author: Dustin Tseng
"""
import unittest
from model import TianGan
from model import DiZhi
from model import Palace
from model import Grid
from model import Board
from model import CHINESE

class TestChinese(unittest.TestCase):
    def test_chinese(self):
        self.assertEqual(u"甲", CHINESE[TianGan.JIA])
        self.assertEqual(u"子", CHINESE[DiZhi.ZI])

