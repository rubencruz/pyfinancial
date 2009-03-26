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
    
    def myAssertRaises(self, error, msg, method, *a, **kw):
        try:
            result = method(*a, **kw)
        except error, e:
            pass
        else:
            self.fail("Expected a " + str(error) + ", but got " + str(result))
            
    def myAssertEquals(self, expected_result, method, *a, **kw):
        res = method(*a, **kw)
        assert res != None
        self.assertAlmostEquals(expected_result, res, TOLERANCE)
            
     
    def testAdd(self):
        """ Verifies the add method of pyFinancialLibrary.py """
        
        assert add(1, 2) ==  Decimal("3.0")
        assert add(0, 0) == Decimal("0.0")
        assert add(-5, 5) == Decimal("0.0")
        assert add(-0.3, 5) == Decimal("4.7")
        assert add(-0.3, -5) == Decimal("-5.3")
        assert add(-0.2372, 0.0001) == Decimal ("-0.2371")
        assert add(-0.2372, -0.00001) ==  Decimal("-0.23721")
        try:
            add(3, "-5as")           
            self.fail("Exception expected")
        except PyFinancialLibraryException:
            pass
        try:
            add(3, "*")           
            self.fail("Exception expected")
        except  PyFinancialLibraryException:
            pass            
        try:
            add(3, list())           
            self.fail("Exception expected")
        except  PyFinancialLibraryException:
            pass      
    
    def testMinus(self):
        """ Verifies the sub method of pyFinancialLibrary.py """
        
        assert sub(2, 1) == Decimal("1.0")
        assert sub(0, 0) ==  Decimal("0.0")
        assert sub(5, -5) ==  Decimal("10.0")
        assert sub(5, -0.3) == Decimal("5.3")
        assert sub(-5, -0.3) == Decimal("-4.7")
        assert sub(-0.2372, 0.0001) == Decimal("-0.2373")
        assert sub(-0.2372, -0.00001) == Decimal("-0.23719")        
        try:
            sub(3, "-5as")           
            self.fail("Exception expected")
        except PyFinancialLibraryException:
            pass            
        try:
            sub(3, "*")           
            self.fail("Exception expected")
        except PyFinancialLibraryException:
            pass            
        try:
            sub(3, list())           
            self.fail("Exception expected")
        except  PyFinancialLibraryException:
            pass
    
    def testMult(self):
        """ Verifies the mult method of pyFinancialLibrary.py """
        
        assert mult(1, 2) == Decimal("2.0")
        assert mult(0, 0) == Decimal("0.0")
        assert mult(-5, 5) == Decimal("-25.0")
        assert mult(-0.3, 5) == Decimal("-1.5")
        assert mult(-0.3, -5) == Decimal("1.5")
        assert mult(-0.2372, 0.0001) == Decimal("-0.00002372")
        assert mult(-0.2372, -0.00001) == Decimal("0.000002372")        
        try:
            mult(3, "-5as")           
            self.fail("Exception expected")
        except PyFinancialLibraryException:
            pass
        try:
            mult(3, "*")           
            self.fail("Exception expected")
        except  PyFinancialLibraryException:
            pass
        try:
            mult(3, list())           
            self.fail("Exception expected")
        except  PyFinancialLibraryException:
            pass

    def testDiv(self):
        """ Verifies the div method of pyFinancialLibrary.py """
        
        assert div(1, 2) == Decimal("0.5")
        assert div(2, 1) ==  Decimal("2.0")
        assert div(-5, 5) == Decimal("-1.0")
        assert div(5, -5) == Decimal("-1.0")
        assert div(-0.3, 5) == Decimal("-0.06")
        assert div(-0.3, -5) == Decimal("0.06")
        assert div(-0.2372, 0.0001)  == Decimal("-2372.0")
        assert div(-0.2372, -0.00001) == Decimal("23720.0")
        try:
            div(3, "-5as")           
            self.fail("Exception expected")
        except  PyFinancialLibraryException:
            pass
        try:
            div(3, "*")           
            self.fail("Exception expected")
        except  PyFinancialLibraryException:
            pass
        try:
            div(3, list())           
            self.fail("Exception expected")
        except  PyFinancialLibraryException:
            pass        
        try:
            div(3, 0)           
            self.fail("Expected a ZeroDivisionError")
        except PyFinancialLibraryException:
            pass
    
    def testNumberOfPayments(self):
        
        #>> END MODE 
        self.myAssertEquals(Decimal("0"), numberOfPayments, PAYMENT_TYPE_END, 
                 i=Decimal("0"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("0"))
                
        #Testing one value
        self.myAssertRaises(PyFinancialLibraryException,"Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_END, 
                            i=Decimal("10"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("0"))
                
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: i value less than -100.", numberOfPayments, PAYMENT_TYPE_END, 
                            i=Decimal("-110"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("0"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_END, 
                            i=Decimal("0"), fv=Decimal("100"), pv=Decimal("0"), pmt=Decimal("0"))
                
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_END, 
                            i=Decimal("0"), fv=Decimal("-100"), pv=Decimal("0"), pmt=Decimal("0"))
            
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_END, 
                            i=Decimal("0"), fv=Decimal("0"), pv=Decimal("50"), pmt=Decimal("0"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_END, 
                            i=Decimal("0"), fv=Decimal("0"), pv=Decimal("-50"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("0"), numberOfPayments, PAYMENT_TYPE_END, 
                 i=Decimal("0"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("70"))        
        
        self.myAssertEquals(Decimal("0"), numberOfPayments, PAYMENT_TYPE_END, 
                 i=Decimal("0"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("-70"))
             
        #Testing two values
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_END, 
                            i=Decimal("10"), fv=Decimal("100"), pv=Decimal("0"), pmt=Decimal("0"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_END, 
                            i=Decimal("-10"), fv=Decimal("-100"), pv=Decimal("0"), pmt=Decimal("0"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Infinite n.", numberOfPayments, PAYMENT_TYPE_END, 
                            i=Decimal("-10"), fv=Decimal("0"), pv=Decimal("50"), pmt=Decimal("0"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Infinite n.", numberOfPayments, PAYMENT_TYPE_END, 
                            i=Decimal("10"), fv=Decimal("0"), pv=Decimal("-50"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("0"), numberOfPayments, PAYMENT_TYPE_END, 
                 i=Decimal("10"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("100"))
        
        self.myAssertEquals(Decimal("0"), numberOfPayments, PAYMENT_TYPE_END, 
                 i=Decimal("10"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("-100"))
             
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_END, 
                            i=Decimal("0"), fv=Decimal("10"), pv=Decimal("50"), pmt=Decimal("0"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_END, 
                            i=Decimal("0"), fv=Decimal("10"), pv=Decimal("-50"), pmt=Decimal("0"))
        
        #FIXME - Review this test: No emulador deu -2
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_END, 
                            i=Decimal("0"), fv=Decimal("10"), pv=Decimal("0"), pmt=Decimal("5"))
                
        self.myAssertEquals(Decimal("2"), numberOfPayments, PAYMENT_TYPE_END, 
                 i=Decimal("0"), fv=Decimal("-10"), pv=Decimal("0"), pmt=Decimal("5"))

        #FIXME - Review this test: No emulador deu -10
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_END, 
                            i=Decimal("0"), fv=Decimal("0"), pv=Decimal("50"), pmt=Decimal("5"))
        
        self.myAssertEquals(Decimal("5"), numberOfPayments, PAYMENT_TYPE_END, 
                 i=Decimal("0"), fv=Decimal("0"), pv=Decimal("50"), pmt=Decimal("-10"))        
                
        #Three values
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_END, 
                            i=Decimal("10"), fv=Decimal("50"), pv=Decimal("10"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("1"), numberOfPayments, PAYMENT_TYPE_END, 
                 i=Decimal("10"), fv=Decimal("0"), pv=Decimal("-10"), pmt=Decimal("70"))
        
        #FIXME - Review this test: No emulador deu -7,00
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_END, 
                            i=Decimal("10"), fv=Decimal("50"), pv=Decimal("0"), pmt=Decimal("10"))
                
        self.myAssertEquals(Decimal("5"), numberOfPayments, PAYMENT_TYPE_END, 
                 i=Decimal("10"), fv=Decimal("50"), pv=Decimal("0"), pmt=Decimal("-10"))
        
        self.myAssertEquals(Decimal("6"), numberOfPayments, PAYMENT_TYPE_END, 
                 i=Decimal("0"), fv=Decimal("50"), pv=Decimal("10"), pmt=Decimal("-10"))

        self.myAssertEquals(Decimal("4"), numberOfPayments, PAYMENT_TYPE_END, 
                 i=Decimal("0"), fv=Decimal("50"), pv=Decimal("-10"), pmt=Decimal("-10"))
#        No emulador deu -1
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_END, 
                            i=Decimal("10"), fv=Decimal("0"), pv=Decimal("-10"), pmt=Decimal("-10"))
        
        self.myAssertEquals(Decimal("1"), numberOfPayments, PAYMENT_TYPE_END, 
                 i=Decimal("-10"), fv=Decimal("0"), pv=Decimal("10"), pmt=Decimal("-10"))
        
        #Four values
        self.myAssertEquals(Decimal("4"), numberOfPayments, PAYMENT_TYPE_END, 
                 i=Decimal("5"), fv=Decimal("50"), pv=Decimal("-10"), pmt=Decimal("-10"))        
              
        #FIXME - Review this test: No emulador deu -11 e no nosso -11.82
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_END, 
                            i=Decimal("-5"), fv=Decimal("50"), pv=Decimal("-10"), pmt=Decimal("2"))
        
        #>> BEG MODE 
        self.myAssertEquals(Decimal("0"), numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("0"))
                
        #Testing one value
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                            i=Decimal("10"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("0"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                            i=Decimal("-10"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("0"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                            i=Decimal("0"), fv=Decimal("100"), pv=Decimal("0"), pmt=Decimal("0"))
                
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                            i=Decimal("0"), fv=Decimal("-100"), pv=Decimal("0"), pmt=Decimal("0"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                            i=Decimal("0"), fv=Decimal("0"), pv=Decimal("50"), pmt=Decimal("0"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                            i=Decimal("0"), fv=Decimal("0"), pv=Decimal("-50"), pmt=Decimal("0"))
                
        self.myAssertEquals(Decimal("0"), numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("70"))
        
        self.myAssertEquals(Decimal("0"), numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("-70"))
                
        #Testing two values
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                            i=Decimal("10"), fv=Decimal("100"), pv=Decimal("0"), pmt=Decimal("0"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                            i=Decimal("-10"), fv=Decimal("-100"), pv=Decimal("0"), pmt=Decimal("0"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                            i=Decimal("-10"), fv=Decimal("0"), pv=Decimal("50"), pmt=Decimal("0"))
                
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                            i=Decimal("10"), fv=Decimal("0"), pv=Decimal("-50"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("0"), numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                            i=Decimal("10"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("100"))
        
        self.myAssertEquals(Decimal("0"), numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                            i=Decimal("10"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("-100"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                            i=Decimal("0"), fv=Decimal("10"), pv=Decimal("50"), pmt=Decimal("0"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                            i=Decimal("0"), fv=Decimal("10"), pv=Decimal("-50"), pmt=Decimal("0"))

        #FIXME - Review this test: No emulador deu -2      
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                            i=Decimal("0"), fv=Decimal("10"), pv=Decimal("0"), pmt=Decimal("5"))
                
        self.myAssertEquals(Decimal("2"), numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), fv=Decimal("-10"), pv=Decimal("0"), pmt=Decimal("5"))
                
        #FIXME - Review this test: No emulador deu -10
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                            i=Decimal("0"), fv=Decimal("0"), pv=Decimal("50"), pmt=Decimal("5"))
            
        self.myAssertEquals(Decimal("5"), numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), fv=Decimal("0"), pv=Decimal("50"), pmt=Decimal("-10"))
                
        #Three values
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                            i=Decimal("10"), fv=Decimal("50"), pv=Decimal("10"), pmt=Decimal("0"))
                
        self.myAssertEquals(Decimal("17"), numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), fv=Decimal("50"), pv=Decimal("-10"), pmt=Decimal("0"))
        
        #FIXME - Review this test: No emulador deu -6
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                            i=Decimal("10"), fv=Decimal("50"), pv=Decimal("0"), pmt=Decimal("10"))
        
        self.myAssertEquals(Decimal("4"), numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), fv=Decimal("50"), pv=Decimal("0"), pmt=Decimal("-10"))
        
        self.myAssertEquals(Decimal("6"), numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), fv=Decimal("50"), pv=Decimal("10"), pmt=Decimal("-10"))       
        
        self.myAssertEquals(Decimal("0"), numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("4"), numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), fv=Decimal("50"), pv=Decimal("-10"), pmt=Decimal("-10"))
                
        #FIXME - Review this test: No emulador deu 0 e o nosso -1
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                            i=Decimal("10"), fv=Decimal("0"), pv=Decimal("-10"), pmt=Decimal("-10"))
                
        self.myAssertEquals(Decimal("1"), numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("-10"), fv=Decimal("0"), pv=Decimal("10"), pmt=Decimal("-10"))
        
        #Four values
        
        self.myAssertEquals(Decimal("4"), numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("5"), fv=Decimal("50"), pv=Decimal("-10"), pmt=Decimal("-10"))
        
        #FIXME - Review this test: No emulador deu -11 e o nosso -11.82
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_BEGINNING, 
                            i=Decimal("-5"), fv=Decimal("50"), pv=Decimal("-10"), pmt=Decimal("2"))
                
        #Scenario with only some variables

        #FIXME - Review this test Nosso deu 19
#        self.myAssertEquals(Decimal("18"), numberOfPayments, PAYMENT_TYPE_END, 
#                 i=Decimal("3.95"), fv=Decimal("50000"), pv=Decimal("-24895.9738"), pmt=Decimal("0"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_END, 
                 i=Decimal("3.95"), fv=Decimal("0"), pv=Decimal("100"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("78"), numberOfPayments, PAYMENT_TYPE_END, 
                 i=Decimal("3.95"), fv=Decimal("50000"), pv=Decimal("-2500.696667"), pmt=Decimal("0"))
        
        #FIXME - Review this test No emulador deu 4 e no nosso 5
#        self.myAssertEquals(Decimal("4"), numberOfPayments, PAYMENT_TYPE_END, 
#                 i=Decimal("0"), fv=Decimal("20008.36"), pv=Decimal("-10000"), pmt=Decimal("-2500.696667"))
        
        #FIXME - Review this test No emulador deu -4 e no nosso -4.63
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", numberOfPayments, PAYMENT_TYPE_END, 
                            i=Decimal("5"), fv=Decimal("0.000002080"), pv=Decimal("-30000"), pmt=Decimal("-5910.52"))
                
    
    def testPresentValue(self):
        
        #>> END MODE
        #Testing one value
        self.myAssertEquals(Decimal("0"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), fv=Decimal("0"), n=Decimal("0"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("0"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("10"), fv=Decimal("0"), n=Decimal("0"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("-10"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), fv=Decimal("10"), n=Decimal("0"), pmt=Decimal("0"))

        self.myAssertEquals(Decimal("20.50"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), fv=Decimal("-20.50"), n=Decimal("0"), pmt=Decimal("0"))

        self.myAssertEquals(Decimal("0"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), fv=Decimal("0"), n=Decimal("10"), pmt=Decimal("0"))

        self.myAssertEquals(Decimal("0"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), fv=Decimal("0"), n=Decimal("-10"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("0"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), fv=Decimal("0"), n=Decimal("0"), pmt=Decimal("10"))
       
        self.myAssertEquals(Decimal("0"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), fv=Decimal("0"), n=Decimal("0"), pmt=Decimal("-10"))
        
        #Testing two values
        self.myAssertEquals(Decimal("20"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("10"), fv=Decimal("-20"), n=Decimal("0"), pmt=Decimal("0"))

        self.myAssertEquals(Decimal("-20"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("-10"), fv=Decimal("20"), n=Decimal("0"), pmt=Decimal("0"))

        self.myAssertEquals(Decimal("0"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("10"), fv=Decimal("0"), n=Decimal("5"), pmt=Decimal("0"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: i value less than -100.", presentValue, PAYMENT_TYPE_END, 
                            i=Decimal("-110"), fv=Decimal("20"), n=Decimal("0"), pmt=Decimal("0"))
                    
        self.myAssertEquals(Decimal("0"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("-10"), fv=Decimal("0"), n=Decimal("0"), pmt=Decimal("50"))

        self.myAssertEquals(Decimal("40"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), fv=Decimal("-20"), n=Decimal("2"), pmt=Decimal("-10"))

        self.myAssertEquals(Decimal("-40"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), fv=Decimal("20"), n=Decimal("-2"), pmt=Decimal("-10"))

        self.myAssertEquals(Decimal("20"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), fv=Decimal("-20"), n=Decimal("0"), pmt=Decimal("100"))

        self.myAssertEquals(Decimal("-20"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), fv=Decimal("20"), n=Decimal("0"), pmt=Decimal("50"))

        self.myAssertEquals(Decimal("600"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), fv=Decimal("0"), n=Decimal("-6"), pmt=Decimal("100"))

        self.myAssertEquals(Decimal("-600"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), fv=Decimal("0"), n=Decimal("-6"), pmt=Decimal("-100"))

        self.myAssertEquals(Decimal("250"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), fv=Decimal("0"), n=Decimal("5"), pmt=Decimal("-50"))
        
        #Testing three values
        self.myAssertEquals(Decimal("28.224"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("10"), fv=Decimal("-50"), n=Decimal("6"), pmt=Decimal("0"))
     
        self.myAssertEquals(Decimal("100"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("10"), fv=Decimal("-100"), n=Decimal("0"), pmt=Decimal("-50"))
        
        self.myAssertEquals(Decimal("-100"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("-10"), fv=Decimal("100"), n=Decimal("0"), pmt=Decimal("-50"))
        
        self.myAssertEquals(Decimal("-771.561"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("10"), fv=Decimal("0"), n=Decimal("-6"), pmt=Decimal("-100"))
        
        self.myAssertEquals(Decimal("881.676"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("-10"), fv=Decimal("0"), n=Decimal("6"), pmt=Decimal("-100"))
        
        self.myAssertEquals(Decimal("150"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), fv=Decimal("100"), n=Decimal("5"), pmt=Decimal("-50"))
        
        self.myAssertEquals(Decimal("150"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), fv=Decimal("100"), n=Decimal("-5"), pmt=Decimal("50"))
        
        self.myAssertEquals(Decimal("-350"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), fv=Decimal("100"), n=Decimal("5"), pmt=Decimal("50"))
        
        #Testing three values
        self.myAssertEquals(Decimal("-165.734150"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("10"), fv=Decimal("50"), n=Decimal("-6"), pmt=Decimal("-10"))
        
        self.myAssertEquals(Decimal("426.028"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("3.5"), fv=Decimal("-550"), n=Decimal("3"), pmt=Decimal("25"))
        
        self.myAssertEquals(Decimal("-531.468"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("-3.5"), fv=Decimal("550"), n=Decimal("3"), pmt=Decimal("-25"))
        
        self.myAssertEquals(Decimal("-333.2"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("-10"), fv=Decimal("550"), n=Decimal("-3"), pmt=Decimal("25"))
        
               
        #>> BEGIN MODE
        #Testing one value
        self.myAssertEquals(Decimal("0"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), fv=Decimal("0"), n=Decimal("0"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("0"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), fv=Decimal("0"), n=Decimal("0"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("-10"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), fv=Decimal("10"), n=Decimal("0"), pmt=Decimal("0"))

        self.myAssertEquals(Decimal("0"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), fv=Decimal("0"), n=Decimal("-20.50"), pmt=Decimal("0"))

        self.myAssertEquals(Decimal("0"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), fv=Decimal("0"), n=Decimal("10"), pmt=Decimal("0"))

        self.myAssertEquals(Decimal("0"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), fv=Decimal("0"), n=Decimal("-10"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("0"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), fv=Decimal("0"), n=Decimal("0"), pmt=Decimal("10"))
       
        self.myAssertEquals(Decimal("0"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), fv=Decimal("0"), n=Decimal("0"), pmt=Decimal("-10"))
        
        #Testing two values
        self.myAssertEquals(Decimal("20"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), fv=Decimal("-20"), n=Decimal("0"), pmt=Decimal("0"))

        self.myAssertEquals(Decimal("-20"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("-10"), fv=Decimal("20"), n=Decimal("0"), pmt=Decimal("0"))

        self.myAssertEquals(Decimal("0"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("-10"), fv=Decimal("0"), n=Decimal("5"), pmt=Decimal("0"))

        self.myAssertEquals(Decimal("0"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("-10"), fv=Decimal("0"), n=Decimal("0"), pmt=Decimal("50"))

        self.myAssertEquals(Decimal("20"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), fv=Decimal("-20"), n=Decimal("2"), pmt=Decimal("0"))

        self.myAssertEquals(Decimal("-20"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), fv=Decimal("20"), n=Decimal("-2"), pmt=Decimal("0"))

        self.myAssertEquals(Decimal("20"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), fv=Decimal("-20"), n=Decimal("0"), pmt=Decimal("100"))

        self.myAssertEquals(Decimal("-20"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), fv=Decimal("20"), n=Decimal("0"), pmt=Decimal("50"))

        self.myAssertEquals(Decimal("600"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), fv=Decimal("0"), n=Decimal("-6"), pmt=Decimal("100"))

        self.myAssertEquals(Decimal("-600"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), fv=Decimal("0"), n=Decimal("-6"), pmt=Decimal("-100"))

        self.myAssertEquals(Decimal("250"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), fv=Decimal("0"), n=Decimal("5"), pmt=Decimal("-50"))
        
        #Testing three values
        self.myAssertEquals(Decimal("28.224"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), fv=Decimal("-50"), n=Decimal("6"), pmt=Decimal("0"))

        self.myAssertEquals(Decimal("-88.578"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), fv=Decimal("50"), n=Decimal("-6"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("100"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), fv=Decimal("-100"), n=Decimal("0"), pmt=Decimal("-50"))
        
        self.myAssertEquals(Decimal("-100"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("-10"), fv=Decimal("100"), n=Decimal("0"), pmt=Decimal("-50"))
        
        self.myAssertEquals(Decimal("-848.717"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), fv=Decimal("0"), n=Decimal("-6"), pmt=Decimal("-100"))
        
        self.myAssertEquals(Decimal("793.509"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("-10"), fv=Decimal("0"), n=Decimal("6"), pmt=Decimal("-100"))
        
        self.myAssertEquals(Decimal("150"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), fv=Decimal("100"), n=Decimal("5"), pmt=Decimal("-50"))
        
        self.myAssertEquals(Decimal("150"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), fv=Decimal("100"), n=Decimal("-5"), pmt=Decimal("50"))
        
        self.myAssertEquals(Decimal("-350"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), fv=Decimal("100"), n=Decimal("5"), pmt=Decimal("50"))
        
        #Testing four values
        self.myAssertEquals(Decimal("423.576"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("3.5"), fv=Decimal("-550"), n=Decimal("3"), pmt=Decimal("25"))
             
        self.myAssertEquals(Decimal("-339.975"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("-10"), fv=Decimal("550"), n=Decimal("-3"), pmt=Decimal("25"))
                
       
        ### Other tests
        
        self.myAssertEquals(Decimal("24766.9979"), presentValue, PAYMENT_TYPE_END, 
                            Decimal("3.98"), Decimal("0"), Decimal("18"), Decimal("-1953.2486"))
        
        #Scenario with the four variables
        self.myAssertEquals(Decimal("29999.9795"), presentValue, PAYMENT_TYPE_END, 
                            Decimal("5"), Decimal("0.000002080"), Decimal("6"), Decimal("-5910.52"))
        
        self.myAssertEquals(Decimal("60.0000003"), presentValue, PAYMENT_TYPE_END, 
                 i=Decimal("19.58131745"), fv=Decimal("-500"), n=Decimal("9"), pmt=Decimal("9.790658"))
        
        
        #Scenario with payment mode in the beggining of the month    
        self.myAssertEquals(Decimal("52.167477"), presentValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("19.58131745"), fv=Decimal("-500"), n=Decimal("9"), pmt=Decimal("9.790658"))
   
    def testFutureValue(self):
       
        #END MODE 
        self.myAssertEquals(Decimal("0"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("0"), n=Decimal("0"), pmt=Decimal("0"))
                
        #One value
        self.myAssertEquals(Decimal("0"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("10"), pv=Decimal("0"), n=Decimal("0"), pmt=Decimal("0"))
                
        self.myAssertEquals(Decimal("0"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("-10"), pv=Decimal("0"), n=Decimal("0"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("-50"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("50"), n=Decimal("0"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("50"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("-50"), n=Decimal("0"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("0"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("0"), n=Decimal("2"), pmt=Decimal("0"))
                
        self.myAssertEquals(Decimal("0"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("0"), n=Decimal("-2"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("0"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("0"), n=Decimal("0"), pmt=Decimal("50"))
        
        self.myAssertEquals(Decimal("50"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("-50"), n=Decimal("0"), pmt=Decimal("-50"))
               
        #Two values
        self.myAssertEquals(Decimal("-50"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("10"), pv=Decimal("50"), n=Decimal("0"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("-50"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("-10"), pv=Decimal("50"), n=Decimal("0"), pmt=Decimal("0"))
            
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", futureValue, PAYMENT_TYPE_END, 
                            i=Decimal("-110"), pv=Decimal("50"), n=Decimal("0"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("0"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("-10"), pv=Decimal("0"), n=Decimal("2"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("0"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("10"), pv=Decimal("0"), n=Decimal("-2"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("0"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("10"), pv=Decimal("0"), n=Decimal("0"), pmt=Decimal("5"))
        
        self.myAssertEquals(Decimal("-50"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("10"), pv=Decimal("50"), n=Decimal("0"), pmt=Decimal("-5"))
        
        self.myAssertEquals(Decimal("-30"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("30"), n=Decimal("2"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("-30"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("30"), n=Decimal("-2"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("-30"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("30"), n=Decimal("0"), pmt=Decimal("10"))
        
        self.myAssertEquals(Decimal("-10"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("30"), n=Decimal("2"), pmt=Decimal("-10"))
        
        self.myAssertEquals(Decimal("100"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("0"), n=Decimal("10"), pmt=Decimal("-10"))
        
        self.myAssertEquals(Decimal("100"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("0"), n=Decimal("-10"), pmt=Decimal("10"))
                
        #Three values
        self.myAssertEquals(Decimal("-36.3"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("10"), pv=Decimal("30"), n=Decimal("2"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("24.793"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("10"), pv=Decimal("-30"), n=Decimal("-2"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("30"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("10"), pv=Decimal("-30"), n=Decimal("0"), pmt=Decimal("10"))
        
        self.myAssertEquals(Decimal("-30"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("-10"), pv=Decimal("30"), n=Decimal("0"), pmt=Decimal("-10"))
        
        self.myAssertEquals(Decimal("-10"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("30"), n=Decimal("2"), pmt=Decimal("-10"))
        
        self.myAssertEquals(Decimal("50"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("-30"), n=Decimal("-2"), pmt=Decimal("10"))
        
        self.myAssertEquals(Decimal("17.355"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("10"), pv=Decimal("0"), n=Decimal("-2"), pmt=Decimal("10"))
        
        self.myAssertEquals(Decimal("21"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("10"), pv=Decimal("0"), n=Decimal("2"), pmt=Decimal("-10"))
             
        #Four values
        self.myAssertEquals(Decimal("-9.25"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("10"), pv=Decimal("25"), n=Decimal("2"), pmt=Decimal("-10"))
        
        self.myAssertEquals(Decimal("-1.25"), futureValue, PAYMENT_TYPE_END,
        i=Decimal("-10"), pv=Decimal("25"), n=Decimal("2"), pmt=Decimal("-10"))
        
        self.myAssertEquals(Decimal("38.017"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("10"), pv=Decimal("-25"), n=Decimal("-2"), pmt=Decimal("10"))
        
        self.myAssertEquals(Decimal("1.25"), futureValue, PAYMENT_TYPE_END, 
                 i=Decimal("-10"), pv=Decimal("-25"), n=Decimal("2"), pmt=Decimal("10"))
        
       
        #BEG MODE 
        self.myAssertEquals(Decimal("0"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("0"), n=Decimal("0"), pmt=Decimal("0"))
               
        #One value
        self.myAssertEquals(Decimal("0"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), pv=Decimal("0"), n=Decimal("0"), pmt=Decimal("0"))
       
        self.myAssertEquals(Decimal("0"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("-10"), pv=Decimal("0"), n=Decimal("0"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("-50"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("50"), n=Decimal("0"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("50"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("-50"), n=Decimal("0"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("0"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("0"), n=Decimal("2"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("0"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("0"), n=Decimal("-2"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("0"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("0"), n=Decimal("0"), pmt=Decimal("50"))
        
        self.myAssertEquals(Decimal("0"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("0"), n=Decimal("0"), pmt=Decimal("-50"))
               
        #Two values
        self.myAssertEquals(Decimal("-50"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), pv=Decimal("50"), n=Decimal("0"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("-50"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), pv=Decimal("50"), n=Decimal("0"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("0"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("-10"), pv=Decimal("0"), n=Decimal("2"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("0"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), pv=Decimal("0"), n=Decimal("-2"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("0"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), pv=Decimal("0"), n=Decimal("0"), pmt=Decimal("5"))
        
        self.myAssertEquals(Decimal("0"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), pv=Decimal("0"), n=Decimal("0"), pmt=Decimal("-5"))
        
        self.myAssertEquals(Decimal("-30"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("30"), n=Decimal("2"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("-30"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("30"), n=Decimal("-2"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("-30"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("30"), n=Decimal("0"), pmt=Decimal("10"))
        
        self.myAssertEquals(Decimal("-30"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("30"), n=Decimal("0"), pmt=Decimal("-10"))
        
        self.myAssertEquals(Decimal("100"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("0"), n=Decimal("10"), pmt=Decimal("-10"))
        
        self.myAssertEquals(Decimal("100"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("0"), n=Decimal("-10"), pmt=Decimal("10"))
                
        #Three values
        self.myAssertEquals(Decimal("-36.3"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), pv=Decimal("30"), n=Decimal("2"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("24.793388"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), pv=Decimal("-30"), n=Decimal("-2"), pmt=Decimal("0"))
        
        self.myAssertEquals(Decimal("30"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), pv=Decimal("-30"), n=Decimal("0"), pmt=Decimal("10"))
        
        self.myAssertEquals(Decimal("-30"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("-10"), pv=Decimal("30"), n=Decimal("0"), pmt=Decimal("-10"))
        
        self.myAssertEquals(Decimal("-10"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("30"), n=Decimal("2"), pmt=Decimal("-10"))
        
        self.myAssertEquals(Decimal("50"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("-30"), n=Decimal("-2"), pmt=Decimal("10"))
        
        self.myAssertEquals(Decimal("19.090909"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), pv=Decimal("0"), n=Decimal("-2"), pmt=Decimal("10"))
        
        self.myAssertEquals(Decimal("23.1"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), pv=Decimal("0"), n=Decimal("2"), pmt=Decimal("-10"))
             
        #Four values
        self.myAssertEquals(Decimal("-7.15"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), pv=Decimal("25"), n=Decimal("2"), pmt=Decimal("-10"))
        
        self.myAssertEquals(Decimal("-3.15"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("-10"), pv=Decimal("25"), n=Decimal("2"), pmt=Decimal("-10"))
        
        self.myAssertEquals(Decimal("39.752066"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), pv=Decimal("-25"), n=Decimal("-2"), pmt=Decimal("10"))
        
        self.myAssertEquals(Decimal("3.15"), futureValue, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("-10"), pv=Decimal("-25"), n=Decimal("2"), pmt=Decimal("10"))
       
    
    def testPayment(self):
        
        #END MODE 
        self.myAssertEquals(Decimal("0"), payment, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("0"), n=Decimal("0"), fv=Decimal("0"))
        
        #One value
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_END, i=Decimal("10"), 
                            pv=Decimal("0"), n=Decimal("0"), fv=Decimal("0"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_END, i=Decimal("-10"), 
                            pv=Decimal("0"), n=Decimal("0"), fv=Decimal("0"))
         
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_END, i=Decimal("0"), 
                            pv=Decimal("50"), n=Decimal("0"), fv=Decimal("0"))      
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_END, i=Decimal("0"), 
                            pv=Decimal("-50"), n=Decimal("0"), fv=Decimal("0"))
        
        self.myAssertEquals(Decimal("0"), payment, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("0"), n=Decimal("2"), fv=Decimal("0"))
        
        self.myAssertEquals(Decimal("0"), payment, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("0"), n=Decimal("-2"), fv=Decimal("0"))
          
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_END, i=Decimal("0"), 
                            pv=Decimal("0"), n=Decimal("0"), fv=Decimal("50"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_END, i=Decimal("0"), 
                            pv=Decimal("0"), n=Decimal("0"), fv=Decimal("-50"))
       
        #Two values
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_END, i=Decimal("10"), 
                            pv=Decimal("50"), n=Decimal("0"), fv=Decimal("0"))

        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_END, i=Decimal("-10"), 
                            pv=Decimal("50"), n=Decimal("0"), fv=Decimal("0"))
        
        self.myAssertEquals(Decimal("0"), payment, PAYMENT_TYPE_END, 
                 i=Decimal("-10"), pv=Decimal("0"), n=Decimal("2"), fv=Decimal("0"))
        
        self.myAssertEquals(Decimal("0"), payment, PAYMENT_TYPE_END, 
                 i=Decimal("10"), pv=Decimal("0"), n=Decimal("-2"), fv=Decimal("0"))

        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_END, i=Decimal("10"), 
                            pv=Decimal("0"), n=Decimal("0"), fv=Decimal("5"))

        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_END, i=Decimal("10"), 
                            pv=Decimal("0"), n=Decimal("0"), fv=Decimal("-5"))
        
        self.myAssertEquals(Decimal("-15"), payment, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("30"), n=Decimal("2"), fv=Decimal("0"))
        
        self.myAssertEquals(Decimal("15"), payment, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("30"), n=Decimal("-2"), fv=Decimal("0"))
              
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_END, i=Decimal("0"), 
                            pv=Decimal("30"), n=Decimal("0"), fv=Decimal("10"))

        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_END, i=Decimal("0"), 
                            pv=Decimal("30"), n=Decimal("0"), fv=Decimal("-10"))

        self.myAssertEquals(Decimal("1"), payment, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("0"), n=Decimal("10"), fv=Decimal("-10"))
        
        self.myAssertEquals(Decimal("1"), payment, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("0"), n=Decimal("-10"), fv=Decimal("10"))
                
        #Three values
        self.myAssertEquals(Decimal("-17.285714"), payment, PAYMENT_TYPE_END, 
                 i=Decimal("10"), pv=Decimal("30"), n=Decimal("2"), fv=Decimal("0"))
        
        self.myAssertEquals(Decimal("-14.285714"), payment, PAYMENT_TYPE_END, 
                 i=Decimal("10"), pv=Decimal("-30"), n=Decimal("-2"), fv=Decimal("0"))
               
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_END, i=Decimal("-110"), 
                            pv=Decimal("-30"), n=Decimal("-2"), fv=Decimal("0"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_END, i=Decimal("10"), 
                            pv=Decimal("-30"), n=Decimal("0"), fv=Decimal("10"))

        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_END, i=Decimal("-10"), 
                            pv=Decimal("30"), n=Decimal("0"), fv=Decimal("-10"))
        
        self.myAssertEquals(Decimal("-10"), payment, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("30"), n=Decimal("2"), fv=Decimal("-10"))
        
        self.myAssertEquals(Decimal("10"), payment, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("-30"), n=Decimal("2"), fv=Decimal("10"))
        
        self.myAssertEquals(Decimal("20"), payment, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("-30"), n=Decimal("2"), fv=Decimal("-10"))
        
        self.myAssertEquals(Decimal("-20"), payment, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("30"), n=Decimal("2"), fv=Decimal("10"))
        
        self.myAssertEquals(Decimal("10"), payment, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("30"), n=Decimal("-2"), fv=Decimal("-10"))                        

        self.myAssertEquals(Decimal("-10"), payment, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("-30"), n=Decimal("-2"), fv=Decimal("10"))
        
        self.myAssertEquals(Decimal("-20"), payment, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("-30"), n=Decimal("-2"), fv=Decimal("-10"))
        
        self.myAssertEquals(Decimal("20"), payment, PAYMENT_TYPE_END, 
                 i=Decimal("0"), pv=Decimal("30"), n=Decimal("-2"), fv=Decimal("10"))                
        
        self.myAssertEquals(Decimal("5.761905"), payment, PAYMENT_TYPE_END, 
                 i=Decimal("10"), pv=Decimal("0"), n=Decimal("-2"), fv=Decimal("10"))
        
        self.myAssertEquals(Decimal("4.761905"), payment, PAYMENT_TYPE_END, 
                 i=Decimal("10"), pv=Decimal("0"), n=Decimal("2"), fv=Decimal("-10"))
              
        #Four values
        self.myAssertEquals(Decimal("-9.642857"), payment, PAYMENT_TYPE_END, 
                 i=Decimal("10"), pv=Decimal("25"), n=Decimal("2"), fv=Decimal("-10"))
        
        self.myAssertEquals(Decimal("-5.394737"), payment, PAYMENT_TYPE_END, 
                 i=Decimal("-10"), pv=Decimal("25"), n=Decimal("2"), fv=Decimal("-10"))
        
        self.myAssertEquals(Decimal("-6.142857"), payment, PAYMENT_TYPE_END, 
                 i=Decimal("10"), pv=Decimal("-25"), n=Decimal("-2"), fv=Decimal("10"))
        
        self.myAssertEquals(Decimal("5.394737"), payment, PAYMENT_TYPE_END, 
                 i=Decimal("-10"), pv=Decimal("-25"), n=Decimal("2"), fv=Decimal("10"))
              
        #BEG MODE
        self.myAssertEquals(Decimal("0"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("0"), n=Decimal("0"), fv=Decimal("0"))
                
        #One value
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_BEGINNING, i=Decimal("10"), 
                            pv=Decimal("0"), n=Decimal("0"), fv=Decimal("0"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_BEGINNING, i=Decimal("-10"), 
                            pv=Decimal("0"), n=Decimal("0"), fv=Decimal("0"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_BEGINNING, i=Decimal("0"), 
                            pv=Decimal("50"), n=Decimal("0"), fv=Decimal("0"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_BEGINNING, i=Decimal("0"), 
                            pv=Decimal("-50"), n=Decimal("0"), fv=Decimal("0"))
        
        self.myAssertEquals(Decimal("0"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("0"), n=Decimal("2"), fv=Decimal("0"))
        
        self.myAssertEquals(Decimal("0"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("0"), n=Decimal("-2"), fv=Decimal("0"))
               
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_BEGINNING, i=Decimal("0"), 
                            pv=Decimal("0"), n=Decimal("0"), fv=Decimal("50"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_BEGINNING, i=Decimal("0"), 
                            pv=Decimal("0"), n=Decimal("0"), fv=Decimal("-50"))
        
        #Two values
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_BEGINNING, i=Decimal("10"), 
                            pv=Decimal("50"), n=Decimal("0"), fv=Decimal("0"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_BEGINNING, i=Decimal("-10"), 
                            pv=Decimal("50"), n=Decimal("0"), fv=Decimal("0"))
        
        self.myAssertEquals(Decimal("0"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("-10"), pv=Decimal("0"), n=Decimal("2"), fv=Decimal("0"))
        
        self.myAssertEquals(Decimal("0"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), pv=Decimal("0"), n=Decimal("-2"), fv=Decimal("0"))
               
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_BEGINNING, i=Decimal("10"), 
                            pv=Decimal("0"), n=Decimal("0"), fv=Decimal("5"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_BEGINNING, i=Decimal("10"), 
                            pv=Decimal("0"), n=Decimal("0"), fv=Decimal("-5"))
        
        self.myAssertEquals(Decimal("-15"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("30"), n=Decimal("2"), fv=Decimal("0"))
        
        self.myAssertEquals(Decimal("15"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("30"), n=Decimal("-2"), fv=Decimal("0"))
                
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_BEGINNING, i=Decimal("0"), 
                            pv=Decimal("30"), n=Decimal("0"), fv=Decimal("10"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_BEGINNING, i=Decimal("0"), 
                            pv=Decimal("30"), n=Decimal("0"), fv=Decimal("-10"))
        
        self.myAssertEquals(Decimal("1"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("0"), n=Decimal("10"), fv=Decimal("-10"))
        
        self.myAssertEquals(Decimal("1"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("0"), n=Decimal("-10"), fv=Decimal("10"))
                
        #Three values
        self.myAssertEquals(Decimal("-15.714286"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), pv=Decimal("30"), n=Decimal("2"), fv=Decimal("0"))
        
        self.myAssertEquals(Decimal("-12.987013"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), pv=Decimal("-30"), n=Decimal("-2"), fv=Decimal("0"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_BEGINNING, i=Decimal("10"), 
                            pv=Decimal("-30"), n=Decimal("0"), fv=Decimal("10"))
        
        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", payment, PAYMENT_TYPE_BEGINNING, i=Decimal("-10"), 
                            pv=Decimal("30"), n=Decimal("0"), fv=Decimal("-10"))
        
        self.myAssertEquals(Decimal("-10"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("30"), n=Decimal("2"), fv=Decimal("-10"))
        
        self.myAssertEquals(Decimal("10"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("-30"), n=Decimal("2"), fv=Decimal("10"))
        
        self.myAssertEquals(Decimal("20"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("-30"), n=Decimal("2"), fv=Decimal("-10"))
        
        self.myAssertEquals(Decimal("-20"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("30"), n=Decimal("2"), fv=Decimal("10"))
        
        self.myAssertEquals(Decimal("10"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("30"), n=Decimal("-2"), fv=Decimal("-10"))                        

        self.myAssertEquals(Decimal("-10"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("-30"), n=Decimal("-2"), fv=Decimal("10"))
        
        self.myAssertEquals(Decimal("-20"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("-30"), n=Decimal("-2"), fv=Decimal("-10"))
        
        self.myAssertEquals(Decimal("20"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("30"), n=Decimal("-2"), fv=Decimal("10"))                
        
        self.myAssertEquals(Decimal("5.238095"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), pv=Decimal("0"), n=Decimal("-2"), fv=Decimal("10"))
        
        self.myAssertEquals(Decimal("4.329004"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), pv=Decimal("0"), n=Decimal("2"), fv=Decimal("-10"))
               
        #Four values
        self.myAssertEquals(Decimal("-8.766234"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), pv=Decimal("25"), n=Decimal("2"), fv=Decimal("-10"))
        
        self.myAssertEquals(Decimal("-5.994152"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("-10"), pv=Decimal("25"), n=Decimal("2"), fv=Decimal("-10"))
        
        self.myAssertEquals(Decimal("-5.584416"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("10"), pv=Decimal("-25"), n=Decimal("-2"), fv=Decimal("10"))
        
        self.myAssertEquals(Decimal("17.690058"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("-10"), pv=Decimal("-25"), n=Decimal("2"), fv=Decimal("-10"))
                
        
        #Scenario with only some variables 

        self.myAssertEquals(Decimal("1884.205838"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("3.95"), pv=Decimal("-24895.9738"), n=Decimal("18"), fv=Decimal("0"))
        
        self.myAssertEquals(Decimal("-834.03"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("0"), pv=Decimal("-10000"), n=Decimal("12"), fv=Decimal("20008.36"))
        
        self.myAssertEquals(Decimal("4410.524043"), payment, PAYMENT_TYPE_END, 
                 i=Decimal("5"), pv=Decimal("0.000002080"), n=Decimal("6"), fv=Decimal("-30000"))    

        self.myAssertEquals(Decimal("-49.115321"), payment, PAYMENT_TYPE_END, 
                 i=Decimal("19"), pv=Decimal("100"), n=Decimal("9"), fv=Decimal("500"))        

        self.myAssertEquals(Decimal("5629.070517"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("5"), pv=Decimal("-30000"), n=Decimal("6"), fv=Decimal("0.000002080"))

        self.myAssertEquals(Decimal("-41.273379"), payment, PAYMENT_TYPE_BEGINNING, 
                 i=Decimal("19"), pv=Decimal("100"), n=Decimal("9"), fv=Decimal("500"))        

    
#    def testInterestRate(self): 
#        
#        # END MODE 
#        self.myAssertEquals(Decimal("0"), interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("0"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("0"))
#        
#        #Testing one value
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("10"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("0"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("-10"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("0"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("0"), fv=Decimal("100"), pv=Decimal("0"), pmt=Decimal("0"))
#
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("0"), fv=Decimal("-100"), pv=Decimal("0"), pmt=Decimal("0"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("0"), fv=Decimal("0"), pv=Decimal("50"), pmt=Decimal("0"))
#
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("0"), fv=Decimal("0"), pv=Decimal("-50"), pmt=Decimal("0"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("0"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("70"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("0"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("-70"))
#        
#        #Testing two values
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("10"), fv=Decimal("100"), pv=Decimal("0"), pmt=Decimal("0"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("-10"), fv=Decimal("-100"), pv=Decimal("0"), pmt=Decimal("0"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("-10"), fv=Decimal("0"), pv=Decimal("50"), pmt=Decimal("0"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("10"), fv=Decimal("0"), pv=Decimal("-50"), pmt=Decimal("0"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("10"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("100"))
#                
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("10"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("-100"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("0"), fv=Decimal("10"), pv=Decimal("50"), pmt=Decimal("0"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("0"), fv=Decimal("10"), pv=Decimal("-50"), pmt=Decimal("0"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("0"), fv=Decimal("10"), pv=Decimal("0"), pmt=Decimal("5"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("0"), fv=Decimal("-10"), pv=Decimal("0"), pmt=Decimal("5"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("0"), fv=Decimal("0"), pv=Decimal("50"), pmt=Decimal("5"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("0"), fv=Decimal("0"), pv=Decimal("50"), pmt=Decimal("-10"))
#        
#        #Three values
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("10"), fv=Decimal("50"), pv=Decimal("10"), pmt=Decimal("0"))
#        
#        self.myAssertEquals(Decimal("17.461894"), interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("10"), fv=Decimal("50"), pv=Decimal("-10"), pmt=Decimal("0"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("10"), fv=Decimal("50"), pv=Decimal("0"), pmt=Decimal("10"))
#                
#        self.myAssertEquals(Decimal("-16.834268"), interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("10"), fv=Decimal("50"), pv=Decimal("0"), pmt=Decimal("-10"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("10"), fv=Decimal("0"), pv=Decimal("-10"), pmt=Decimal("-10"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("-10"), fv=Decimal("0"), pv=Decimal("10"), pmt=Decimal("-10"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("0"), fv=Decimal("50"), pv=Decimal("10"), pmt=Decimal("-10"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("0"), fv=Decimal("50"), pv=Decimal("-10"), pmt=Decimal("-10"))
#        
#        #Four values
#        self.myAssertEquals(Decimal("-7.348064"), interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("5"), fv=Decimal("50"), pv=Decimal("-10"), pmt=Decimal("-10"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("-5"), fv=Decimal("50"), pv=Decimal("-10"), pmt=Decimal("2"))
#                
#        #>> BEG MODE
#        self.myAssertEquals(Decimal("0"), interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("0"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("0"))
#        
#        #Testing one value
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("10"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("0"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("-10"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("0"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("0"), fv=Decimal("100"), pv=Decimal("0"), pmt=Decimal("0"))
#
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("0"), fv=Decimal("-100"), pv=Decimal("0"), pmt=Decimal("0"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("0"), fv=Decimal("0"), pv=Decimal("50"), pmt=Decimal("0"))
#
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("0"), fv=Decimal("0"), pv=Decimal("-50"), pmt=Decimal("0"))
#
#        self.myAssertEquals(Decimal("0"), interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("0"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("70"))
#
#        self.myAssertEquals(Decimal("0"), interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("0"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("-70"))
#        
#        #Testing two values
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("10"), fv=Decimal("100"), pv=Decimal("0"), pmt=Decimal("0"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("-10"), fv=Decimal("-100"), pv=Decimal("0"), pmt=Decimal("0"))
#                
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("-10"), fv=Decimal("0"), pv=Decimal("50"), pmt=Decimal("0"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("10"), fv=Decimal("0"), pv=Decimal("-50"), pmt=Decimal("0"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("10"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("100"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("10"), fv=Decimal("0"), pv=Decimal("0"), pmt=Decimal("-100"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("0"), fv=Decimal("10"), pv=Decimal("50"), pmt=Decimal("0"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("0"), fv=Decimal("10"), pv=Decimal("-50"), pmt=Decimal("0"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("0"), fv=Decimal("10"), pv=Decimal("0"), pmt=Decimal("5"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("0"), fv=Decimal("-10"), pv=Decimal("0"), pmt=Decimal("5"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("0"), fv=Decimal("0"), pv=Decimal("50"), pmt=Decimal("5"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("0"), fv=Decimal("0"), pv=Decimal("50"), pmt=Decimal("-10"))
#        
#        #Three values
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("10"), fv=Decimal("50"), pv=Decimal("10"), pmt=Decimal("0"))
#        
#        self.myAssertEquals(Decimal("17.461894"), interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("10"), fv=Decimal("50"), pv=Decimal("-10"), pmt=Decimal("0"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("10"), fv=Decimal("50"), pv=Decimal("0"), pmt=Decimal("10"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("10"), fv=Decimal("50"), pv=Decimal("0"), pmt=Decimal("-10"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("10"), fv=Decimal("0"), pv=Decimal("-10"), pmt=Decimal("-10"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("-10"), fv=Decimal("0"), pv=Decimal("10"), pmt=Decimal("-10"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("0"), fv=Decimal("50"), pv=Decimal("10"), pmt=Decimal("-10"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("0"), fv=Decimal("50"), pv=Decimal("-10"), pmt=Decimal("-10"))
#        
#        #Four values
#        self.myAssertEquals(Decimal("-5.421431"), interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("5"), fv=Decimal("50"), pv=Decimal("-10"), pmt=Decimal("-10"))
#        
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("-5"), fv=Decimal("50"), pv=Decimal("-10"), pmt=Decimal("2"))
#                 
#                 
#        #Scenario with only some variables
#        self.myAssertEquals(Decimal("3.950232"), interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("18"), fv=Decimal("50000"), pv=Decimal("-24895.9738"), pmt=Decimal("0"))
#
#        self.myAssertEquals(Decimal("7.550141"), interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("18"), fv=Decimal("50000"), pv=Decimal("0"), pmt=Decimal("-1394.668122"))
#       
#        self.myAssertRaises(PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT).", interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("18"), fv=Decimal("0"), pv=Decimal("-24895.9738"), pmt=Decimal("-1394.668122"))
#
#        self.myAssertEquals(Decimal("28.361354"), interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("12"), fv=Decimal("20008.36"), pv=Decimal("-1000"), pmt=Decimal("0"))    
#               
#        self.myAssertEquals(Decimal("2.841596e11"), interestRate, PAYMENT_TYPE_END, 
#                            n=Decimal("6"), fv=Decimal("-30000"), pv=Decimal("0.000002080"), pmt=Decimal("-5910.52"))
#        
#        self.myAssertEquals(Decimal("-100"), interestRate, PAYMENT_TYPE_BEGINNING, 
#                            n=Decimal("6"), fv=Decimal("0.000002080"), pv=Decimal("-30000"), pmt=Decimal("-5910.52"))
    
    def testFrenchAmortizationCalculation(self):
        """ This function will verify if the calculation of the amortization in the 
        French system with PRICE payment is being done correctly """
        
        #First scenario
        amortizationPlan = frenchAmortization(Decimal('600') , Decimal('10'), Decimal('3'))
        assert amortizationPlan != None
        assert len(amortizationPlan) == 4
        
        assert amortizationPlan == [[Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('600')],
                                     [Decimal('241.2688821752265861027190333'), Decimal('60.0000000000000000000000000'), Decimal('60.0000000000000000000000000'), Decimal('181.2688821752265861027190333'), Decimal('181.2688821752265861027190333'), Decimal('418.7311178247734138972809667')],
                                      [Decimal('241.2688821752265861027190333'), Decimal('41.8731117824773413897280967'), Decimal('101.8731117824773413897280967'), Decimal('199.3957703927492447129909366'), Decimal('380.6646525679758308157099699'), Decimal('219.3353474320241691842900301')],
                                       [Decimal('241.2688821752265861027190333'), Decimal('21.9335347432024169184290030'), Decimal('123.8066465256797583081570997'), Decimal('219.3353474320241691842900303'), Decimal('600.0000000000000000000000002'), Decimal('0')]]
        
        #Second scenario
        amortizationPlan = frenchAmortization(Decimal('8530.20'), Decimal('3'), Decimal('10'))
        assert amortizationPlan != None
        assert len(amortizationPlan) == 11
        assert amortizationPlan == [[Decimal("0"), Decimal("0"), Decimal("0"), Decimal("0"), Decimal("0"), Decimal("8530.20")],
          [Decimal("999.9996674433323750915424559"), Decimal("255.9060000000000000000000000"), Decimal("255.9060000000000000000000000"), Decimal("744.0936674433323750915424559"), Decimal("744.0936674433323750915424559"), Decimal("7786.106332556667624908457544")],
           [Decimal("999.9996674433323750915424559"), Decimal("233.5831899767000287472537263"), Decimal("489.4891899767000287472537263"), Decimal("766.4164774666323463442887296"), Decimal("1510.510144909964721435831186"), Decimal("7019.689855090035278564168814")],
            [Decimal("999.9996674433323750915424559"), Decimal("210.5906956527010583569250644"), Decimal("700.0798856294010871041787907"), Decimal("789.4089717906313167346173915"), Decimal("2299.919116700596038170448578"), Decimal("6230.280883299403961829551422")],
             [Decimal("999.9996674433323750915424559"), Decimal("186.9084264989821188548865427"), Decimal("886.9883121283832059590653334"), Decimal("813.0912409443502562366559132"), Decimal("3113.010357644946294407104491"), Decimal("5417.189642355053705592895509")], 
             [Decimal("999.9996674433323750915424559"), Decimal("162.5156892706516111677868653"), Decimal("1049.504001399034817126852199"), Decimal("837.4839781726807639237555906"), Decimal("3950.494335817627058330860082"), Decimal("4579.705664182372941669139918")], 
             [Decimal("999.9996674433323750915424559"), Decimal("137.3911699254711882500741976"), Decimal("1186.895171324506005376926397"), Decimal("862.6084975178611868414682583"), Decimal("4813.102833335488245172328340"), Decimal("3717.097166664511754827671660")],
              [Decimal("999.9996674433323750915424559"), Decimal("111.5129149999353526448301498"), Decimal("1298.408086324441358021756547"), Decimal("888.4867524433970224467123061"), Decimal("5701.589585778885267619040646"), Decimal("2828.610414221114732380959354")], 
              [Decimal("999.9996674433323750915424559"), Decimal("84.8583124266334419714287806"), Decimal("1383.266398751074799993185328"), Decimal("915.1413550166989331201136753"), Decimal("6616.730940795584200739154321"), Decimal("1913.469059204415799260845679")], 
              [Decimal("999.9996674433323750915424559"), Decimal("57.4040717761324739778253704"), Decimal("1440.670470527207273971010698"), Decimal("942.5955956671999011137170855"), Decimal("7559.326536462784101852871406"), Decimal("970.8734635372158981471285935")], 
              [Decimal("999.9996674433323750915424559"), Decimal("29.1262039061164769444138578"), Decimal("1469.796674433323750915424556"), Decimal("970.8734635372158981471285981"), Decimal("8530.200000000000000000000004"), Decimal("0")]]
        
        #Testing invalid situations
        try:
            amortizationPlan = frenchAmortization(Decimal('0'), Decimal('3'), Decimal('10'))
        except PyFinancialLibraryException:
            pass
        else:
            self.fail("Some values for calculating amortization have not been provided.")
        
        try:
            amortizationPlan = frenchAmortization(Decimal('8530.20'), Decimal('0'), Decimal('10'))
        except PyFinancialLibraryException:
            pass
        else:
            self.fail("Some values for calculating amortization have not been provided.")
        
        try:
            amortizationPlan = frenchAmortization(Decimal('8530.20'), Decimal('3'), Decimal('0'))
        except PyFinancialLibraryException:
            pass
        else:
            self.fail("Some values for calculating amortization have not been provided.")
            
        try:
            amortizationPlan = frenchAmortization(None, Decimal('3'), Decimal('10'))
        except PyFinancialLibraryException:
            pass
        else:
            self.fail("Some values for calculating amortization have not been provided.")
            
        try:
            amortizationPlan = frenchAmortization(Decimal('8530.20'), None, Decimal('10'))
        except PyFinancialLibraryException:
            pass
        else:
            self.fail("Some values for calculating amortization have not been provided.")    
            
        try:
            amortizationPlan = frenchAmortization(Decimal('8530.20'), Decimal('3'), None)
        except PyFinancialLibraryException:
            pass
        else:
            self.fail("Some values for calculating amortization have not been provided.")
    
    def testEqualsAmortizationCalculation(self):
        """ This function will verify if the calculation of the amortization in the 
        equals system is being done correctly"""
        
        #First scenario
        amortizationPlan = equalsAmortization(Decimal('600') , Decimal('10'), Decimal('3'))
        assert amortizationPlan != None
        assert len(amortizationPlan) == 4
        assert amortizationPlan == [[Decimal("0"), Decimal("0"), Decimal("0"), Decimal("0"), Decimal("0"), Decimal("600")], 
         [Decimal("260.0"), Decimal("60.0"), Decimal("60.0"), Decimal("200"), Decimal("200"), Decimal("400")], 
         [Decimal("240.0"), Decimal("40.0"), Decimal("100.0"), Decimal("200"), Decimal("400"), Decimal("200")],
          [Decimal("220.0"), Decimal("20.0"), Decimal("120.0"), Decimal("200"), Decimal("600"), Decimal("0")]]
        
        #Second scenario
        amortizationPlan = equalsAmortization(Decimal('300000.0') , Decimal('4'), Decimal('5'))
        assert amortizationPlan != None
        assert len(amortizationPlan) == 6
        assert amortizationPlan == [[Decimal("0"), Decimal("0"), Decimal("0"), Decimal("0"), Decimal("0"), Decimal("300000.0")],
          [Decimal("72000.000"), Decimal("12000.000"), Decimal("12000.000"), Decimal("60000.0"), Decimal("60000.0"), Decimal("240000.0")],
           [Decimal("69600.000"), Decimal("9600.000"), Decimal("21600.000"), Decimal("60000.0"), Decimal("120000.0"), Decimal("180000.0")],
            [Decimal("67200.000"), Decimal("7200.000"), Decimal("28800.000"), Decimal("60000.0"), Decimal("180000.0"), Decimal("120000.0")],
             [Decimal("64800.000"), Decimal("4800.000"), Decimal("33600.000"), Decimal("60000.0"), Decimal("240000.0"), Decimal("60000.0")],
              [Decimal("62400.000"), Decimal("2400.000"), Decimal("36000.000"), Decimal("60000.0"), Decimal("300000.0"), Decimal("0")]]
        
        #Third scenario
        amortizationPlan = equalsAmortization(Decimal('80000.0') , Decimal('4'), Decimal('40'))
        assert amortizationPlan != None
        assert len(amortizationPlan) == 41
        assert amortizationPlan == [[Decimal("0"), Decimal("0"), Decimal("0"), Decimal("0"), Decimal("0"), Decimal("80000.0")], 
         [Decimal("5200.000"), Decimal("3200.000"), Decimal("3200.000"), Decimal("2000.0"), Decimal("2000.0"), Decimal("78000.0")], 
         [Decimal("5120.000"), Decimal("3120.000"), Decimal("6320.000"), Decimal("2000.0"), Decimal("4000.0"), Decimal("76000.0")], 
         [Decimal("5040.000"), Decimal("3040.000"), Decimal("9360.000"), Decimal("2000.0"), Decimal("6000.0"), Decimal("74000.0")],
          [Decimal("4960.000"), Decimal("2960.000"), Decimal("12320.000"), Decimal("2000.0"), Decimal("8000.0"), Decimal("72000.0")],
           [Decimal("4880.000"), Decimal("2880.000"), Decimal("15200.000"), Decimal("2000.0"), Decimal("10000.0"), Decimal("70000.0")], 
           [Decimal("4800.000"), Decimal("2800.000"), Decimal("18000.000"), Decimal("2000.0"), Decimal("12000.0"), Decimal("68000.0")], 
           [Decimal("4720.000"), Decimal("2720.000"), Decimal("20720.000"), Decimal("2000.0"), Decimal("14000.0"), Decimal("66000.0")],
            [Decimal("4640.000"), Decimal("2640.000"), Decimal("23360.000"), Decimal("2000.0"), Decimal("16000.0"), Decimal("64000.0")], 
            [Decimal("4560.000"), Decimal("2560.000"), Decimal("25920.000"), Decimal("2000.0"), Decimal("18000.0"), Decimal("62000.0")], 
            [Decimal("4480.000"), Decimal("2480.000"), Decimal("28400.000"), Decimal("2000.0"), Decimal("20000.0"), Decimal("60000.0")],
             [Decimal("4400.000"), Decimal("2400.000"), Decimal("30800.000"), Decimal("2000.0"), Decimal("22000.0"), Decimal("58000.0")], 
             [Decimal("4320.000"), Decimal("2320.000"), Decimal("33120.000"), Decimal("2000.0"), Decimal("24000.0"), Decimal("56000.0")], 
             [Decimal("4240.000"), Decimal("2240.000"), Decimal("35360.000"), Decimal("2000.0"), Decimal("26000.0"), Decimal("54000.0")], 
             [Decimal("4160.000"), Decimal("2160.000"), Decimal("37520.000"), Decimal("2000.0"), Decimal("28000.0"), Decimal("52000.0")], 
             [Decimal("4080.000"), Decimal("2080.000"), Decimal("39600.000"), Decimal("2000.0"), Decimal("30000.0"), Decimal("50000.0")], 
             [Decimal("4000.000"), Decimal("2000.000"), Decimal("41600.000"), Decimal("2000.0"), Decimal("32000.0"), Decimal("48000.0")], 
             [Decimal("3920.000"), Decimal("1920.000"), Decimal("43520.000"), Decimal("2000.0"), Decimal("34000.0"), Decimal("46000.0")], 
             [Decimal("3840.000"), Decimal("1840.000"), Decimal("45360.000"), Decimal("2000.0"), Decimal("36000.0"), Decimal("44000.0")], 
             [Decimal("3760.000"), Decimal("1760.000"), Decimal("47120.000"), Decimal("2000.0"), Decimal("38000.0"), Decimal("42000.0")], 
             [Decimal("3680.000"), Decimal("1680.000"), Decimal("48800.000"), Decimal("2000.0"), Decimal("40000.0"), Decimal("40000.0")],
              [Decimal("3600.000"), Decimal("1600.000"), Decimal("50400.000"), Decimal("2000.0"), Decimal("42000.0"), Decimal("38000.0")], 
              [Decimal("3520.000"), Decimal("1520.000"), Decimal("51920.000"), Decimal("2000.0"), Decimal("44000.0"), Decimal("36000.0")], 
              [Decimal("3440.000"), Decimal("1440.000"), Decimal("53360.000"), Decimal("2000.0"), Decimal("46000.0"), Decimal("34000.0")], 
              [Decimal("3360.000"), Decimal("1360.000"), Decimal("54720.000"), Decimal("2000.0"), Decimal("48000.0"), Decimal("32000.0")], 
              [Decimal("3280.000"), Decimal("1280.000"), Decimal("56000.000"), Decimal("2000.0"), Decimal("50000.0"), Decimal("30000.0")], 
              [Decimal("3200.000"), Decimal("1200.000"), Decimal("57200.000"), Decimal("2000.0"), Decimal("52000.0"), Decimal("28000.0")], 
              [Decimal("3120.000"), Decimal("1120.000"), Decimal("58320.000"), Decimal("2000.0"), Decimal("54000.0"), Decimal("26000.0")], 
              [Decimal("3040.000"), Decimal("1040.000"), Decimal("59360.000"), Decimal("2000.0"), Decimal("56000.0"), Decimal("24000.0")],
               [Decimal("2960.000"), Decimal("960.000"), Decimal("60320.000"), Decimal("2000.0"), Decimal("58000.0"), Decimal("22000.0")], 
               [Decimal("2880.000"), Decimal("880.000"), Decimal("61200.000"), Decimal("2000.0"), Decimal("60000.0"), Decimal("20000.0")], 
               [Decimal("2800.000"), Decimal("800.000"), Decimal("62000.000"), Decimal("2000.0"), Decimal("62000.0"), Decimal("18000.0")], 
               [Decimal("2720.000"), Decimal("720.000"), Decimal("62720.000"), Decimal("2000.0"), Decimal("64000.0"), Decimal("16000.0")], 
               [Decimal("2640.000"), Decimal("640.000"), Decimal("63360.000"), Decimal("2000.0"), Decimal("66000.0"), Decimal("14000.0")],
                [Decimal("2560.000"), Decimal("560.000"), Decimal("63920.000"), Decimal("2000.0"), Decimal("68000.0"), Decimal("12000.0")], 
                [Decimal("2480.000"), Decimal("480.000"), Decimal("64400.000"), Decimal("2000.0"), Decimal("70000.0"), Decimal("10000.0")], 
                [Decimal("2400.000"), Decimal("400.000"), Decimal("64800.000"), Decimal("2000.0"), Decimal("72000.0"), Decimal("8000.0")], 
                [Decimal("2320.000"), Decimal("320.000"), Decimal("65120.000"), Decimal("2000.0"), Decimal("74000.0"), Decimal("6000.0")], 
                [Decimal("2240.000"), Decimal("240.000"), Decimal("65360.000"), Decimal("2000.0"), Decimal("76000.0"), Decimal("4000.0")], 
                [Decimal("2160.000"), Decimal("160.000"), Decimal("65520.000"), Decimal("2000.0"), Decimal("78000.0"), Decimal("2000.0")], 
                [Decimal("2080.000"), Decimal("80.000"), Decimal("65600.000"), Decimal("2000.0"), Decimal("80000.0"), Decimal("0")]]
        
        #Testing invalid situations 
        try:
            amortizationPlan = equalsAmortization(Decimal('0'), Decimal('3'), Decimal('10'))
        except PyFinancialLibraryException:
            pass
        else:
            self.fail("Some values for calculating amortization have not been provided.")
        
        try:
            amortizationPlan = equalsAmortization(Decimal('8530.20'), Decimal('0'), Decimal('10'))
        except PyFinancialLibraryException:
            pass
        else:
            self.fail("Some values for calculating amortization have not been provided.")
        
        try:
            amortizationPlan = equalsAmortization(Decimal('8530.20'), Decimal('3'), Decimal('0'))
        except PyFinancialLibraryException:
            pass
        else:
            self.fail("Some values for calculating amortization have not been provided.")
            
        try:
            amortizationPlan = equalsAmortization(None, Decimal('3'), Decimal('10'))
        except PyFinancialLibraryException:
            pass
        else:
            self.fail("Some values for calculating amortization have not been provided.")
            
        try:
            amortizationPlan = equalsAmortization(Decimal('8530.20'), None, Decimal('10'))
        except PyFinancialLibraryException:
            pass
        else:
            self.fail("Some values for calculating amortization have not been provided.")    
            
        try:
            amortizationPlan = equalsAmortization(Decimal('8530.20'), Decimal('3'), None)
        except PyFinancialLibraryException:
            pass
        else:
            self.fail("Some values for calculating amortization have not been provided.")
            
    def testConvertAnualPeriodsToMonthPeriods(self):

        self.myAssertRaises(PyFinancialLibraryException, "Exception expected", convertAnualPeriodsToMonthPeriods, None)
        self.myAssertRaises(PyFinancialLibraryException, "Exception expected", convertAnualPeriodsToMonthPeriods, "a")
        self.myAssertRaises(PyFinancialLibraryException, "Exception expected", convertAnualPeriodsToMonthPeriods, "1.5")
        self.myAssertRaises(PyFinancialLibraryException, "Exception expected", convertAnualPeriodsToMonthPeriods, "-2")
        
        self.myAssertEquals(Decimal("0"), convertAnualPeriodsToMonthPeriods, "0")
        self.myAssertEquals(Decimal("24"), convertAnualPeriodsToMonthPeriods, "2")
    
    def testConvertAnualRateToMonthRates(self):
        
        self.myAssertRaises(PyFinancialLibraryException, "Exception expected", convertAnualRateToMonthRates, None, True)
        self.myAssertRaises(PyFinancialLibraryException, "Exception expected", convertAnualRateToMonthRates, None, False)
        self.myAssertRaises(PyFinancialLibraryException, "Exception expected", convertAnualRateToMonthRates, None)
        
        self.myAssertEquals(Decimal("30"), convertAnualRateToMonthRates, "360", False)
        self.myAssertEquals(Decimal("30"), convertAnualRateToMonthRates, "360")
        self.myAssertEquals(Decimal("0"), convertAnualRateToMonthRates, "0", False)
        self.myAssertEquals(Decimal("7"), convertAnualRateToMonthRates, "84", False)
        self.myAssertEquals(Decimal("42"), convertAnualRateToMonthRates, "504", False)
        self.myAssertEquals(Decimal('7.934843773411037759276511400'), convertAnualRateToMonthRates, "1.5", True)
        