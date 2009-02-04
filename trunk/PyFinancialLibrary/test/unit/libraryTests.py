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
        
        assert add(1, 2) ==  Decimal("3.0")
        assert add(0, 0) == Decimal("0.0")
        assert add(-5, 5) == Decimal("0.0")
        assert add(-0.3, 5) == Decimal("4.7")
        assert add(-0.3, -5) == Decimal("-5.3")
        assert add(-0.2372, 0.0001) == Decimal ("-0.2371")
        assert add(-0.2372, -0.00001) ==  Decimal("-0.23721")
        try:
            add(3, "-5as")           
            self.fail("Expected a ValueError")
        except InvalidOperation:
            pass
        try:
            add(3, "*")           
            self.fail("Expected a ValueError")
        except  InvalidOperation:
            pass            
        try:
            add(3, list())           
            self.fail("Expected a TypeError")
        except  InvalidOperation:
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
        except  InvalidOperation:
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
            self.fail("Expected a ValueError")
        except InvalidOperation:
            pass
        try:
            mult(3, "*")           
            self.fail("Expected a ValueError")
        except  InvalidOperation:
            pass
        try:
            mult(3, list())           
            self.fail("Expected a TypeError")
        except  InvalidOperation:
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
            self.fail("Expected a ValueError")
        except  InvalidOperation:
            pass
        try:
            div(3, "*")           
            self.fail("Expected a ValueError")
        except  InvalidOperation:
            pass
        try:
            div(3, list())           
            self.fail("Expected a TypeError")
        except  InvalidOperation:
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
        assert n != Decimal("0.0")
        self.assertAlmostEquals(Decimal("18.0"), n, TOLERANCE)
        
        n = numberOfPayments(PAYMENT_TYPE_END, 3.95, 0, 10000, -2500.696667)
        assert n != None
        assert n != Decimal("0.0")
        #TODO Erro nas formulas
        #self.assertAlmostEquals(Decimal("5.0"), n, TOLERANCE)
        #n = numberOfPayments(PAYMENT_TYPE_END, 3.95, 50000, 0, -2500.696667)
        #assert n != None
        #assert n != Decimal("0.0")
        #self.assertAlmostEquals(Decimal("16.0"), n, TOLERANCE)
        
        n = numberOfPayments(PAYMENT_TYPE_END, 0, 20008.36, -10000, -2500.696667)
        assert n != None
        assert n != Decimal("0.0")
        self.assertAlmostEquals(Decimal("12.0"), n, TOLERANCE)
        
        #Scenario with the four variables
        try:
            n = numberOfPayments(PAYMENT_TYPE_END, 5, 0.000002080, -30000, -5910.52)
            self.fail("Invalid number of payments")
            assert n != None
            assert n != Decimal("0.0")
            self.assertAlmostEquals(Decimal("6"), n, TOLERANCE)
        except ValueError:
            pass    
        
        n = numberOfPayments(PAYMENT_TYPE_END, 19.58131745, -500, 100, 9.790658e-11)
        assert n != None
        assert n != Decimal("0.0")
        self.assertAlmostEquals(Decimal("9.0"), n, TOLERANCE)
        
        #Scenario with payment mode in the beggining of the month
        try:
            n = numberOfPayments(PAYMENT_TYPE_BEGINNING, 5, 0.000002080, -30000, -5910.52)
            self.fail("Invalid number of payments")
            assert n != None
            assert n != Decimal("0.0")
            self.assertAlmostEquals(Decimal("6.0"), n, TOLERANCE)
        except ValueError:
            pass
        
        n = numberOfPayments(PAYMENT_TYPE_BEGINNING, 19.58131745, -500, 100, 9.790658e-11)
        assert n != None
        assert n != Decimal("0.0")
        self.assertAlmostEquals(Decimal("9.0"), n, TOLERANCE)
    
    def testPresentValue(self):
        
        #Scenario with only some variables
        pv = presentValue(PAYMENT_TYPE_END, 3.95, 50000, 18, 0)
        assert pv != None
        assert pv != Decimal("0")
        self.assertAlmostEquals(Decimal("-24895.9738"), pv, TOLERANCE)
        
        pv = presentValue(PAYMENT_TYPE_END, 0, 50000, 18, -1953.2486)
        assert pv != None
        assert pv != Decimal("0")
        self.assertAlmostEquals(Decimal("-14841.5252"), pv, TOLERANCE)
        
        pv = presentValue(PAYMENT_TYPE_END, 3.98, 50000, 0, -1953.2486)
        assert pv != None
        assert pv != Decimal("0")
        self.assertAlmostEquals(Decimal("-50000"), pv, TOLERANCE)
        
