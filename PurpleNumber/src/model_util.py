'''
Created on Apr 14, 2013

Contains utility function on the data model

@author: Robert Tseng
'''

from model import *
from model_data import ALPHA_STARS
from model_data import BETA_STARS
from model_data import BRIGHTNESS

def find_star_in_grid(grid, star_type):
    assert isinstance(grid, Grid)
    assert isinstance(star_type, StarType)

    for star in grid.stars:
        if star.type == star_type:
            return star
    return None

def star_rank(star_type):
    assert isinstance(star_type, StarType)
    if star_type in ALPHA_STARS:
        return 0
    elif star_type in BETA_STARS:
        return 1
    else:
        return 2

def star_brightness(star_type, di_zhi):
    assert isinstance(star_type, StarType)
    assert isinstance(di_zhi, DiZhi)
    for brightness in Brightness:
        if star_type in BRIGHTNESS[di_zhi][brightness]:
            return brightness
    return None

def has_star_of_rank(grid, rank):
    assert isinstance(grid, Grid)
    assert isinstance(rank, int)
    assert 0 <= rank and rank <= 2
    return any(get_rank(star.type) == rank for star in grid.stars)
