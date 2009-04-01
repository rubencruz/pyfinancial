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
# library.py, This module contains the implementation of functions in the 
# calculator HP12-C  
#
#*****************************************************************************


# LINK consulta: http://www.crd2000.com.br/crd012d.htm
# http://www.ufcg-uaac.com/Curso_extensao_gestao_investimentos.htm
from decimal import Decimal, InvalidOperation, DivisionByZero, ROUND_UP, ROUND_HALF_UP
from pyFinancialLibraryException import PyFinancialLibraryException


TOLERANCE = Decimal("0.0000000001")

#Payment modes
PAYMENT_TYPE_END = 0
PAYMENT_TYPE_BEGINNING = 1
    
def add(number1, number2):
    """ Realize the addition operation between two values """
    
    try:
        n1 = convertToDecimal(number1)
        n2 = convertToDecimal(number2)
        return n1 + n2
    except InvalidOperation, TypeError:
        raise PyFinancialLibraryException("Invalid scenario: Impossible operations." )
    except ValueError:
        raise PyFinancialLibraryException("Invalid scenario: Impossible operations." )
    
def sub(number1, number2):
    """ Realize the subtraction operation between two values """
    
    try:
        n1 = convertToDecimal(number1)
        n2 = convertToDecimal(number2)
        
        #TODO - Insert a tolerance at equal comparison
        if (number1 == number2):
            return Decimal('0.0')
        return n1 - n2
    except InvalidOperation, TypeError:
        raise PyFinancialLibraryException("Invalid scenario: Impossible operations." )
    except ValueError:
        raise PyFinancialLibraryException("Invalid scenario: Impossible operations." )
    
def mult(number1, number2):
    """ Realize the multiplication operation between two values """
    
    try:
        n1 = convertToDecimal(number1)
        n2 = convertToDecimal(number2)
        return n1 * n2
    except InvalidOperation, TypeError:
        raise PyFinancialLibraryException("Invalid scenario: Impossible operations." )
    except ValueError:
        raise PyFinancialLibraryException("Invalid scenario: Impossible operations." )
    
def div(number1, number2):
    """ Realize the division operation between two values """
    
    try:
        n1 = convertToDecimal(number1)
        n2 = convertToDecimal(number2)
        
        #TODO - Insert a tolerance at equal comparison
        if n1 == n2 and n1 != Decimal('0.0'):
            return Decimal('1.0')
        return n1 / n2
    except ZeroDivisionError:
        raise PyFinancialLibraryException("Invalid scenario: Zero division." )
    except Exception:
        raise PyFinancialLibraryException("Invalid scenario: Impossible operations." )

def numberOfPayments(paymentMode, i, fv, pv, pmt):
    """ This function is responsible for calculating the number of payments 
    given the payment mode (at the beggining or end of the month), the present value, 
    the future value, the return rate and the payment """
    
    i = convertToDecimal(i)
    fv = convertToDecimal(fv)
    pv = convertToDecimal(pv)
    pmt = convertToDecimal(pmt)

    if (paymentMode != PAYMENT_TYPE_BEGINNING and paymentMode != PAYMENT_TYPE_END):
        raise PyFinancialLibraryException("Invalid scenario: Should select BEG or END." )
    
    #All parameters are zero
    if (i == Decimal("0") and fv == Decimal("0") and pv == Decimal("0") and pmt == Decimal("0")):
        return Decimal("0")
    
    i = __checkInterestRate(i)
        
    try:
        if (paymentMode == PAYMENT_TYPE_BEGINNING):
            n = __nBeg(i, pv, pmt, fv)
            
        else:
            n = __nEnd(i, pv, pmt, fv)
            

        if n.is_infinite():
            raise PyFinancialLibraryException, "Invalid scenario: Infinite n."
                
    except (InvalidOperation, DivisionByZero):
        try:
            n = - (fv + pv)/pmt
        except (InvalidOperation, DivisionByZero):
            raise PyFinancialLibraryException("Invalid scenario: Error(s) in the values of operators of capitalization (n, i, PV, FV or PMT).")

    finalValue = n.quantize(Decimal("1"), ROUND_UP)
    
    if finalValue < Decimal("0"):
        raise PyFinancialLibraryException("Invalid scenario: Error(s) in the values of operators of capitalization (n, i, PV, FV or PMT).")
    return finalValue

