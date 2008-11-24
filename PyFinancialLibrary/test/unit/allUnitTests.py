#****************************************************************************
#allUnitTests.py, This module is responsible for running all unit tests of our
#library
#
# pyFinancial, a financial library for python users
# Copyright (C) 2008, Felipe Leal, David Candeia, Everton Leandro and Diego Dantas
#*****************************************************************************

import unittest
from unit.libraryTests import *

if __name__ == "__main__":
    """ Here we collect and run all unit tests of our library """
    
    suite1 = unittest.makeSuite(LibraryTestCase, "test")
    
    runner = unittest.TextTestRunner()
    runner.run(suite1)