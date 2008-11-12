import unittest
from calcStack import *

class calcStackTestCase (unittest.TestCase):
    
    def testConstruction(self):
        """ Verifies the construction of a stack """
        
        #Testing the construction of a stack without pre-determined values
        stack = calcStack()
        assert stack != None
        assert stack == [0.0, 0.0, 0.0, 0.0]
        
        #Constructing with determined values
        stack = calcStack([1,2,3,4])
        assert stack != None
        assert stack == [1,2,3,4]
        
        stack = calcStack([10000000000000.0000,0.000271,677625,854775.8266235553])
        assert stack != None
        assert stack == [10000000000000.0000,0.000271,677625,854775.8266235553]
        
        #Invalid constructions
        stack = calcStack([1,2,3])
        assert stack != None
        assert stack == [0.0, 0.0, 0.0, 0.0]
        
        stack = calcStack([])
        assert stack != None
        assert stack == [0.0, 0.0, 0.0, 0.0]
        
        stack = calcStack(None)
        assert stack != None
        assert stack == [0.0, 0.0, 0.0, 0.0]
        
    def testReplaceAll(self):
        """ Verifies if the substitution of stack elements is being done correctly """
        
        #Valid replaces
        stack = calcStack()
        stack.replaceAll([0.0,0.0,0.0,0.0])
        assert stack == [0.0,0.0,0.0,0.0]
        
        stack.replaceAll([1,2,3,4])
        assert stack == [1,2,3,4]
        
        stack.replaceAll([10000000000000.0000,0.000271,677625,854775.8266235553])
        assert stack == [10000000000000.0000,0.000271,677625,854775.8266235553]
        
        #Invalid replaces
        stack = calcStack()
        stack.replaceAll([])
        assert stack == [0.0,0.0,0.0,0.0]
        
        stack.replaceAll([2913847, 999887.999990011111, 1])
        assert stack == [0.0,0.0,0.0,0.0]
        
        stack.replaceAll(None)
        assert stack == [0.0,0.0,0.0,0.0]
        
    def testExchangeXAndY(self):
        """ Verifies if the exchanging of values between the X and the Y registers is correct """
        
        #Verifying one exchange
        stack = calcStack([1,2,3,4])
        stack.exchangeXAndY()
        assert stack != None
        assert stack == [2,1,3,4]
        
        #Exchanging again
        stack.exchangeXAndY()
        assert stack != None
        assert stack == [1,2,3,4]
        
        #One more time
        stack.exchangeXAndY()
        assert stack != None
        assert stack == [2,1,3,4]
    
    def testRollCounterClockWise(self):
       """ Tests if the rotation of registers values is being done correctly, e.g, 
       X assumes Y value, Y assumes Z, Z assumes W and W assumes X previous value """
       
       #Verifying one exchange
       stack = calcStack([1,2,3,4])
       stack.rollCounterClockWise() 
       assert stack != None
       assert stack == [2,3,4,1]
       
       #Second exchange
       stack.rollCounterClockWise() 
       assert stack != None
       assert stack == [3,4,1,2]
       
       #Third exchange
       stack.rollCounterClockWise() 
       assert stack != None
       assert stack == [4,1,2,3]
       
       #Fourth exchange
       stack.rollCounterClockWise() 
       assert stack != None
       assert stack == [1,2,3,4]
       
       #Starting all over again
       stack.rollCounterClockWise() 
       assert stack != None
       assert stack == [2,3,4,1]
        
    def testRollClockWise(self):
       """ Verifies if the rotation of registers values is being done correctly,
       e.g, W assumes Z, Z assumes Y, Y assumes X, X assumes W previous value """
       
       #Verifying one exchange
       stack = calcStack([1,2,3,4])
       stack.rollClockWise()
       assert stack != None
       assert stack == [4,1,2,3]
       
       #Second exchange
       stack.rollClockWise()
       assert stack != None
       assert stack == [3,4,1,2]
       
       #Third exchange
       stack.rollClockWise()
       assert stack != None
       assert stack == [2,3,4,1]
       
       #Fourth exchange
       stack.rollClockWise()
       assert stack != None
       assert stack == [1,2,3,4]
       
       #Starting all over again
       stack.rollClockWise()
       assert stack != None
       assert stack == [4,1,2,3]             