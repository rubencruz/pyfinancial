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

from decimal import Decimal, InvalidOperation, DivisionByZero

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
    except InvalidOperation:
        raise InvalidOperation, "Incompatibility of types."
    except ValueError, TypeError:
        raise TypeError, "Incompatibility of types."
    
def sub(number1, number2):
    """ Realize the subtraction operation between two values """
    
    try:
        n1 = convertToDecimal(number1)
        n2 = convertToDecimal(number2)
        if (number1 == number2):
            return Decimal('0.0')
        return n1 - n2
    except InvalidOperation:
        raise InvalidOperation, "Incompatibility of types."
    except ValueError, TypeError:
        raise TypeError, "Incompatibility of types."
    
def mult(number1, number2):
    """ Realize the multiplication operation between two values """
    
    try:
        n1 = convertToDecimal(number1)
        n2 = convertToDecimal(number2)
        return n1 * n2
    except InvalidOperation:
        raise InvalidOperation, "Incompatibility of types."
    except ValueError, TypeError:
        raise TypeError, "Incompatibility of types."
    
def div(number1, number2):
    """ Realize the division operation between two values """
    
    try:
        n1 = convertToDecimal(number1)
        n2 = convertToDecimal(number2)
        if n1 == n2 and n1 != Decimal('0.0'):
            return Decimal('1.0')
        return n1 / n2
    except InvalidOperation:
        raise InvalidOperation, "Incompatibility of types."
    except ValueError, TypeError:
        raise TypeError, "Incompatibility of types."
    except ZeroDivisionError:
        raise ZeroDivisionError, "Zero division."


def numberOfPayments(paymentMode, i, fv, pv, pmt):
    """ This function is responsible for calculating the number of payments 
    given the payment mode (at the beggining or end of the month), the present value, 
    the future value, the return rate and the payment """
    
    i = convertToDecimal(i)
    fv = convertToDecimal(fv)
    pv = convertToDecimal(pv)
    pmt = convertToDecimal(pmt)
    
    
    #All parameters are zero
    if (i == Decimal("0") and fv == Decimal("0") and pv == Decimal("0") and pmt == Decimal("0")):
        return Decimal("0")
    
    if (i <= Decimal("-100")):
        raise ValueError("Impossible scenario: i value less than -100")
    
    try:
    
        if (i == Decimal("0")):
#            if (pmt == Decimal("0")):
#                
#                #Special case
#                d = (i / Decimal("100")) / ( 1+(i*paymentMode / Decimal("100")) ) 
#                upperBound = max(fv*d, pv*d)
#                lowerBound = min(fv*d, pv*d)
#                
#                #Searching for a pmt 
#                found = False
#                firstValue = lowerBound 
#                while (firstValue < upperBound):
#                    dec = (pv - fv) / firstValue
#                    if Decimal(str(round(dec))) == dec:
#                        pmt = firstValue
#                        found = True
#                    else:
#                        firstValue += Decimal("0.1")    
#                
#                if not found:
#                    raise ValueError, "Can't calculate n with PMT and i = 0"
            
            value = (pv - fv) / pmt
            
            if (value < Decimal("0") and ((pv.is_signed() and fv.is_signed() and pmt.is_signed()) or (not pv.is_signed() and not fv.is_signed() and not pmt.is_signed())  )  ):
                raise ValueError, "Impossible scenario: Negative n"
            return abs(value)
        
#        elif pmt == Decimal("0") and i != Decimal("0") and fv != Decimal("0") and pv != Decimal("0"):
#            fv = abs(fv)
#            pv = abs(pv)
#            i = abs(i)
#            
#            n = (Decimal(fv) / pv).log10() / (Decimal('1.0') + (i / Decimal('100.0'))).log10()
#            if n < Decimal("0"):
#                raise ValueError, "Impossible scenario: Negative n"
#            return n
        
    #    if (not pv and not fv) or (not pv and not pmt) or (not pmt and not fv):
    #        raise ValueError, "Can't calculate n with only two or less registers!"
        
        if (paymentMode == PAYMENT_TYPE_BEGINNING):
            n = __nBeg(Decimal(i) / Decimal("100"), pv, pmt, fv)
            
            if n < Decimal("0") or n.is_infinite():
                raise ValueError, "Impossible scenario: Negative n"
            
            return n
        elif(paymentMode == PAYMENT_TYPE_END):
            n = __nEnd(Decimal(i) / Decimal("100"), pv, pmt, fv)
            
            if n < Decimal("0") or n.is_infinite():
                raise ValueError, "Impossible scenario: Negative n"
            
            return n
    
    except (InvalidOperation, DivisionByZero):
        raise ValueError("Impossible scenario")
    
    return Decimal("0")

def __nBeg(ir, pv, pmt, fv):
    """ This function is responsible for calculating the number of payments 
    given the present value, the future value, the return rate and the payment
    and that the payment mode is at the beggining of the month. """ 
    
    return ((-fv * Decimal(ir) + pmt* Decimal(ir) + pmt)/(Decimal(ir) * pmt + pmt + Decimal(ir) * pv)).log10() / (Decimal(ir) + Decimal("1")).log10()

