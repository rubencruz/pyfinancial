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
    
    def testNumberOfPayments(self):
        
        #Scenario with only some variables
        n = numberOfPayments(PAYMENT_TYPE_END, 3.95, 50000, -24895.9738, 0)
        assert n != None
        assert n != 0
        self.assertAlmostEquals(18, n, 0.00001)
        
        n = numberOfPayments(PAYMENT_TYPE_END, 0, 20008.36, -10000, -2500.696667)
        assert n != None
        assert n != 0
        self.assertAlmostEquals(12, n, 0.00001)
        
        #Scenario with the four variables
        n = numberOfPayments(PAYMENT_TYPE_END, 5, 0.000002080, -30000, -5910.52)
        assert n != None
        assert n != 0
        self.assertAlmostEquals(6, n, 0.00001)
        
        n = numberOfPayments(PAYMENT_TYPE_END, 19.58131745, -500, 100, 9.790658e-11)
        assert n != None
        assert n != 0
        self.assertAlmostEquals(9, n, 0.00001)
        
        #Scenario with payment mode in the beggining of the month
        n = numberOfPayments(PAYMENT_TYPE_BEGINNING, 5, 0.000002080, -30000, -5910.52)
        assert n != None
        assert n != 0
        self.assertAlmostEquals(6, n, 0.00001)
        
        n = numberOfPayments(PAYMENT_TYPE_BEGINNING, 19.58131745, -500, 100, 9.790658e-11)
        assert n != None
        assert n != 0
        self.assertAlmostEquals(9, n, 0.00001)
    
    def testPresentValue(self):
        #Scenario with only some variables
        pv = presentValue(PAYMENT_TYPE_END, 3.95, 50000, 18, 0)
        assert pv != None
        assert pv != 0
        self.assertAlmostEquals(-24895.9738, pv, 0.00001)
        
        pv = presentValue(PAYMENT_TYPE_END, 0, 20008.36, 12, -2500.696667)
        assert pv != None
        assert pv != 0
        self.assertAlmostEquals(-10000, pv, 0.00001)
        
        #Scenario with the four variables
        pv = presentValue(PAYMENT_TYPE_END, 5, 0.000002080, 6, -5910.52)
        assert pv != None
        assert pv != 0
        self.assertAlmostEquals(-30000, pv, 0.00001)
        
        pv = presentValue(PAYMENT_TYPE_END, 19.58131745, -500, 9, 9.790658e-11)
        assert pv != None
        assert pv != 0
        self.assertAlmostEquals(100, pv, 0.00001)
        
        #Scenario with payment mode in the beggining of the month
        pv = presentValue(PAYMENT_TYPE_BEGINNING, 5, 0.000002080, 6, -5910.52)
        assert pv != None
        assert pv != 0
        self.assertAlmostEquals(-30000, pv, 0.00001)
        
        pv = presentValue(PAYMENT_TYPE_BEGINNING, 19.58131745, -500, 9, 9.790658e-11)
        assert pv != None
        assert pv != 0
        self.assertAlmostEquals(100, pv, 0.00001)
   
    def testFutureValue(self):
       
        #Scenario with only some variables
        fv = futureValue(PAYMENT_TYPE_END, 3.95, -24895.9738, 18, 0)
        assert fv != None
        assert fv != 0
        self.assertAlmostEquals( 50000, fv, 0.00001)
       
        
        fv = futureValue(PAYMENT_TYPE_END, 0, -10000, 12, -2500.696667)
        assert fv != None
        assert fv != 0
        self.assertAlmostEquals(20008.36, fv, 0.00001)#
        
        #Scenario with the four variables
        fv = futureValue(PAYMENT_TYPE_END, 5, 0.000002080, 6, -5910.52)
        assert fv != None
        assert fv != 0
        self.assertAlmostEquals(-30000, fv, 0.00001)
        
        fv = futureValue(PAYMENT_TYPE_END, 19.58131745, 100, 9, 9.790658e-11)
        assert fv != None
        assert fv != 0
        self.assertAlmostEquals(-500, fv, 0.00001)#
        
        #Scenario with payment mode in the beggining of the month
        fv = futureValue(PAYMENT_TYPE_BEGINNING, 5, -30000, 6, -5910.52)
        assert fv != None
        assert fv != 0
        self.assertAlmostEquals(0.000002080, fv, 0.00001)#
        
        fv = futureValue(PAYMENT_TYPE_BEGINNING, 19.58131745, 100, 9, 9.790658e-11)
        assert fv != None
        assert fv != 0
        self.assertAlmostEquals(-500, fv, 0.00001)#       
    
    def testPayment(self):
        #Scenario with only some variables
        pmt = payment(PAYMENT_TYPE_END, 3.95, 50000, 18, -24895.9738)
        assert pmt != None
        assert pmt != 0
        self.assertAlmostEquals( -1958.631969, pmt, 0.00001)
        
        pmt = payment(PAYMENT_TYPE_END, 0, 20008.36, 12, -10000)
        assert pmt != None
        assert pmt != 0
        self.assertAlmostEquals(-2500.696667, pmt, 0.00001)#
        
        #Scenario with the four variables
        pmt = payment(PAYMENT_TYPE_END, 5, -30000, 6,  0.000002080)
        assert pmt != None
        assert pmt != 0
        self.assertAlmostEquals(-5910.52, pmt, 0.00001)#
        
        pmt = payment(PAYMENT_TYPE_END, 19.58131745, -500, 9, 100)
        assert pmt != None
        assert pmt != 0
        self.assertAlmostEquals(9.790658e-11, pmt, 0.00001)#
        
        #Scenario with payment mode in the beggining of the month
        pmt = payment(PAYMENT_TYPE_BEGINNING, 5, 0.000002080, 6, -30000)
        assert pmt != None
        assert pmt != 0
        self.assertAlmostEquals(-5910.52, pmt, 0.00001)#
        
        pmt = payment(PAYMENT_TYPE_BEGINNING, 19.58131745, -500, 9, 100)
        assert pmt != None
        assert pmt != 0
        self.assertAlmostEquals( 9.790658e-11, pmt, 0.00001)#
    
    def interestRate(self): 
        
        #Scenario with only some variables
        i = interestRate(PAYMENT_TYPE_END, 50000, -24895.9738, 18, 0)
        assert i != None
        assert i != 0
        self.assertAlmostEquals(3.95 , i, 0.00001)#
       
        
        i = interestRate(PAYMENT_TYPE_END, 20008.36, -10000, 12, 0)
        assert i != None
        assert i != 0
        self.assertAlmostEquals(5.949999192, i, 0.00001)#
        
        #Scenario with the four variables
        i = interestRate(PAYMENT_TYPE_END, -30000, 0.000002080, 6, -5910.52)
        assert i != None
        assert i != 0
        self.assertAlmostEquals(5, i, 0.00001)# 
        
        i = interestRate(PAYMENT_TYPE_END, -500, 100, 9, 9.790658e-11)
        assert i != None
        assert i != 0
        self.assertAlmostEquals(19.58131745, i, 0.00001)#
        
        #Scenario with payment mode in the beggining of the month
        i = futureValue(PAYMENT_TYPE_BEGINNING, 0.000002080, -30000, 6, -5910.52)
        assert i != None
        assert i != 0
        self.assertAlmostEquals(5, i, 0.00001)#
        
        i = futureValue(PAYMENT_TYPE_BEGINNING, -500, 100, 9, 9.790658e-11)
        assert i != None
        assert i != 0
        self.assertAlmostEquals(19.58131745, i, 0.00001)#      