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

import math

tolerance = 0.0000000001

#Payment modes
PAYMENT_TYPE_BEGINNING = 0
PAYMENT_TYPE_END = 1
    
def add(number1, number2):
    """ Realize the addition operation between two values """
    
    try:
        n1 = float(number1)
        n2 = float(number2)
        return n1 + n2
    except ValueError, TypeError:
        raise TypeError, "Incompatibility of types."
    
def sub(number1, number2):
    """ Realize the subtraction operation between two values """
    
    try:
        n1 = float(number1)
        n2 = float(number2)
        if (equalNums(number1, number2)):
            return 0
        return n1 - n2
    except ValueError, TypeError:
        raise TypeError, "Incompatibility of types."
    
def mult(number1, number2):
    """ Realize the multiplication operation between two values """
    
    try:
        n1 = float(number1)
        n2 = float(number2)
        return n1 * n2
    except ValueError, TypeError:
        raise TypeError, "Incompatibility of types."
    
def div(number1, number2):
    """ Realize the division operation between two values """
    
    try:
        n1 = float(number1)
        n2 = float(number2)
        if (equalNums(number1, number2)):
            return 1
        return n1 / n2
    except ValueError, TypeError:
        raise TypeError, "Incompatibility of types."
    except ZeroDivisionError:
        raise ZeroDivisionError, "Zero division."

def equalNums(number1, number2):
    """ Verify if two numbers are equals """
    
    return (number1 - number2).__abs__() < tolerance 

def numberOfPayments(paymentMode, i, fv, pv, pmt):
    """ This function is responsible for calculating the number of payments 
    given the payment mode (at the beggining or end of the month), the present value, 
    the future value, the return rate and the payment """
    
    if (i == 0):
        if (pmt == 0):
            raise ValueError, "Can't calculate PMT with PMT=0"
        
        value = (pv - fv) / pmt
        if (value < 0):
            raise ValueError, "Impossible scenario: Negative n"
        return value
    
    elif pmt == 0 and i != 0 and fv != 0 and pv != 0:
        fv = math.fabs(fv)
        pv = math.fabs(pv)
        i = math.fabs(i)
        return (math.log(fv / pv)) / (math.log(1+ (i / 100)))
    
    if (paymentMode == PAYMENT_TYPE_BEGINNING):
        return __nBeg(i, pv, pmt, fv)
    elif(paymentMode == PAYMENT_TYPE_END):
        return __nEnd(i, pv, pmt, fv)
    
    return 0

def __nBeg(ir, pv, pmt, fv):
    """ This function is responsible for calculating the number of payments 
    given the present value, the future value, the return rate and the payment
    and that the payment mode is at the beggining of the month. """ 
    
    return math.log((-fv*ir + pmt*ir + pmt)/(ir*pmt + pmt + ir*pv)) / math.log(ir + 1)

def __nEnd(ir, pv, pmt, fv):
    """ This function is responsible for calculating the number of payments 
    given the present value, the future value, the return rate and the payment
    and that the payment mode is at the end of the month. """
    
    return math.log((pmt - fv*ir)/(pmt + ir*pv)) / math.log(ir + 1)

def presentValue(paymentMode, i, fv, n, pmt):
    """ This function is responsible for calculating the present value of scenario 
    given the payment mode (at the beggining or end of the month), the number of payments, 
    the future value, the return rate and the payment """
    
    if i == 0:
        return fv + n * pmt
    elif pmt == 0:
        return fv / math.pow(1+i/100, n)
    
    if (paymentMode == PAYMENT_TYPE_BEGINNING):
        return __pvBeg(n, i, pmt, fv)
    elif(paymentMode == PAYMENT_TYPE_END):
        return __pvEnd(n, i, pmt, fv)
    
    return 0

def __pvBeg(np, i, pmt, fv ):
    """ This function is responsible for calculating the present value 
    given the number of payments, the return rate, the payment, the future value 
    and that the payment mode is at the beggining of the month. """
    
    return ((i + 1)**-np * (-fv * i - (i+1) * ((i + 1)**np - 1) * pmt))/i

