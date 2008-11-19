from financialLibrary.pyFinancialLibrary import *
import unittest

class LibraryTestCase (unittest.TestCase):
    
    def testSum(self):
        """ Verifies the sum method of pyFinancialLibrary.py """
        assert sum(1, 2) == 3
        assert sum(0, 0) == 0
        assert sum(-5, 5) == 0
        assert sum(-0.3, 5) == 4.7
        assert sum(-0.3, -5) == -5.3
        
        self.assertRaises(TypeError, sum(3, "-5"), -1, -1)
    
    def testMinus(self):
        """ Verifies the minus method of pyFinancialLibrary.py """
        assert minus(1, 2) == 1
        assert minus(0, 0) == 0
        assert minus(-5, 5) == 10
        assert minus(-0.3, 5) == 5.3
        assert minus(-0.3, -5) == -4.7
        
        self.assertRaises(TypeError, minus(3, "-5"), -1, -1)
    
    def testMult(self):
        """ Verifies the mult method of pyFinancialLibrary.py """
        assert mult(1, 2) == 2
        assert mult(0, 0) == 0
        assert mult(-5, 5) == -25
        assert mult(-0.3, 5) == -1.5
        assert mult(-0.3, -5) == 1.5
        
        self.assertRaises(TypeError, mult(3, "-5"), -1, -1)

    def testDiv(self):
        """ Verifies the div method of pyFinancialLibrary.py """
        assert div(1, 2) == 2
        assert div(2, 1) == 0.5
        assert div(-5, 5) == -1
        assert div(5, -0.3) == -0.06
        assert div(-5, -0.3) == 0.06
        
        self.assertRaises(TypeError, div(3, "-5"), -1, -1) 
