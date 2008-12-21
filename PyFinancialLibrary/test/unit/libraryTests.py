# *********************************************************************************
# Copyright (c) 2008, Felipe Coutinho, David Maia, Everton Leandro and Diego Dantas
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the PyFinancial Calculator Team nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY Felipe Coutinho, 
# David Maia, Everton Leandro and Diego Dantas ''AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <copyright holder> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# *********************************************************************************
#
# pyFinancialLibraryTests.py, This module contains tests for the financial functions
#being implemented
#
#*****************************************************************************

import unittest
from financialLibrary.pyFinancialLibrary import *


TOLERANCE = 3

class LibraryTestCase (unittest.TestCase):
     
    def testAdd(self):
        """ Verifies the add method of pyFinancialLibrary.py """
        
        assert add(1, 2) == 3
        assert add(0, 0) == 0
        assert add(-5, 5) == 0
        assert add(-0.3, 5) == convertToDecimal(4.7)
        assert add(-0.3, -5) == convertToDecimal(-5.3)
        assert add(-0.2372, 0.0001) == convertToDecimal(-0.2371)
        assert add(-0.2372, -0.00001) == convertToDecimal(-0.23721)
        try:
            add(3, "-5as")           
            self.fail("Expected a ValueError")
        except InvalidOperation:
            pass
        try:
            add(3, "*")           
            self.fail("Expected a ValueError")
        except InvalidOperation:
            pass            
        try:
            add(3, list())           
            self.fail("Expected a TypeError")
        except InvalidOperation:
            pass      
    
    def testMinus(self):
        """ Verifies the sub method of pyFinancialLibrary.py """
        
        assert sub(2, 1) == 1
        assert sub(0, 0) == 0
        assert sub(5, -5) == 10
        assert sub(5, -0.3) == convertToDecimal(5.3)
        assert sub(-5, -0.3) == convertToDecimal(-4.7)
        assert sub(-0.2372, 0.0001) == convertToDecimal(-0.2373)
        assert sub(-0.2372, -0.00001) == convertToDecimal(-0.23719)        
        try:
            sub(3, "-5as")           
            self.fail("Expected a ValueError")
        except InvalidOperation:
            pass            
        try:
            sub(3, "*")           
            self.fail("Expected a ValueError")
        except InvalidOperation:
            pass            
        try:
            sub(3, list())           
            self.fail("Expected a TypeError")
        except InvalidOperation:
            pass
    
    def testMult(self):
        """ Verifies the mult method of pyFinancialLibrary.py """
        
        assert mult(1, 2) == 2
        assert mult(0, 0) == 0
        assert mult(-5, 5) == -25
        assert mult(-0.3, 5) == convertToDecimal(-1.5)
        assert mult(-0.3, -5) == convertToDecimal(1.5)
        assert mult(-0.2372, 0.0001) == convertToDecimal(-0.00002372)
        assert mult(-0.2372, -0.00001) == convertToDecimal(0.000002372)        
        try:
            mult(3, "-5as")           
            self.fail("Expected a ValueError")
        except InvalidOperation:
            pass
        try:
            mult(3, "*")           
            self.fail("Expected a ValueError")
        except InvalidOperation:
            pass
        try:
            mult(3, list())           
            self.fail("Expected a TypeError")
        except InvalidOperation:
            pass

    def testDiv(self):
        """ Verifies the div method of pyFinancialLibrary.py """
        
        assert div(1, 2) == convertToDecimal(0.5)
        assert div(2, 1) ==  2
        assert div(-5, 5) == -1
        assert div(5, -5) == -1
        assert div(-0.3, 5) == convertToDecimal(-0.06)
        assert div(-0.3, -5) == convertToDecimal(0.06)
        assert div(-0.2372, 0.0001) == -2372
        assert div(-0.2372, -0.00001) == 23720
        try:
            div(3, "-5as")           
            self.fail("Expected a ValueError")
        except InvalidOperation:
            pass
        try:
            div(3, "*")           
            self.fail("Expected a ValueError")
        except InvalidOperation:
            pass
        try:
            div(3, list())           
            self.fail("Expected a ValueError")
        except InvalidOperation:
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
        self.assertAlmostEquals(18, n, TOLERANCE)
        
#        n = numberOfPayments(PAYMENT_TYPE_END, 3.95, 0, 10000, -2500.696667)
#        assert n != None
#        assert n != 0
#        self.assertAlmostEquals(5, n, TOLERANCE)
        
