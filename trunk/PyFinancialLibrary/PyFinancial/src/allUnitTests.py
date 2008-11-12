import unittest
from calcElements.stackTests import calcStackTestCase

if __name__ == "__main__":
    suite1 = unittest.makeSuite(calcStackTestCase, "test")
    
    runner = unittest.TextTestRunner()
    runner.run(suite1)