def __nBeg(ir, pv, pmt, fv):
    """ This function is responsible for calculating the number of payments 
    given the present value, the future value, the return rate and the payment
    and that the payment mode is at the beggining of the month. """ 
    
    return ((-fv * Decimal(ir) + pmt* Decimal(ir) + pmt)/(Decimal(ir) * pmt + pmt + Decimal(ir) * pv)).log10() / (Decimal(ir) + Decimal("1")).log10()

def __nEnd(ir, pv, pmt, fv):
    """ This function is responsible for calculating the number of payments 
    given the present value, the future value, the return rate and the payment
    and that the payment mode is at the end of the month. """
    
    return ((pmt - fv * ir)/(pmt + ir * pv)).log10() / (ir + Decimal("1")).log10()

def presentValue(paymentMode, i, fv, n, pmt):
    """ This function is responsible for calculating the present value of scenario 
    given the payment mode (at the beggining or end of the month), the number of payments, 
    the future value, the return rate and the payment """
    
    i = convertToDecimal(i)
    fv = convertToDecimal(fv)
    n = convertToDecimal(n)
    pmt = convertToDecimal(pmt)

    i = __checkInterestRate(i)
    
    if i == Decimal("0"):
        
        pv = fv + n * pmt
        return -pv
        
    if paymentMode == PAYMENT_TYPE_END:
        return __pvEnd(n, i, pmt, fv)
    elif paymentMode == PAYMENT_TYPE_BEGINNING:
        return __pvBeg(n, i, pmt, fv)
    else:
        raise PyFinancialLibraryException, "Invalid scenario: Should select BEG or END." 

def __pvBeg(n, i, pmt, fv ):
    """ This function is responsible for calculating the present value 
    given the number of payments, the return rate, the payment, the future value 
    and that the payment mode is at the beggining of the month. """
    
    return ((i + Decimal("1"))**-n * (-fv * i - (i+Decimal("1")) * ((i + Decimal("1"))**n - Decimal("1")) * pmt))/i

def __pvEnd(n, i, pmt, fv ):
    """ This function is responsible for calculating the present value 
    given the number of payments, the return rate, the payment, the future value 
    and that the payment mode is at the end of the month. """
    
    return ((i + Decimal("1"))**-n * (-pmt * (i + Decimal("1"))**n - fv * i + pmt))/i

def payment(paymentMode, i, fv, n, pv):
    """ This function is responsible for calculating the payment of scenario 
    given the payment mode (at the beggining or end of the month), the return rate, 
    the future value, the number of payments and the present value """
    
    i = convertToDecimal(i)
    fv = convertToDecimal(fv)
    pv = convertToDecimal(pv)
    n = convertToDecimal(n)

    if (paymentMode != PAYMENT_TYPE_BEGINNING and paymentMode != PAYMENT_TYPE_END):
        raise PyFinancialLibraryException, "Invalid scenario: Should select BEG or END."
    
    if n == Decimal("0") and fv == Decimal("0") and i == Decimal("0") and pv == Decimal("0"):
        return Decimal("0")
    
    #Error condition
    if n == Decimal("0") or i <= Decimal("-100"):
        raise PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators of capitalization (n, i, PV, FV or PMT)." 
    
    if i == Decimal("0"):
        return -(fv + pv)/n
                
    if (paymentMode == PAYMENT_TYPE_BEGINNING):
        return _pmtBeg(n, i, pv, fv)
    else:
        return _pmtEnd(n, i, pv, fv)
    
    
def _pmtBeg(n, i, pv, fv):
    """ This function is responsible for calculating the payment 
    given the number of payments, the return rate, the present value, 
    the future value and that the payment mode is at the beggining of the month. """
    
    i = i / Decimal("100")
    return - ( (i * (pv * (i + Decimal("1"))**n + fv )) / 
               ((i + Decimal("1")) * ((i + Decimal("1"))**n - Decimal("1")) ) )

