'''
Created on Apr 14, 2013

Contains utility function on the data model

@author: Robert Tseng
'''

from model import *

def find_star_in_grid(grid, star_type):
    assert isinstance(grid, Grid)
    assert isinstance(star_type, StarType)

    for star in grid.stars:
        if star.type == star_type:
            return star
    return None

def get_rank(star_type):
    assert isinstance(star_type, StarType)
    if star_type in ALPHA_STARS:
        return 0
    elif star_type in BETA_STARS:
        return 1
    else:
        return 2
