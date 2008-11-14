import unittest
from financialLibrary import pyFinancialLibrary

class LibraryTestCase (unittest.TestCase):
    
    def testSum(self):
        """ Verifies the sum method of pyFinancialLibrary.py """
        assert pyFinancialLibrary.sum(1, 2) == 3
        assert pyFinancialLibrary.sum(0, 0) == 0
        assert pyFinancialLibrary.sum(-5, 5) == 0
        assert pyFinancialLibrary.sum(-0.3, 5) == 4.7
        assert pyFinancialLibrary.sum(-0.3, -5) == -5.3
        
        self.assertRaises(TypeError, pyFinancialLibrary.sum(3, "-5"), -1, -1)
    
    def testMinus(self):
        """ Verifies the minus method of pyFinancialLibrary.py """
        assert pyFinancialLibrary.minus(1, 2) == -1
        assert pyFinancialLibrary.minus(0, 0) == 0
        assert pyFinancialLibrary.minus(-5, 5) == -10
        assert pyFinancialLibrary.minus(-0.3, 5) == -5.3
        assert pyFinancialLibrary.minus(-0.3, -5) == 4.7
        
        self.assertRaises(TypeError, pyFinancialLibrary.minus(3, "-5"), -1, -1)
    
    def testMult(self):
        """ Verifies the mult method of pyFinancialLibrary.py """
        assert pyFinancialLibrary.mult(1, 2) == 2
        assert pyFinancialLibrary.mult(0, 0) == 0
        assert pyFinancialLibrary.mult(-5, 5) == -25
        assert pyFinancialLibrary.mult(-0.3, 5) == -1.5
        assert pyFinancialLibrary.mult(-0.3, -5) == 1.5
        
        self.assertRaises(TypeError, pyFinancialLibrary.mult(3, "-5"), -1, -1)

    def testDiv(self):
        """ Verifies the div method of pyFinancialLibrary.py """
        assert pyFinancialLibrary.div(1, 2) == 0.5
        assert pyFinancialLibrary.div(-5, 5) == -1
        assert pyFinancialLibrary.div(-0.3, 5) == -0.06
        assert pyFinancialLibrary.div(-0.3, -5) == 0.06
        
        self.assertRaises(TypeError, pyFinancialLibrary.div(3, "-5"), -1, -1)
        self.assertRaises(TypeError, pyFinancialLibrary.div(3, 0), -1, -1) 
        self.assertRaises(TypeError, pyFinancialLibrary.div(0, 0), -1, -1)   
