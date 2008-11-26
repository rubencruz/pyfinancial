#****************************************************************************
# library.py, This module contains the implementation of functions in the 
# calculator HP12-C
#
# pyFinancial, a financial library for python users
# Copyright (C) 2008, Felipe Leal, David Candeia, Everton Leandro and Diego Dantas
#*****************************************************************************

tolerance = 0.0000000001
    
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
    