def __nEnd(ir, pv, pmt, fv):
    """ This function is responsible for calculating the number of payments 
    given the present value, the future value, the return rate and the payment
    and that the payment mode is at the end of the month. """
    
    return ((pmt - fv * Decimal(ir))/(pmt + Decimal(ir) * pv)).log10() / (Decimal(ir) + Decimal("1")).log10()

def presentValue(paymentMode, i, fv, n, pmt):
    """ This function is responsible for calculating the present value of scenario 
    given the payment mode (at the beggining or end of the month), the number of payments, 
    the future value, the return rate and the payment """
    
    i = convertToDecimal(i)
    fv = convertToDecimal(fv)
    n = convertToDecimal(n)
    pmt = convertToDecimal(pmt)

    if i <= Decimal("-100"):
        raise ValueError, "Invalid scenario: invalid i"
    
    if i == Decimal("0"):
        
        pv = fv + n * pmt
        return -pv
        
    i = Decimal(i) / Decimal('100.0')
    
    if paymentMode == PAYMENT_TYPE_END:
        return __pvEnd(n, i, pmt, fv)
    elif paymentMode == PAYMENT_TYPE_BEGINNING:
        return __pvBeg(n, i, pmt, fv)
    else:
        #TODO - Raise a library exception
        raise Exception()

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
    
    if n == Decimal("0") and fv == Decimal("0") and i == Decimal("0") and pv == Decimal("0"):
        return Decimal("0")
    
    #Error condition
    if n == Decimal("0") or i <= Decimal("-100"):
        raise ValueError, "Invalid scenario: invalid parameters "+str(n)+" "+str(i)
    
    if i == Decimal("0"):
#        if n == Decimal("0") or fv == Decimal("0") or pv == Decimal("0"):
#            raise ValueError, "Can't calculate pmt with only two or less registers!"
        if n != Decimal("0"):
            pmt = (pv - fv)/n
            if pv < fv and pmt < Decimal("0"):
                return -pmt
            elif pv > fv and pmt > Decimal("0"):
                return -pmt
            elif n < Decimal("0"):
                return -pmt
            
            return pmt 
            
#    elif fv == Decimal("0") and paymentMode == PAYMENT_TYPE_END:
#        if n == Decimal("0") or i == Decimal("0") or pv == Decimal("0"):
#            raise ValueError, "Can't calculate pmt with only two or less registers!"
#        pmt = ((((Decimal("1")+i/Decimal("100"))**n) * i/Decimal("100") ) / (((Decimal("1")+i/Decimal("100"))**n) -Decimal("1"))*(Decimal("1")+i/Decimal("100"))) * pv
#        if (pv > Decimal("0") and pmt > Decimal("0")) or (pv < Decimal("0") and pmt < Decimal("0")):
#            return -pmt
#        
#        return pmt
#        
#    elif pv == Decimal("0") and fv != Decimal("0") and i != Decimal("0") and n != Decimal("0") and paymentMode == PAYMENT_TYPE_END:
#        pmt = fv * i / (((Decimal("1")+i)** n)-Decimal("1"))
#        if (pv > Decimal("0") and pmt > Decimal("0")) or (pv < Decimal("0") and pmt < Decimal("0")):
#            return -pmt
    
    if (paymentMode == PAYMENT_TYPE_BEGINNING):
        return _pmtBeg(n, i / Decimal("100"), pv, fv)
    elif(paymentMode == PAYMENT_TYPE_END):
        return _pmtEnd(n, i / Decimal("100"), pv, fv)
    else:
        raise ValueError, "Invalid scenario: Should select BEG or END"
    
#    if not n and not pv:
#        raise ValueError, "Can't calculate pmt with only two or less registers!"
    
#    dotPosition = str(Decimal(n)).find(".")
#    nIntPart = int(n)
#    nFracPart = Decimal(str(Decimal(n))[dotPosition:])
#    i = Decimal(i) / Decimal("100")
#    pmt = ((pv * (Decimal("1.0")+i) ** nFracPart) + fv * (Decimal("1.0")+i)**(-nIntPart)) / ((Decimal("1.0")+i*paymentMode)* ( (Decimal("1.0")-(Decimal("1.0")+i)**(-nIntPart))/ Decimal(i) ))
#    if (pv > Decimal("0") and pmt > Decimal("0")) or (pv < Decimal("0") and pmt < Decimal("0")):
#        return -pmt
#        
#    return pmt                                                               

def _pmtBeg(n, i, pv, fv):
    """ This function is responsible for calculating the payment 
    given the number of payments, the return rate, the present value, 
    the future value and that the payment mode is at the beggining of the month. """
    
    return - ( (i * (pv * (i + Decimal("1"))**n + fv )) / 
               ((i + Decimal("1")) * ((i + Decimal("1"))**n - Decimal("1")) ) )

