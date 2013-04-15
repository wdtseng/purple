'''
Created on Apr 14, 2013

@author: mac
'''
import unittest
from model_util import *
from model import *

class TestUtilityFunctions(unittest.TestCase):
    """ Test the utility function in model_util """

    def test_rank_coverage(self):
        for star_type in StarType:
            self.assertTrue(star_type in ALPHA_STARS or star_type in BETA_STARS)