def _pmtEnd(n, i, pv, fv):
    """ This function is responsible for calculating the payment 
    given the number of payments, the return rate, the present value, 
    the future value and that the payment mode is at the end of the month. """
    
    i = i / Decimal("100")
    return - ( (i * (pv * (i + Decimal("1"))**n + fv )) / 
               ((i + Decimal("1"))**n - Decimal("1")) )

def futureValue(paymentMode, i, pv, n, pmt):
    """ This function is responsible for calculating the future value of scenario 
    given the payment mode (at the beggining or end of the month), the number of payments, 
    the present value, the return rate and the payment """

    i = convertToDecimal(i)
    n = convertToDecimal(n)
    pv = convertToDecimal(pv)
    pmt = convertToDecimal(pmt)
    
    #Error condition
    i = __checkInterestRate(i)
    
    if i == Decimal("0"):
        return - (pv + n * pmt)

    if paymentMode == PAYMENT_TYPE_END:
        return __fvEnd(n, i, pv, pmt)
    elif paymentMode == PAYMENT_TYPE_BEGINNING:
        return __fvBeg(n, i, pv, pmt)
    else:
        raise PyFinancialLibraryException, "Invalid scenario: Should select BEG or END." 

def __fvBeg(n, i, pv, pmt):
    """ This function is responsible for calculating the number of payments 
    given the present value, the future value, the return rate and the payment
    and that the payment mode is at the beggining of the month. """
    
    return ((i + Decimal("1")) * pmt - (i + Decimal("1"))**n * (i * pmt + pmt + i*pv))/i

def __fvEnd(n, i, pv, pmt):
    """ This function is responsible for calculating the number of payments 
    given the present value, the future value, the return rate and the payment
    and that the payment mode is at the end of the month. """
    
    return (pmt - ((i + Decimal("1"))**n) * (pmt + i * pv) )/i

def interestRate(paymentMode, fv, pv, n, pmt):
    """ This function is responsible for calculating the interest rate given 
    the present value, the future value, the number of payments and the payment
    and that the payment mode is at beggining or end of the month. """ 
    
    n = convertToDecimal(n)
    fv = convertToDecimal(fv)
    pv = convertToDecimal(pv)
    pmt = convertToDecimal(pmt)
    
    if (paymentMode != PAYMENT_TYPE_BEGINNING and paymentMode != PAYMENT_TYPE_END):
        raise PyFinancialLibraryException, "Invalid scenario: Should select BEG or END."
    
    if n == Decimal("0") and fv == Decimal("0") and pmt == Decimal("0") and pv == Decimal("0"):
        return Decimal("0")    

    #Error conditions
    if (n <= Decimal("0") or n >= (Decimal("10")**Decimal("10")) or pmt == Decimal("0") or 
        (fv.is_signed() and pv.is_signed() and pmt.is_signed()) or (not fv.is_signed() and not pv.is_signed() and not pmt.is_signed())):
        raise PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators of capitalization (n, i, PV, FV or PMT)."
    
    ir = Decimal("0.01")
    tir = ir
    maxtries = 400
    val = 0
    oldval = 0
    delta = 0
    olddelta = 0
    
    if fv == Decimal("0") and pv == Decimal("0"):
        if pmt < Decimal("0"):
            return Decimal("-100")
        else:
            return Decimal("100")
    else:
        k = 0
        solved = False
        while k < 2 and not solved:
            i = 0
            j = 0
            if k == 0:
                guess = ir
            else:
                guess = -ir
            gd = guess * Decimal("0.5")
            if(gd == Decimal("0.0")):
                gd = Decimal("1.0")
                
            while i < maxtries and j <= 3:
                guess += gd
                if(guess != Decimal("0.0") and guess > Decimal("-1")):
                    val = futureValue(paymentMode, guess * Decimal("100"), pv, n, pmt)
                    delta = abs(val-fv)
                if i > 0 :
                    j += 1
                    if (abs(val-oldval) > Decimal("1.0E-8")) or (delta > Decimal("1.0E-8")):
                        j = 0
                    if(delta > olddelta):
                        gd *= Decimal("-0.5")
                    
                oldval = val;
                olddelta = delta;
                
                i += 1

            if(i < maxtries):
                tir = guess
                solved = True

            k += 1

        if not solved:
            raise PyFinancialLibraryException, "Invalid scenario: Error(s) in the values of operators of capitalization (n, i, PV, FV or PMT)."
    
    return tir * Decimal("100")


