import unittest
from financialLibrary.pyFinancialLibrary import *

class LibraryTestCase (unittest.TestCase):
    
    def testSum(self):
        """ Verifies the sum method of pyFinancialLibrary.py """
        assert PyFinancialLibrary.sum(1, 2) == 3
        assert PyFinancialLibrary.sum(0, 0) == 0
        assert PyFinancialLibrary.sum(-5, 5) == 0
        assert PyFinancialLibrary.sum(-0.3, 5) == 4.7
        assert PyFinancialLibrary.sum(-0.3, -5) == -5.3
        
        self.assertRaises(TypeError, PyFinancialLibrary.sum(3, "-5"), -1, -1)
        self.assertRaises(TypeError, PyFinancialLibrary.sum(3, PyFinancialLibrary()), -1, -1)
    
    def testMinus(self):
        """ Verifies the minus method of pyFinancialLibrary.py """
        assert PyFinancialLibrary.minus(1, 2) == -1
        assert PyFinancialLibrary.minus(0, 0) == 0
        assert PyFinancialLibrary.minus(-5, 5) == -10
        assert PyFinancialLibrary.minus(-0.3, 5) == -5.3
        assert PyFinancialLibrary.minus(-0.3, -5) == 4.7
        
        self.assertRaises(TypeError, PyFinancialLibrary.minus(3, "-5"), -1, -1)
        self.assertRaises(TypeError, PyFinancialLibrary.minus(3, PyFinancialLibrary()), -1, -1)
    
    def testMult(self):
        """ Verifies the mult method of pyFinancialLibrary.py """
        assert PyFinancialLibrary.mult(1, 2) == 2
        assert PyFinancialLibrary.mult(0, 0) == 0
        assert PyFinancialLibrary.mult(-5, 5) == -25
        assert PyFinancialLibrary.mult(-0.3, 5) == -1.5
        assert PyFinancialLibrary.mult(-0.3, -5) == 1.5
        
        self.assertRaises(TypeError, PyFinancialLibrary.mult(3, "-5"), -1, -1)
        self.assertRaises(TypeError, PyFinancialLibrary.mult(3, PyFinancialLibrary()), -1, -1)    

    def testDiv(self):
        """ Verifies the div method of pyFinancialLibrary.py """
        assert PyFinancialLibrary.div(1, 2) == 0.5
        assert PyFinancialLibrary.div(-5, 5) == -1
        assert PyFinancialLibrary.div(-0.3, 5) == -0.06
        assert PyFinancialLibrary.div(-0.3, -5) == 0.06
        
        self.assertRaises(TypeError, PyFinancialLibrary.div(3, "-5"), -1, -1)
        self.assertRaises(TypeError, PyFinancialLibrary.div(3, PyFinancialLibrary()), -1, -1)
        self.assertRaises(TypeError, PyFinancialLibrary.div(3, 0), -1, -1) 
        self.assertRaises(TypeError, PyFinancialLibrary.div(0, 0), -1, -1)   