#        n = numberOfPayments(PAYMENT_TYPE_END, 3.95, 50000, 0, -2500.696667)
#        assert n != None
#        assert n != 0
#        self.assertAlmostEquals(16, n, TOLERANCE)
        
        n = numberOfPayments(PAYMENT_TYPE_END, 0, 20008.36, -10000, -2500.696667)
        assert n != None
        assert n != 0
        self.assertAlmostEquals(12, n, TOLERANCE)
        
        #Scenario with the four variables
        try:
            n = numberOfPayments(PAYMENT_TYPE_END, 5, 0.000002080, -30000, -5910.52)
            self.fail("Invalid number of payments")
            assert n != None
            assert n != 0
            self.assertAlmostEquals(6, n, TOLERANCE)
        except ValueError:
            pass    
        
        n = numberOfPayments(PAYMENT_TYPE_END, 19.58131745, -500, 100, 9.790658e-11)
        assert n != None
        assert n != 0
        self.assertAlmostEquals(9, n, TOLERANCE)
        
        #Scenario with payment mode in the beggining of the month
        try:
            n = numberOfPayments(PAYMENT_TYPE_BEGINNING, 5, 0.000002080, -30000, -5910.52)
            self.fail("Invalid number of payments")
            assert n != None
            assert n != 0
            self.assertAlmostEquals(6, n, TOLERANCE)
        except ValueError:
            pass
        
        n = numberOfPayments(PAYMENT_TYPE_BEGINNING, 19.58131745, -500, 100, 9.790658e-11)
        assert n != None
        assert n != 0
        self.assertAlmostEquals(9, n, TOLERANCE)
    
    def testPresentValue(self):
        
        #Scenario with only some variables
        pv = presentValue(PAYMENT_TYPE_END, 3.95, 50000, 18, 0)
        assert pv != None
        assert pv != 0
        self.assertAlmostEquals(convertToDecimal(-24895.9738), pv, TOLERANCE)
        
        pv = presentValue(PAYMENT_TYPE_END, 0, 50000, 18, -1953.2486)
        assert pv != None
        assert pv != 0
        self.assertAlmostEquals(convertToDecimal(-14841.5252), pv, TOLERANCE)
        
#        pv = presentValue(PAYMENT_TYPE_END, 3.98, 0, 18, -1953.2486)
#        assert pv != None
#        assert pv != 0
#        self.assertAlmostEquals(convertToDecimal(24766.9979), pv, TOLERANCE)
        
        pv = presentValue(PAYMENT_TYPE_END, 3.98, 50000, 0, -1953.2486)
        assert pv != None
        assert pv != 0
        self.assertAlmostEquals(-50000, pv, TOLERANCE)
        
        pv = presentValue(PAYMENT_TYPE_END, 0, 20008.36, 12, -2500.696667)
        assert pv != None
        assert pv != 0
        self.assertAlmostEquals(-10000, pv, TOLERANCE)
        
        #Scenario with the four variables
#        pv = presentValue(PAYMENT_TYPE_END, 5, 0.000002080, 6, -5910.52)
#        assert pv != None
#        assert pv != 0
#        self.assertAlmostEquals(convertToDecimal(29999.9795), pv, TOLERANCE)
        
#        pv = presentValue(PAYMENT_TYPE_END, 19.58131745, -500, 9, 9.790658e-11)
#        assert pv != None
#        assert pv != 0
#        self.assertAlmostEquals(100, pv, TOLERANCE)
        
        #Scenario with payment mode in the beggining of the month
#        pv = presentValue(PAYMENT_TYPE_BEGINNING, 5, 0.000002080, 6, -5910.52)
#        assert pv != None
#        assert pv != 0
#        self.assertAlmostEquals(convertToDecimal(31499.9785), pv, TOLERANCE)
        
#        pv = presentValue(PAYMENT_TYPE_BEGINNING, 19.58131745, -500, 9, 9.790658e-11)
#        assert pv != None
#        assert pv != 0
#        self.assertAlmostEquals(100, pv, TOLERANCE)
   
#    def testFutureValue(self):
       
        #Scenario with only some variables
#        fv = futureValue(PAYMENT_TYPE_END, 3.95, -24895.9738, 18, 0)
#        assert fv != None
#        assert fv != 0
#        self.assertAlmostEquals( 50000, fv, TOLERANCE)
        
#        fv = futureValue(PAYMENT_TYPE_END, 3.95, -24895.9738, 0, 1958.6320)
#        assert fv != None
#        assert fv != 0
#        self.assertAlmostEquals( 24895.9738, fv, TOLERANCE)
#        
#        fv = futureValue(PAYMENT_TYPE_END, 3.95, 0, 18, 1958.6320)
#        assert fv != None
#        assert fv != 0
#        self.assertAlmostEquals(-50000.0, fv, 1)
#        
#        fv = futureValue(PAYMENT_TYPE_END, 0, -10000, 12, -2500.696667)
#        assert fv != None
#        assert fv != 0
#        self.assertAlmostEquals(40008.36, fv, TOLERANCE)#
#        
#        #Scenario with the four variables
#        fv = futureValue(PAYMENT_TYPE_END, 5, 0.000002080, 6, 5910.52)
#        assert fv != None
#        assert fv != 0
#        self.assertAlmostEquals(-40202.8417, fv, TOLERANCE)
#        
#        fv = futureValue(PAYMENT_TYPE_END, 19.58131745, 100, 9, 9.790658e-11)
#        assert fv != None
#        assert fv != 0
#        self.assertAlmostEquals(-500, fv, TOLERANCE)#
#        
#        #Scenario with payment mode in the beggining of the month
#        fv = futureValue(PAYMENT_TYPE_BEGINNING, 5, -30000, 6, -5910.52)
#        assert fv != None
#        assert fv != 0
#        self.assertAlmostEquals(82415.8530, fv, TOLERANCE)#
#        
#        fv = futureValue(PAYMENT_TYPE_BEGINNING, 19.58131745, 100, 9, 9.790658e-11)
#        assert fv != None
#        assert fv != 0
#        self.assertAlmostEquals(-500, fv, TOLERANCE)#   
#        
#        fv = futureValue(PAYMENT_TYPE_BEGINNING, 0, 10000, 12, -2500.696667)
#        assert fv != None
#        assert fv != 0
#        self.assertAlmostEquals(20008.36, fv, TOLERANCE)    
#    
#    def testPayment(self):
        
        #Scenario with only some variables