#        pv = presentValue(PAYMENT_TYPE_END, 3.98, 0, 18, -1953.2486)
#        assert pv != None
#        assert pv != Decimal("0")
#        self.assertAlmostEquals(Decimal("24766.9979"), pv, TOLERANCE)  

        pv = presentValue(PAYMENT_TYPE_END, 0, 20008.36, 12, -2500.696667)
        assert pv != None
        assert pv != Decimal("0")
        self.assertAlmostEquals(Decimal("-10000"), pv, TOLERANCE)
        
        #Scenario with the four variables
#        pv = presentValue(PAYMENT_TYPE_END, 5, 0.000002080, 6, -5910.52)
#        assert pv != None
#        assert pv != Decimal("0")
#        self.assertAlmostEquals(Decimal("29999.9795"), pv, TOLERANCE)
        
#        pv = presentValue(PAYMENT_TYPE_END, 19.58131745, -500, 9, 9.790658e-11)
#        assert pv != None
#        assert pv != Decimal("0")
#        self.assertAlmostEquals(Decimal("100"), pv, TOLERANCE)
        
        #Scenario with payment mode in the beggining of the month
#        pv = presentValue(PAYMENT_TYPE_BEGINNING, 5, 0.000002080, 6, -5910.52)
#        assert pv != None
#        assert pv != Decimal("0")
#        self.assertAlmostEquals(Decimal("29999.979"), pv, TOLERANCE)
        
#        pv = presentValue(PAYMENT_TYPE_BEGINNING, 19.58131745, -500, 9, 9.790658e-11)
#        assert pv != None
#        assert pv != Decimal("0")
#        self.assertAlmostEquals(Decimal("100"), pv, TOLERANCE)
   
    def testFutureValue(self):
       
        #Scenario with only some variables
#        fv = futureValue(PAYMENT_TYPE_END, 3.95, -24895.9738, 18, 0)
#        assert fv != None
#        assert fv != Decimal("0")
#        self.assertAlmostEquals( Decimal("50000"), fv, TOLERANCE)
        
        fv = futureValue(PAYMENT_TYPE_END, 3.95, -24895.9738, 0, 1958.6320)
        assert fv != None
        assert fv != Decimal("0")
        self.assertAlmostEquals( Decimal("24895.9738"), fv, TOLERANCE)
        
        fv = futureValue(PAYMENT_TYPE_END, 3.95, 0, 18, 1958.6320)
        assert fv != None
        assert fv != Decimal("0")
        self.assertAlmostEquals(Decimal("-50000.0"), fv, 1)
        
        fv = futureValue(PAYMENT_TYPE_END, 0, -10000, 12, -2500.696667)
        assert fv != None
        assert fv != Decimal("0")
        self.assertAlmostEquals(Decimal("40008.36"), fv, TOLERANCE)#
        
        #Scenario with the four variables
        fv = futureValue(PAYMENT_TYPE_END, 5, 0.000002080, 6, 5910.52)
        assert fv != None
        assert fv != Decimal("0")
        self.assertAlmostEquals(Decimal("-40202.8417"), fv, TOLERANCE)
        
