import unittest
from financialLibrary.library import *

class LibraryTestCase (unittest.TestCase):
    
    def testSum(self):
        """ Verifies the sum method of library.py """
        assert library.sum(1, 2) == 3
        assert library.sum(0, 0) == 0
        assert library.sum(-5, 5) == 0
        assert library.sum(-0.3, 5) == 4.7
        assert library.sum(-0.3, -5) == -5.3
        
        self.assertRaises(TypeError, library.sum(3, "-5"), -1, -1)
        self.assertRaises(TypeError, library.sum(3, library()), -1, -1)
    
    def testMinus(self):
        """ Verifies the minus method of library.py """
        assert library.minus(1, 2) == -1
        assert library.minus(0, 0) == 0
        assert library.minus(-5, 5) == -10
        assert library.minus(-0.3, 5) == -5.3
        assert library.minus(-0.3, -5) == 4.7
        
        self.assertRaises(TypeError, library.minus(3, "-5"), -1, -1)
        self.assertRaises(TypeError, library.minus(3, library()), -1, -1)
    
    def testMult(self):
        """ Verifies the mult method of library.py """
        assert library.mult(1, 2) == 2
        assert library.mult(0, 0) == 0
        assert library.mult(-5, 5) == -25
        assert library.mult(-0.3, 5) == -1.5
        assert library.mult(-0.3, -5) == 1.5
        
        self.assertRaises(TypeError, library.mult(3, "-5"), -1, -1)
        self.assertRaises(TypeError, library.mult(3, library()), -1, -1)    

    def testDiv(self):
        """ Verifies the div method of library.py """
        assert library.div(1, 2) == 0.5
        assert library.div(-5, 5) == -1
        assert library.div(-0.3, 5) == -0.06
        assert library.div(-0.3, -5) == 0.06
        
        self.assertRaises(TypeError, library.div(3, "-5"), -1, -1)
        self.assertRaises(TypeError, library.div(3, library()), -1, -1)
        self.assertRaises(TypeError, library.div(3, 0), -1, -1) 
        self.assertRaises(TypeError, library.div(0, 0), -1, -1)   
