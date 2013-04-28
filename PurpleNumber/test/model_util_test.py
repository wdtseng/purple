'''
Created on Apr 14, 2013

@author: mac
'''
import unittest
import model
import model_data
import model_util

class TestUtilityFunctions(unittest.TestCase):
    """ Test the utility function in model_util """
    def test_star_rank_coverage(self):
        for star_type in model.StarType:
            rank = model_util.star_rank(star_type)
            self.assertTrue(0 <= rank and rank <= 2)
    def test_star_brightness(self):
        for di_zhi in model.DiZhi:
            for brightness in model.Brightness:
                for star_type in model_data.BRIGHTNESS[di_zhi][brightness]:
                    self.assertEquals(brightness,
                                      model_util.star_brightness(star_type,
                                                                 di_zhi))
