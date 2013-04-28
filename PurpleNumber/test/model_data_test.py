# coding=utf-8
"""Unit test for model_data.py."""
import inspect
import itertools
import sys
import unittest
from protorpc import messages
from model import *  # Import all classes from model to ensure coverage.
from model_data import ALPHA_STARS
from model_data import BETA_STARS
from model_data import BRIGHTNESS
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
        for enum_value in itertools.chain(*enum_classes):
            self.assertTrue(enum_value in CHINESE,
                            "%s missing in CHINESE" % enum_value)

class TestBrightness(unittest.TestCase):
    """Test the brightness matrix."""
    def test_coverge(self):
        for di_zhi in DiZhi:
            self.assertTrue(di_zhi in BRIGHTNESS,
                           "DiZhi.%s is not in BRIGHTNESS" % di_zhi)
        for di_zhi, brightness_column in BRIGHTNESS.iteritems():
            stars = set(itertools.chain(*(brightness_column.values())))
            self.assertEquals(20,
                              len(stars),
                              ("Brightness recorded for %d stars with DiZhi.%s"
                               % (len(stars), di_zhi)))
    def test_uniqueness(self):
        for di_zhi, brightness_column in BRIGHTNESS.iteritems():
            stars = tuple(itertools.chain(*(brightness_column.values())))
            self.assertTrue(len(set(stars)) == len(stars),
                            "Some star is repeated: %s" % str(stars))


class TestPrint(unittest.TestCase):
    """Test the printing functions."""
    def test_print_board(self):
        print_board(SAMPLE)
    def test_print_person(self):
        print_person(SAMPLE_PERSON)
