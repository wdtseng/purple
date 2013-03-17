# coding=utf-8
'''
Created on Mar 15, 2013

A grid is the abstraction of a "square" in the board, counting:
1. A list of stars
2. The TianGan
3. The type of palace it is

@author: Robert Tseng
'''
from core.constants import TianGanEnumValue
from core.star import Star

class Grid(object):
    def __init__(self, palace):
        self._palace = palace
        self._stars = []

    '''
    Properties getter/setter
    '''
    @property
    def tian_gan(self):
        return self._tian_gan
    @tian_gan.setter
    def tian_gan(self, tian_gan):
        assert isinstance(tian_gan, TianGanEnumValue)
        self._tian_gan = tian_gan

    @property
    def palace(self):
        return self._palace

    @property
    def stars(self):
        return tuple(self._stars)

    '''
    Star manipulation methods
    '''
    def add_star(self, star):
        assert isinstance(star, Star)

        #no_op if the star is already in the list
        if self._stars.count(star) == 0:
            self._stars.append(star)
    
    def remove_star(self, star):
        assert isinstance(star, Star)
        if self._stars.count(star) > 0:
            self._stars.remove(star)
    
    def contain_star(self, star):
        assert isinstance(star, Star)
        return self._stars.count(star) > 0
