"""
Created on Mar 15, 2013

The star class

@author: Robert
"""

# total_ordering
class Star(object):
    """
    classdocs
    """

    def __init__(self, name):
        """
        Constructor
        """
        self._name = name;

    def __eq__(self, other):
        assert isinstance(other, Star)
        return self._name.lower() == other._name.lower()

    def __lt__(self, other):
        assert isinstance(other, Star)
        return self._name.lower() < other._name.lower()