#        pmt = payment(PAYMENT_TYPE_END, 3.95, 0, 18, -24895.9738)
#        assert pmt != None
#        assert pmt != 0
#        self.assertAlmostEquals( convertToDecimal(1958.6320), pmt, TOLERANCE)
#        
#        pmt = payment(PAYMENT_TYPE_END, 0, 20008.36, 12, -10000)
#        assert pmt != None
#        assert pmt != 0
#        self.assertAlmostEquals(-2500.696667, pmt, TOLERANCE)#
#        
#        #Scenario with the four variables
#        pmt = payment(PAYMENT_TYPE_END, 5, -30000, 6,  0.000002080)
#        assert pmt != None
#        assert pmt != 0
#        self.assertAlmostEquals(-4410.5240, pmt, TOLERANCE)#
#        
#        pmt = payment(PAYMENT_TYPE_END, 19.58131745, -500, 9, 100)
#        assert pmt != None
#        assert pmt != 0
#        self.assertAlmostEquals(9.790658e-11, pmt, TOLERANCE)#
#        
#        #Scenario with payment mode in the beggining of the month
#        pmt = payment(PAYMENT_TYPE_BEGINNING, 5, 0.000002080, 6, -30000)
#        assert pmt != None
#        assert pmt != 0
#        self.assertAlmostEquals(5629.0705, pmt, TOLERANCE)#
#        
#        pmt = payment(PAYMENT_TYPE_BEGINNING, 19.58131745, -500, 9, 100)
#        assert pmt != None
#        assert pmt != 0
#        self.assertAlmostEquals( 9.790658e-11, pmt, TOLERANCE)#
#    
    def interestRate(self): 
        
        #Scenario with only some variables
        i = interestRate(PAYMENT_TYPE_END, 50000, -24895.9738, 18, 0)
        assert i != None
        assert i != 0
        self.assertAlmostEquals(3.95 , i, TOLERANCE)#
       
        try:
            i = interestRate(PAYMENT_TYPE_END, 0, -24895.9738, 18, -1394.668122)
            self.fail("Invalid scenario")
            assert i != None
            assert i != 0
            self.assertAlmostEquals(3.95 , i, TOLERANCE)#
        except ValueError:
            pass    
       
        i = interestRate(PAYMENT_TYPE_END, 50000, 0, 18, -1394.668122)
        self.fail("Invalid scenario")
        assert i != None
        assert i != 0
        self.assertAlmostEquals(0.000000001 , i, TOLERANCE)#
        
        try:
            i = interestRate(PAYMENT_TYPE_END, 50000, -24895.9738, 0, -1394.668122)
            self.fail("Invalid scenario")
            assert i != None
            assert i != 0
            self.assertAlmostEquals(0.000000001 , i, TOLERANCE)#
        except ValueError:
            pass
            
        i = interestRate(PAYMENT_TYPE_END, 20008.36, -10000, 12, 0)
        assert i != None
        assert i != 0
        self.assertAlmostEquals(5.949999192, i, TOLERANCE)#
        
        #Scenario with the four variables
        i = interestRate(PAYMENT_TYPE_END, -30000, 0.000002080, 6, -5910.52)
        assert i != None
        assert i != 0
        self.assertAlmostEquals(2.841596e11, i, TOLERANCE)# 
        
        i = interestRate(PAYMENT_TYPE_END, -500, 100, 9, 9.790658e-11)
        assert i != None
        assert i != 0
        self.assertAlmostEquals(19.58131745, i, TOLERANCE)#
        
        #Scenario with payment mode in the beggining of the month
        i = futureValue(PAYMENT_TYPE_BEGINNING, 0.000002080, -30000, 6, -5910.52)
        assert i != None
        assert i != 0
        self.assertAlmostEquals(-99.99999996, i, TOLERANCE)#
        
        i = futureValue(PAYMENT_TYPE_BEGINNING, -500, 100, 9, 9.790658e-11)
        assert i != None
        assert i != 0
        self.assertAlmostEquals(19.58131745, i, TOLERANCE)#