'''
Created on Mar 16, 2013

Methods and classes for creating an enum

@author: Robert Tseng
'''

'''
Create an enum based on the tuple passed in. The tuple must consist of instances
of an EnumValue class (or one of its derivatives).
'''
def CreateEnum(values):
    assert isinstance(values, tuple)
    class EnumClass(object):
        __slots__ = [value.name for value in values]
        def __iter__(self): return iter(values)
        def __len__(self): return len(values)
        def __getitem__(self, i): return values[i]

    for number, value in enumerate(values):
        assert isinstance(value, EnumValue)
        setattr(EnumClass, value.name, value)
        value.number = number
    return EnumClass()

'''
Represents a basic enum value
'''
class EnumValue(object):
    def __init__ (self, name):
        self.name = name;

    def __str__(self):
        return self.name;

    def __repr__(self):
        return self.name;

'''
Represents an enum with chinese value associated with it
'''
class ChineseEnumValue(EnumValue):
    def __init__(self, name, chinese):
        EnumValue.__init__(self, name)
        self.chinese = chinese

    def __str__(self):
        return self.chinese

    def __repr__(self):
        return self.chinese