def _pmtEnd(n, i, pv, fv):
    """ This function is responsible for calculating the payment 
    given the number of payments, the return rate, the present value, 
    the future value and that the payment mode is at the end of the month. """
    
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
    if i <= Decimal("-100"):
        raise ValueError, "Invalid scenario: Invalid i"
    
    if i == Decimal("0"):
        return - (pv + n * pmt)

    i = i / Decimal("100")
    
    if paymentMode == PAYMENT_TYPE_END:
        return __fvEnd(n, i, pv, pmt)
    elif paymentMode == PAYMENT_TYPE_BEGINNING:
        return __fvBeg(n, i, pv, pmt)
    else:
        #TODO - Raise a library exception
        raise Exception()

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

    #Error conditions
    if (n <= Decimal("0") or n >= Decimal("10**10") or 
        (fv.is_signed() and pv.is_signed() and pmt.is_signed()) or (not fv.is_signed() and not pv.is_signed() and not pmt.is_signed())):
        raise ValueError, "Impossible scenario: invalid parameters"
    
    #Testing which information is available
    if fv != Decimal("0") and pv != Decimal("0") and n != Decimal("0"):
        i = (((abs(Decimal(fv) / pv)) ** (Decimal("1") / Decimal(n))) - Decimal("1")) * Decimal("100")
        if (i < Decimal("0") and abs(fv) > abs(pv)) or (i > Decimal("0")  and abs(fv) < abs(pv)) or (i <= Decimal("-100")):
            raise ValueError, "Calculated i, pv and fv do not match!!"
        return i
    
    if n == Decimal("0"):
        number = numberOfPayments(paymentMode, Decimal("0"), fv, pv, pmt)
        if number != Decimal("0"):
            i = (((abs(Decimal(fv) / pv))** (Decimal("1") / Decimal(number))) - Decimal("1")) * Decimal("100")
            if (i < Decimal("0") and fv > pv) or (i > Decimal("0")  and fv < pv) or (i <= Decimal("-100")):
                raise ValueError, "Calculated i, pv and fv do not match!!"
            return i
    
    if pv == Decimal("0"):
        pv2 = presentValue(paymentMode, Decimal("0"), fv, n, pmt)
        if pv2 != Decimal("0"):
            i = (((abs(Decimal(fv) / pv2))** (Decimal("1") / Decimal(n))) - Decimal("1")) * Decimal("100")
            if (i < Decimal("0") and fv > pv) or (i > Decimal("0")  and fv < pv) or (i < Decimal("0") and pv < Decimal("0") and fv < Decimal("0") and pmt < Decimal("0")) or (i > Decimal("0") and pv > Decimal("0") and fv > Decimal("0") and pmt > Decimal("0")) or (i <= Decimal("-100")):
                    raise ValueError, "Calculated i, pv and fv do not match!!"
            return i
    
    if fv == Decimal("0"):
        fv2 = futureValue(paymentMode, Decimal("0"), pv, n, pmt)
        if fv2 != Decimal("0"):
                i =  (((abs(Decimal(fv2) / pv))** (Decimal("1") / Decimal(n))) - Decimal("1")) * Decimal("100")
                if (i < Decimal("0") and fv > pv) or (i > Decimal("0")  and fv < pv) or (i <= Decimal("-100")):
                    raise ValueError, "Calculated i, pv and fv do not match!!"
                return i
     
    return Decimal("0")

def netPresentValue(interRate, cashFlowsList):
    """ This function will perform the calculation of the npv value for a certain number of cash flows 
    that were previously informed """
    
    try:
        __checkInterestRate(interRate)
    except Exception, e:
        raise ValueError, e.message + " at NPV." 
    
    npv = Decimal('0.0')
    i = div(interRate, 100)
    if i == Decimal('-1.0') or i < Decimal('-1.0'):
        raise ValueError
    const = add(1, i)
    for count in range(0,len(cashFlowsList)):
        npv = add(npv, div(cashFlowsList[count], const**count ))
        
    return npv

def __checkInterestRate(interestRate):
    i = div(interestRate, 100)
    if i == Decimal('-1.0') or i < Decimal('-1.0'):
        raise ValueError, "Interest rate can not be equal or less than -100%"
    
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
    return pv * ( (((Decimal("1")+i)**n) * i) / ( ((Decimal("1")+i)**n)-Decimal("1") ) )
    
def frenchAmortization(pv, i, n):
    """ This method will implement the amortization based on the french system for PRICE payment """
    
    if i == None or pv == None or n == None or i == Decimal("0") or pv == Decimal("0") or n == Decimal("0"):
        raise ValueError, "Cannot calculate amortization without pv, n and i"
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
    
    if i == None or pv == None or n == None or i == 0 or pv == 0 or n == 0:
            raise ValueError, "Cannot calculate amortization without pv, n and i"
    realRate = i / Decimal('100.0')
    
    #Getting constant amortization
    amortization = Decimal(pv) / n
    
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
        
def simpleInterest(pv, n, i):
    pass

def convertToDecimal(arg1):
    if arg1 == None:
        return None
    argDec1 = Decimal(str(arg1))
    return argDec1       
