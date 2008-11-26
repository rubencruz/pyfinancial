#****************************************************************************
# libraryTests.py, This module contains unit tests for our library 
#
# pyFinancial, a financial library for python users
# Copyright (C) 2008, Felipe Leal, David Candeia, Everton Leandro and Diego Dantas
#*****************************************************************************

from financialLibrary.pyFinancialLibrary import *
import unittest

class LibraryTestCase (unittest.TestCase):
    
    def testEqualNums(self):
        """ Verifies the equalNums method of pyFinancialLibrary.py """
        
        self.assertTrue (equalNums(1,1))
        self.assertTrue(equalNums(0.0, 0.0))
        self.assertTrue(equalNums(0.000000000001, 0.000000000000011))
        self.assertTrue(equalNums(-0.000000000001, 0.000000000000011))
        self.assertTrue(equalNums(0.000000000001, -0.000000000000011))
        self.assertTrue(equalNums(-0.000000000001, -0.000000000000011))
        self.assertFalse(equalNums(0.000000001, 0.000000011))
        self.assertFalse(equalNums(-123.4567891231, 123.4567891230))        
    
    def testAdd(self):
        """ Verifies the add method of pyFinancialLibrary.py """
        
        assert equalNums(add(1, 2), 3)
        assert equalNums(add(0, 0), 0)
        assert equalNums(add(-5, 5), 0)
        assert equalNums(add(-0.3, 5), 4.7)
        assert equalNums(add(-0.3, -5), -5.3)
        assert equalNums(add(-0.2372, 0.0001),-0.2371)
        assert equalNums(add(-0.2372, -0.00001), -0.23721)
        try:
            add(3, "-5as")           
            self.fail("Expected a ValueError")
        except TypeError:
            pass
        try:
            add(3, "*")           
            self.fail("Expected a ValueError")
        except TypeError:
            pass            
        try:
            add(3, list())           
            self.fail("Expected a TypeError")
        except TypeError:
            pass      
    
    def testMinus(self):
        """ Verifies the sub method of pyFinancialLibrary.py """
        
        assert equalNums(sub(2, 1), 1)
        assert equalNums(sub(0, 0), 0)
        assert equalNums(sub(5, -5), 10)
        assert equalNums(sub(5, -0.3), 5.3)
        assert equalNums(sub(-5, -0.3), -4.7)
        assert equalNums(sub(-0.2372, 0.0001), -0.2373)
        assert equalNums(sub(-0.2372, -0.00001), -0.23719)        
        try:
            sub(3, "-5as")           
            self.fail("Expected a ValueError")
        except TypeError:
            pass            
        try:
            sub(3, "*")           
            self.fail("Expected a ValueError")
        except TypeError:
            pass            
        try:
            sub(3, list())           
            self.fail("Expected a TypeError")
        except TypeError:
            pass
    
    def testMult(self):
        """ Verifies the mult method of pyFinancialLibrary.py """
        
        assert equalNums(mult(1, 2), 2)
        assert equalNums(mult(0, 0), 0)
        assert equalNums(mult(-5, 5), -25)
        assert equalNums(mult(-0.3, 5), -1.5)
        assert equalNums(mult(-0.3, -5), 1.5)
        assert equalNums(mult(-0.2372, 0.0001), -0.00002372)
        assert equalNums(mult(-0.2372, -0.00001), 0.000002372)        
        try:
            mult(3, "-5as")           
            self.fail("Expected a ValueError")
        except TypeError:
            pass
        try:
            mult(3, "*")           
            self.fail("Expected a ValueError")
        except TypeError:
            pass
        try:
            mult(3, list())           
            self.fail("Expected a TypeError")
        except TypeError:
            pass

    def testDiv(self):
        """ Verifies the div method of pyFinancialLibrary.py """
        
        assert equalNums(div(1, 2), 0.5)
        assert equalNums(div(2, 1),  2)
        assert equalNums(div(-5, 5), -1)
        assert equalNums(div(5, -5), -1)
        assert equalNums(div(-0.3, 5), -0.06)
        assert equalNums(div(-0.3, -5), 0.06)
        assert equalNums(div(-0.2372, 0.0001), -2372)
        assert equalNums(div(-0.2372, -0.00001), 23720)
        try:
            div(3, "-5as")           
            self.fail("Expected a ValueError")
        except TypeError:
            pass
        try:
            div(3, "*")           
            self.fail("Expected a ValueError")
        except TypeError:
            pass
        try:
            div(3, list())           
            self.fail("Expected a TypeError")
        except TypeError:
            pass        
        try:
            div(3, 0)           
            self.fail("Expected a ZeroDivisionError")
        except ZeroDivisionError:
            pass
        