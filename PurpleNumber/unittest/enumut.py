# coding=utf-8
'''
Created on Mar 16, 2013

Test the CreateEnum method

@author: Robert Tseng
'''
import unittest
from core.enum import *

class Test(unittest.TestCase):


    def testCreateEnumWithEnumValue(self):
        # set up pet enum
        class PetEnumValue(EnumValue):
            pass

        pets = ["CAT", "DOG", "GOLDFISH"]
        petsTuple = tuple(PetEnumValue(name) for name in pets)
        PetEnum = CreateEnum(petsTuple);
        
        # verify the enum contain right number of elements
        self.assertEqual(len(list(iter(PetEnum))), 3);
        self.assertEqual(len(PetEnum), 3);

        # verify each elements individually
        self.assertEqual(PetEnum.CAT.name, "CAT")
        self.assertEqual(PetEnum.CAT.number, 0)
        self.assertEqual(PetEnum.DOG.name, "DOG")
        self.assertEqual(PetEnum.DOG.number, 1)
        self.assertEqual(PetEnum.GOLDFISH.name, "GOLDFISH")
        self.assertEqual(PetEnum.GOLDFISH.number, 2)

        # verify that each enum is exactly equal to itself
        for i in xrange(len(PetEnum)):
            self.assertTrue(isinstance(PetEnum[i], PetEnumValue))
            for j in xrange(len(PetEnum)):
                self.assertEqual(i == j, PetEnum[i] == PetEnum[j])


    def testCreateEnumWithChineseEnumValue(self):
        # set up pet enum
        class PetEnumValue(ChineseEnumValue):
            pass
        pets = [("CAT", "貓"), ("DOG", "狗"), ("GOLDFISH", "魚")]
        petsTuple = tuple(PetEnumValue(name, chinese) for name, chinese in pets)
        PetEnum = CreateEnum(petsTuple)

        # verify the enum contain right number of elements
        self.assertEqual(len(list(iter(PetEnum))), 3);
        self.assertEqual(len(PetEnum), 3);

        # verify each elements individually
        self.assertEqual(PetEnum.CAT.name, "CAT")
        self.assertEqual(PetEnum.CAT.number, 0)
        self.assertEqual(PetEnum.CAT.chinese, "貓")
        self.assertEqual(PetEnum.DOG.name, "DOG")
        self.assertEqual(PetEnum.DOG.number, 1)
        self.assertEqual(PetEnum.DOG.chinese, "狗")
        self.assertEqual(PetEnum.GOLDFISH.name, "GOLDFISH")
        self.assertEqual(PetEnum.GOLDFISH.number, 2)
        self.assertEqual(PetEnum.GOLDFISH.chinese, "魚")

        # verify that each enum is exactly equal to itself
        for i in xrange(len(PetEnum)):
            self.assertTrue(isinstance(PetEnum[i], PetEnumValue))
            for j in xrange(len(PetEnum)):
                self.assertEqual(i == j, PetEnum[i] == PetEnum[j])

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