def netPresentValue(interRate, cashFlowsList):
    """ This function will perform the calculation of the npv value for a certain number of cash flows 
    that were previously informed """
    
    i = __checkInterestRate(interRate)
    
    npv = Decimal('0.0')
    if i == Decimal('-1.0') or i < Decimal('-1.0'):
        raise ValueError
    const = add(1, i)
    for count in range(0,len(cashFlowsList)):
        npv = add(npv, div(cashFlowsList[count], const**count ))
        
    return npv

def __checkInterestRate(interestRate):
    i = div(interestRate, 100)
    if i <= Decimal('-1.0'):
        raise PyFinancialLibraryException, "Invalid scenario: i value equal or less than -100%."
    return i 
    
def interestRateOfReturn(cashFlowsList):
    """ This function will perform the calculation of the intern return rate (IRR)
    for a certain number of cash flows that were previously informed """
    
    step = Decimal('0.05') # 0.05%    
    i = Decimal('0.0')
    npv = netPresentValue(i, cashFlowsList)
    if npv == Decimal('0.0'):
        return i
    elif npv > Decimal('0.0'):
        while npv > Decimal('0.0'):
            iBefore = i
            npvBefore = npv
            
            i = i + step
            npv = netPresentValue(i, cashFlowsList)
        return __findIRR(iBefore, npvBefore, i, npv)
    else:
        while npv < Decimal('0.0'):
            iBefore = i
            npvBefore = npv
            
            i = i + step
            npv = netPresentValue(i, cashFlowsList)
        return __findIRR(iBefore, npvBefore, i, npv)

def __findIRR(upperX, upperY, downX, downY):
    return div(upperY*downX - downY*upperX, upperY - downY)     

def calculateFrenchPmt(pv, i, n):
    """ This function calculates the pmt of an amortization plan based on the french system """
    
    return pv * ( (((Decimal("1")+i)**n) * i) / ( ((Decimal("1")+i)**n)-Decimal("1") ) )
    
def frenchAmortization(pv, i, n):
    """ This method will implement the amortization based on the french system for PRICE payment """
    
    if i == None or pv == None or n == None or i == Decimal("0") or pv == Decimal("0") or n == Decimal("0"):
        raise PyFinancialLibraryException, "Some values for calculating amortization have not been provided." 
    realRate = i / Decimal('100.0')
    
    #Getting pmt
    pmt = calculateFrenchPmt(pv, realRate, n)
    
    #Storing information for first period, containing for each period: pmt, interest, acumulated interest, amortization, acumulated amortization and amount to be payed
    amortizationPlan = [ [Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), pv] ]
    
    #Calculating information for other periods
    for index in xrange(1, n+1, 1):
        lastAmountToBePayed = amortizationPlan[index-1][5]
        acumulatedAmortization = amortizationPlan[index-1][4]
        acumulatedInterest = amortizationPlan[index-1][2]
        
        amortization = (pmt - (pv* realRate) ) * (realRate+1)**(index-1)
        interest = pmt - amortization
        amountToBePayed = lastAmountToBePayed - amortization
        newAcumulatedAmortization = acumulatedAmortization + amortization
        newAcumulatedInterest = acumulatedInterest + interest
        
        if amountToBePayed <= TOLERANCE:
            amountToBePayed = Decimal('0')
        
        amortizationPlan.append( [pmt, interest, newAcumulatedInterest, amortization, newAcumulatedAmortization, amountToBePayed]  )
     
    return amortizationPlan   

