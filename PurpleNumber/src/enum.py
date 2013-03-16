'''
Created on Mar 16, 2013

Methods and classes for creating an enum

@author: mac
'''

'''
Create an enum based on the tuple passed in. It will return a class
'''
def CreateEnum(values):
    assert isinstance(values, tuple)
    class EnumClass(object):
        __slots__ = [value.name for value in values]
        def __iter__(self): return iter(values)
        def __len__(self): return len(values)
        def __getitem__(self, i): return values[i]

    for number, value in enumerate(values):
        setattr(EnumClass, value.name, value)
        value.number = number
    return EnumClass()

class EnumValue(object):
    def __init__ (self, name):
        self.name = name;

    def __str__(self):
        return self.name;

    def __repr__(self):
        return self.name;

class ChineseEnumValue(EnumValue):
    def __init__(self, name, chinese):
        EnumValue.__init__(self, name)
        self.__chinese = chinese

    def __str__(self):
        return self.__chinese

    def __repr__(self):
        return self.__chinese
