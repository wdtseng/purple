# coding=utf-8
"""Unit test for enums.py.

@author: Dustin Tseng
"""
import unittest
from core.enums import TianGanUtil
from core.enums import TianGan

class TestTianGanUtil(unittest.TestCase):
    def test_chinese(self):
        self.assertEqual("甲", TianGanUtil.chinese(0))
        self.assertEqual("甲", TianGanUtil.chinese("JIA"))
        self.assertEqual("甲", TianGanUtil.chinese(TianGan.JIA))
        self.assertEqual("丁", TianGanUtil.chinese(3))
        self.assertEqual("丁", TianGanUtil.chinese("DING"))
        self.assertEqual("丁", TianGanUtil.chinese(TianGan.DING))

if __name__ == '__main__':
    unittest.main()