def __pvEnd(np, i, pmt, fv ):
    """ This function is responsible for calculating the present value 
    given the number of payments, the return rate, the payment, the future value 
    and that the payment mode is at the end of the month. """
    
    return ((i + 1)**-np * (-pmt * (i + 1)**np - fv * i + pmt))/i

def payment(paymentMode, i, fv, n, pv):
    """ This function is responsible for calculating the payment of scenario 
    given the payment mode (at the beggining or end of the month), the return rate, 
    the future value, the number of payments and the present value """
    
    if i == 0:
        if n == 0:
            raise ValueError, "Can't calculate pmt with i = 0 and n = 0"
        return (pv - fv)/n
    elif fv == 0:
        return ((math.pow(1+i/100, n) * i/100 ) / (math.pow(1+i/100,n) -1)) * pv
    elif pv == 0 and fv != 0 and i != 0 and n != 0:
        return fv * i / (math.pow(1+i, n)-1)
    
    if (paymentMode == PAYMENT_TYPE_BEGINNING):
        return _pmtBeg(n, i, pv, fv)
    elif(paymentMode == PAYMENT_TYPE_END):
        return _pmtEnd(n, i, pv, fv)
    
    return 0

def _pmtBeg(n, i, pv, fv):
    """ This function is responsible for calculating the payment 
    given the number of payments, the return rate, the present value, 
    the future value and that the payment mode is at the beggining of the month. """
    
    return - ( (i * (pv * (i + 1)**n + fv )) / 
               ((i + 1) * ((i + 1)**n - 1) ) )

def _pmtEnd(n, i, pv, fv):
    """ This function is responsible for calculating the payment 
    given the number of payments, the return rate, the present value, 
    the future value and that the payment mode is at the end of the month. """
    
    return - ( (i * (pv * (i + 1)**n + fv )) / 
               ((i + 1)**n - 1) )

def futureValue(paymentMode, i, pv, n, pmt):
    """ This function is responsible for calculating the future value of scenario 
    given the payment mode (at the beggining or end of the month), the number of payments, 
    the present value, the return rate and the payment """
#    return -(pv * math.pow((1 + i/100), n))
    if (i == 0 and pv != 0 and n != 0 and pmt != 0):
        return pv - n * pmt
    elif (pmt == 0 and pv != 0 and n != 0 and i != 0):
        return pv * math.pow(1+i, n)
    elif pv == 0 and pmt != 0 and i != 0 and n != 0:
        return pmt * ((math.pow(i+1, n)-1) / i)
    
    if (paymentMode == PAYMENT_TYPE_BEGINNING):
        return _fvBeg(n, i, pv, pmt)
    elif(paymentMode == PAYMENT_TYPE_END):
        return _fvEnd(n, i, pv, pmt)    

    return 0

def _fvBeg(np, i, pv, pmt):
    """ This function is responsible for calculating the number of payments 
    given the present value, the future value, the return rate and the payment
    and that the payment mode is at the beggining of the month. """
    
    return ((i + 1) * pmt - (i + 1)**np * (i * pmt + pmt + i*pv))/i

def _fvEnd(np, i, pv, pmt):
    """ This function is responsible for calculating the number of payments 
    given the present value, the future value, the return rate and the payment
    and that the payment mode is at the end of the month. """
    
    return (pmt - (i + 1)**np * (pmt + i * pv) )/i

def interestRate(paymentMode, fv, pv, n, pmt):
    """ This function is responsible for calculating the interest rate given 
    the present value, the future value, the number of payments and the payment
    and that the payment mode is at beggining or end of the month. """ 
    
    #Testing which information is available
    if fv != 0 and pv != 0 and n != 0:
        return (math.pow(fv / pv, 1 / n) - 1) * 100
    
    if n == 0:
        number = numberOfPayments(paymentMode, 0, fv, pv, pmt)
        if number != 0:
            return (math.pow(fv / pv, 1 / number) - 1) * 100
    
    if pv == 0:
        presentValue = presentValue(paymentMode, 0, fv, n, pmt)
        if presentValue != 0:
            return (math.pow(fv / presentValue, 1 / n) - 1) * 100
    
    if fv == 0:
        futureValue = futureValue(paymentMode, 0, pv, n, pmt)
        if futureValue != 0:
                return (math.pow(futureValue / presentValue, 1 / n) - 1) * 100
     
    return 0       