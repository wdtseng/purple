# coding=utf-8
"""Unit test for model.py.

@author: Dustin Tseng
"""
import unittest
from helloworld import num_to_chinese
from helloworld import board_context
from model_data import SAMPLE

class TestHelloworld(unittest.TestCase):
    """Test helper functions currently residing in helloworld.py."""
    def test_num_to_chinese(self):
        self.assertEqual(u"零", num_to_chinese(0))
        self.assertEqual(u"一", num_to_chinese(1))
        self.assertEqual(u"十九", num_to_chinese(19))
        self.assertEqual(u"一九八四", num_to_chinese(1984))
        self.assertEqual(u"　零", num_to_chinese(0, 2))
        self.assertEqual(u"　一", num_to_chinese(1, 2))
        self.assertEqual(u"十九", num_to_chinese(19, 2))
        self.assertEqual(u"一九八四", num_to_chinese(1984, 2))
        self.assertEqual(u"　　　零", num_to_chinese(0, 4))
        self.assertEqual(u"　　　一", num_to_chinese(1, 4))
        self.assertEqual(u"　　十九", num_to_chinese(19, 4))
        self.assertEqual(u"一九八四", num_to_chinese(1984, 4))
    def test_board_context(self):
        context = board_context(SAMPLE)
        self.assertTrue("solar_birthday" in context)
        self.assertTrue("lunar_birthday" in context)
        self.assertTrue("birthday" in context)
        self.assertEqual(u"陽曆一九六四　　一　十八", context["solar_birthday"])
        self.assertEqual(u"　　　　　　年　　月　　日酉時生", context["birthday"])
        self.assertEqual(u"陰曆　癸卯　　十二　　四", context["lunar_birthday"])