def equalsAmortization(pv, i, n):
    """ This method will implement the amortization based on the constant amortization system for PRICE payment """
    
    if i == None or pv == None or n == None or i == 0 or pv == 0 or n == 0:
            raise PyFinancialLibraryException, "Some values for calculating amortization have not been provided."
    realRate = i / Decimal('100.0')
    
    #Getting constant amortization
    amortization = convertToDecimal(pv) / n
    
    #Storing information for first period, containing for each period: pmt, interest, acumulated interest, amortization, acumulated amortization and amount to be payed
    amortizationPlan = [ [Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), Decimal('0'), pv] ]
    
    #Calculating information for other periods
    for index in xrange(1, n+1, 1):
        lastAmountToBePayed = amortizationPlan[index-1][5]
        acumulatedAmortization = amortizationPlan[index-1][4]
        acumulatedInterest = amortizationPlan[index-1][2]
        
        interest = (pv * realRate) - (amortization * realRate * (index-1))
        payment = amortization + interest
        
        newAmountToBePayed = lastAmountToBePayed - amortization
        newAcumulatedAmortization = acumulatedAmortization + amortization
        newAcumulatedInterest = acumulatedInterest + interest
        
        if newAmountToBePayed <= TOLERANCE:
            newAmountToBePayed = Decimal('0')
            
        amortizationPlan.append( [ payment, interest, newAcumulatedInterest, amortization, newAcumulatedAmortization,  newAmountToBePayed  ] )   
        
    return amortizationPlan

def convertAnualPeriodsToMonthPeriods(numberOfAnualPeriods):
    """ This function will convert annual periods to month periods for financial calculations """
    
    if numberOfAnualPeriods == None:
        raise PyFinancialLibraryException, "Invalid scenario: Impossible operations." 
    
    decimalNumberOfAnualPeriods = convertToDecimal(numberOfAnualPeriods)
    
    #Converting the anual number of periods to month periods
    monthPeriods = decimalNumberOfAnualPeriods * Decimal("12.0")
    return monthPeriods
     
def convertAnualRateToMonthRates(anualRate, isCompoundInterest):
    """ This function will convert an annual rate to a month rate according to the fact that it's dealing with 
    a compound rate system or a simple one """
    
    if anualRate == None:
        raise PyFinancialLibraryException, "Invalid scenario: Impossible operations." 
    
    decimalAnualRate = convertToDecimal(anualRate) / Decimal("100.0")
    
    if isCompoundInterest:#Converting rates in a compound rate system
        rateSigned = (Decimal("1.0")+decimalAnualRate).__abs__()
        expTerm = (rateSigned)**(Decimal("0.083333333"))
        if Decimal("1.0")+decimalAnualRate < Decimal("0.0"):
            expTerm = -expTerm
        
        monthRate = Decimal("100.0") * ((expTerm) - Decimal("1.0"))
        
        
    else:#Converting rates in a simple rate system
        monthRate = Decimal("100.0") * decimalAnualRate / Decimal("12.0")
     
    return monthRate
        
def simpleInterest(pv, n, i):
    return Decimal("0")

def percentageAmount(base, percentage):
    """This function finds the amount corresponding to a percentage of a 
    number."""
    base = convertToDecimal(base)
    percentage = convertToDecimal(percentage)
    
    return (base * percentage) / Decimal("100")

def percentOfTotal(total, value):
    
    total = convertToDecimal(total)
    value = convertToDecimal(value)
    
    if total == Decimal("0"):
        raise PyFinancialLibraryException, "Put an error msg here."
    
    return Decimal("100") * (value / total)

def convertToDecimal(arg1):
    """ This function will convert the number received as an argument to a Decimal representation """
    
    if arg1 == None:
        return None
    try:
        argDec1 = Decimal(str(arg1))
        return argDec1
    except InvalidOperation:
        raise PyFinancialLibraryException, "Invalid scenario: Impossible operations."
           