#        fv = futureValue(PAYMENT_TYPE_END, 19.58131745, 100, 9, 9.790658e-11)
#        assert fv != None
#        assert fv != Decimal("0")
#        self.assertAlmostEquals(Decimal("-500"), fv, TOLERANCE)#
        
        #Scenario with payment mode in the beggining of the month
#        fv = futureValue(PAYMENT_TYPE_BEGINNING, 5, -30000, 6, -5910.52)
#        assert fv != None
#        assert fv != Decimal("0")
#        self.assertAlmostEquals(Decimal("80405.711"), fv, TOLERANCE)#
        
#        fv = futureValue(PAYMENT_TYPE_BEGINNING, 19.58131745, 100, 9, 9.790658e-11)
#        assert fv != None
#        assert fv != Decimal("0")
#        self.assertAlmostEquals(Decimal("-500"), fv, TOLERANCE)#   
        
        fv = futureValue(PAYMENT_TYPE_BEGINNING, 0, 10000, 12, -2500.696667)
        assert fv != None
        assert fv != Decimal("0")
        self.assertAlmostEquals(Decimal("20008.36"), fv, TOLERANCE)    
    
    def testPayment(self):
        
#        #Scenario with only some variables
#        pmt = payment(PAYMENT_TYPE_END, 3.95, 0, 18, -24895.9738)
#        assert pmt != None
#        assert pmt != Decimal("0")
#        self.assertAlmostEquals( Decimal("1958.6320"), pmt, TOLERANCE)
        
        pmt = payment(PAYMENT_TYPE_END, 0, 20008.36, 12, -10000)
        assert pmt != None
        assert pmt != Decimal("0")
        self.assertAlmostEquals(Decimal("-2500.696667"), pmt, TOLERANCE)#
        
        #Scenario with the four variables
        pmt = payment(PAYMENT_TYPE_END, 5, -30000, 6,  0.000002080)
        assert pmt != None
        assert pmt != Decimal("0")
        self.assertAlmostEquals(Decimal("-4410.5240"), pmt, TOLERANCE)#
        
#        pmt = payment(PAYMENT_TYPE_END, 19.58131745, -500, 9, 100)
#        assert pmt != None
#        assert pmt != Decimal("0")
#        self.assertAlmostEquals(Decimal("9.790658e-11"), pmt, TOLERANCE)#
        
#        #Scenario with payment mode in the beggining of the month
#        pmt = payment(PAYMENT_TYPE_BEGINNING, 5, 0.000002080, 6, -30000)
#        assert pmt != None
#        assert pmt != Decimal("0")
#        self.assertAlmostEquals(Decimal("5910.524"), pmt, TOLERANCE)#
        
#        pmt = payment(PAYMENT_TYPE_BEGINNING, 19.58131745, -500, 9, 100)
#        assert pmt != None
#        assert pmt != Decimal("0")
#        self.assertAlmostEquals( Decimal("9.790658e-11"), pmt, TOLERANCE)#
    
    def testInterestRate(self): 

        #Scenario with only some variables
        i = interestRate(PAYMENT_TYPE_END, 50000, -24895.9738, 18, 0)
        assert i != None
        assert i != Decimal("0")
        self.assertAlmostEquals(Decimal("3.95") , i, TOLERANCE)#
        
#        try:
#            i = interestRate(PAYMENT_TYPE_END, 0, -24895.9738, 18, -1394.668122)
#            self.fail("Invalid scenario")
#            assert i != None
#            assert i != Decimal("0")
#            self.assertAlmostEquals(Decimal("3.95") , i, TOLERANCE)#
#        except ValueError:
#            pass    
        
#        i = interestRate(PAYMENT_TYPE_END, 50000, 0, 18, -1394.668122)
#        assert i != None
#        assert i != Decimal("0")
#        self.assertAlmostEquals(Decimal("7.550140938") , i, TOLERANCE)#
        
