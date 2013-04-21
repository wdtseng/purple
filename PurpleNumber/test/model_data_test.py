# coding=utf-8
"""Unit test for model_data.py."""
import inspect
import itertools
import sys
import unittest
from protorpc import messages
from model import * # All classes must be imported to ensure coverage.
from model_data import ALPHA_STARS
from model_data import BETA_STARS
from model_data import CHINESE
from model_data import SAMPLE
from model_data import SAMPLE_PERSON
from model_data import print_board
from model_data import print_person

class TestStarClassification(unittest.TestCase):
    """Test star rank classification."""
    def test_rank_coverage(self):
        for star_type in StarType:
            self.assertTrue(star_type in ALPHA_STARS
                            or star_type in BETA_STARS)


class TestChinese(unittest.TestCase):
    """Test the Chinese dictionary."""
    def test_example(self):
        self.assertEqual(u"甲", CHINESE[TianGan.JIA])
        self.assertEqual(u"子", CHINESE[DiZhi.ZI])
    def test_coverage(self):
        clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
        enum_classes = [clsmember[1] for clsmember in clsmembers if (
            issubclass(clsmember[1], messages.Enum)
            and clsmember[1].__module__ == "model"
        )]
        print enum_classes
        print TianGan
        for enum_value in TianGan:
            self.assertTrue(enum_value in CHINESE,
                            "%s missing in CHINESE" % enum_value)
        for enum_value in enum_classes[0]:
            self.assertTrue(enum_value in CHINESE,
                            "%s missing in CHINESE" % enum_value)
        for enum_value in itertools.chain(*enum_classes):
            self.assertTrue(enum_value in CHINESE,
                            "%s missing in CHINESE" % enum_value)

class TestPrint(unittest.TestCase):
    """Test the printing functions."""
    def test_print_board(self):
        print_board(SAMPLE)
    def test_print_person(self):
        print_person(SAMPLE_PERSON)
