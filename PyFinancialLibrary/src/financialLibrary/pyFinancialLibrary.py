#****************************************************************************
# library.py, This module contains the implementation of functions in the 
# calculator HP12-C
#
# pyFinancial, a financial library for python users
# Copyright (C) 2008, Felipe Leal, David Candeia, Everton Leandro and Diego Dantas
#*****************************************************************************


    
def sum(number1, number2):
    """ Realize the sum operation between two values """
    try:
        return number1 + number2
    except TypeError:
        print("Incompatibility of types.")
    
def minus(number1, number2):
    """ Realize the minus operation between two values """
    try:
        return number2 - number1
    except TypeError:
        print("Incompatibility of types.")
    
def mult(number1, number2):
    """ Realize the multiplication operation between two values """
    try:
        return number1 * number2
    except TypeError:
        print("Incompatibility of types.")
    
def div(number1, number2):
    """ Realize the division operation between two values """
    try:
        n1 = float(number1)
        n2 = float(number2)
        return n2 / n1
    except TypeError:
        print("Incompatibility of types.")
