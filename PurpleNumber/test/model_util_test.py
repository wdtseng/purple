'''
Created on Apr 14, 2013

@author: mac
'''
import unittest
import model_util
from model import *

class TestUtilityFunctions(unittest.TestCase):
    """ Test the utility function in model_util """

    def test_rank_coverage(self):
        for star_type in StarType:
            rank = model_util.get_rank(star_type)
            self.assertTrue(0 <= rank and rank <= 2)
