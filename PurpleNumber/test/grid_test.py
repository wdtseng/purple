'''
Created on Mar 16, 2013

@author: Robert Tseng
'''

from core.constants import Palace, TianGan
from core.grid import Grid
from core.star import Star
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        self.grid = Grid(Palace.XIONGDI)
        self.grid.tian_gan = TianGan.JIA

    def tearDown(self):
        pass

    def testProperties(self):
        self.assertEqual(self.grid.tian_gan, TianGan.JIA, "TianGan mismatch")
        self.assertEqual(self.grid.palace, Palace.XIONGDI, "Palace mismatch")
        self.assertEqual(0, len(self.grid.stars), "List of stars should be initially empty")

    def testStarManipulation(self):
        star_one = Star("one")
        star_two = Star("two")

        # add one star
        self.grid.add_star(star_one)
        self.assertEqual(len(self.grid.stars), 1, "Number of star is incorrect after adding star_one")
        self.assertEqual(self.grid.stars[0], star_one, "List of star is incorrect after adding star_one")

        # adding the same star is a no_op
        self.grid.add_star(star_one)
        self.assertEqual(len(self.grid.stars), 1, "Adding the same star should be a no-op")
        self.assertEqual(self.grid.stars[0], star_one, "Adding the same star should be a no-op")

        # add a second star and verify both stars are in the list via the contain_star API
        self.grid.add_star(star_two)
        self.assertEqual(len(self.grid.stars), 2, "Number of star is incorrect after adding star_two")
        self.assertTrue(self.grid.contain_star(star_one), "Star_one should remain in the list")
        self.assertTrue(self.grid.contain_star(star_two), "Star_two should be added to the list")

        # remove the first star and verify that the correct star is removed
        self.grid.remove_star(star_one)
        self.assertEqual(len(self.grid.stars), 1, "Number of stars is incorrect after removing star_one")
        self.assertEqual(self.grid.stars[0], star_two, "List of star is incorrect after removing star_one")

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