#        try:
#            i = interestRate(PAYMENT_TYPE_END, 50000, -24895.9738, 0, -1394.668122)
#            self.fail("Invalid scenario")
#            assert i != None
#            assert i != Decimal("0")
#            self.assertAlmostEquals(Decimal("0.000000001") , i, TOLERANCE)#
#        except ValueError:
#            pass
            
        i = interestRate(PAYMENT_TYPE_END, 20008.36, -10000, 12, 0)
        assert i != None
        assert i != Decimal("0")
        self.assertAlmostEquals(Decimal("5.949999192"), i, TOLERANCE)
        
        #Scenario with the four variables
#        i = interestRate(PAYMENT_TYPE_END, -30000, 0.000002080, 6, -5910.52)
#        assert i != None
#        assert i != Decimal("0")
#        self.assertAlmostEquals(Decimal("2.841596e11"), i, TOLERANCE)# 
        
        i = interestRate(PAYMENT_TYPE_END, -500, 100, 9, 9.790658e-11)
        assert i != None
        assert i != Decimal("0")
        self.assertAlmostEquals(Decimal("19.58131745"), i, TOLERANCE)#
        
#        #Scenario with payment mode in the beggining of the month
#        i = interestRate(PAYMENT_TYPE_BEGINNING, 0.000002080, -30000, 6, -5910.52)
#        assert i != None
#        assert i != Decimal("0")
#        self.assertAlmostEquals(Decimal("-99.99999996"), i, TOLERANCE)#
        
        i = interestRate(PAYMENT_TYPE_BEGINNING, -500, 100, 9, 9.790658e-11)
        assert i != None
        assert i != Decimal("0")
        self.assertAlmostEquals(Decimal("19.58131745"), i, TOLERANCE)#
    
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
        except ValueError:
            pass
        else:
            self.fail("Should give pv, n and i")
        
        try:
            amortizationPlan = frenchAmortization(Decimal('8530.20'), Decimal('0'), Decimal('10'))
        except ValueError:
            pass
        else:
            self.fail("Should give pv, n and i")
        
        try:
            amortizationPlan = frenchAmortization(Decimal('8530.20'), Decimal('3'), Decimal('0'))
        except ValueError:
            pass
        else:
            self.fail("Should give pv, n and i")
            
        try:
            amortizationPlan = frenchAmortization(None, Decimal('3'), Decimal('10'))
        except ValueError:
            pass
        else:
            self.fail("Should give pv, n and i")
            
        try:
            amortizationPlan = frenchAmortization(Decimal('8530.20'), None, Decimal('10'))
        except ValueError:
            pass
        else:
            self.fail("Should give pv, n and i")    
            
        try:
            amortizationPlan = frenchAmortization(Decimal('8530.20'), Decimal('3'), None)
        except ValueError:
            pass
        else:
            self.fail("Should give pv, n and i")
    
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
        except ValueError:
            pass
        else:
            self.fail("Should give pv, n and i")
        
        try:
            amortizationPlan = equalsAmortization(Decimal('8530.20'), Decimal('0'), Decimal('10'))
        except ValueError:
            pass
        else:
            self.fail("Should give pv, n and i")
        
        try:
            amortizationPlan = equalsAmortization(Decimal('8530.20'), Decimal('3'), Decimal('0'))
        except ValueError:
            pass
        else:
            self.fail("Should give pv, n and i")
            
        try:
            amortizationPlan = equalsAmortization(None, Decimal('3'), Decimal('10'))
        except ValueError:
            pass
        else:
            self.fail("Should give pv, n and i")
            
        try:
            amortizationPlan = equalsAmortization(Decimal('8530.20'), None, Decimal('10'))
        except ValueError:
            pass
        else:
            self.fail("Should give pv, n and i")    
            
        try:
            amortizationPlan = equalsAmortization(Decimal('8530.20'), Decimal('3'), None)
        except ValueError:
            pass
        else:
            self.fail("Should give pv, n and i")