#****************************************************************************
# library.py, This module contains the implementation of functions in the 
# calculator HP12-C
#
# pyFinancial, a financial library for python users
# Copyright (C) 2008, Felipe Leal, David Candeia, Everton Leandro and Diego Dantas
#
# This is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License, either Version 2 or any later
# version.  This program is distributed in the hope that it will be useful,
# but WITTHOUT ANY WARRANTY.  See the included LICENSE file for details.
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
        return number1 - number2
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
        return n1 / n2
    except TypeError:
        print("Incompatibility of types.")
    except AttributeError:
        print("Incompatibility of types.")
    except ZeroDivisionError:
        print("Division by zero")
