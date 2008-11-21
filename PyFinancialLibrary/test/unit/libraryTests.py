from financialLibrary.pyFinancialLibrary import *
import unittest

class LibraryTestCase (unittest.TestCase):
    
    def testSum(self):
        """ Verifies the add method of pyFinancialLibrary.py """
        assert add(1, 2) == 3
        assert add(0, 0) == 0
        assert add(-5, 5) == 0
        assert add(-0.3, 5) == 4.7
        assert add(-0.3, -5) == -5.3
        
        self.assertRaises(TypeError, add(3, "-5"), -1, -1)
    
    def testMinus(self):
        """ Verifies the sub method of pyFinancialLibrary.py """
        assert sub(2, 1) == 1
        assert sub(0, 0) == 0
        assert sub(5, -5) == 10
        assert sub(5, -0.3) == 5.3
        assert sub(-5, -0.3) == -4.7
        
        self.assertRaises(TypeError, sub(3, "-5"), -1, -1)
    
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
        assert div(1, 2) == 0.5
        assert div(2, 1) == 2
        assert div(-5, 5) == -1
        assert div(-0.3, 5) == -0.06
        assert div(-0.3, -5) == 0.06
        
        self.assertRaises(TypeError, div(3, "-5"), -1, -1) 
        self.assertRaises(ZeroDivisionError, div(3, 0), -1, -1)
